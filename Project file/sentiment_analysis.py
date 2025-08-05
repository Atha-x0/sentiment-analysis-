from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import emoji
from langdetect import detect

# Load Models
roberta_model = "cardiffnlp/twitter-roberta-base-sentiment"
multilang_model = "nlptown/bert-base-multilingual-uncased-sentiment"  # OR xlm-roberta

roberta_tokenizer = AutoTokenizer.from_pretrained(roberta_model)
roberta_model = AutoModelForSequenceClassification.from_pretrained(roberta_model)

multilang_tokenizer = AutoTokenizer.from_pretrained(multilang_model)
multilang_model = AutoModelForSequenceClassification.from_pretrained(multilang_model)

# Label maps
roberta_labels = ['negative', 'neutral', 'positive']
multilang_labels = ['very negative', 'negative', 'neutral', 'positive', 'very positive']

# Preprocess emojis
def preprocess(text):
    return emoji.demojize(text)

# Language-based model selector
def detect_language(text):
    try:
        return detect(text)
    except:
        return "unknown"

# Main multi-model sentiment analyzer
def analyze_sentiment(text):
    lang = detect_language(text)
    text = preprocess(text)

    if lang in ['en']:  # English = Twitter Roberta
        tokenizer = roberta_tokenizer
        model = roberta_model
        labels = roberta_labels
    else:  # Other language = Multilingual
        tokenizer = multilang_tokenizer
        model = multilang_model
        labels = multilang_labels

    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True, max_length=512)
    with torch.no_grad():
        outputs = model(**inputs)
        probs = torch.nn.functional.softmax(outputs.logits, dim=1)
        pred = torch.argmax(probs)

    return labels[pred]
