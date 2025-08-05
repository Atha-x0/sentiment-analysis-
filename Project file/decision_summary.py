from transformers import pipeline
import streamlit as st
from transformers import AutoTokenizer

# Load model + tokenizer
summarizer = pipeline("summarization", model="sshleifer/distilbart-cnn-12-6")
tokenizer = AutoTokenizer.from_pretrained("sshleifer/distilbart-cnn-12-6")

def generate_decision_summary(data):
    COMMENTS_PER_CHUNK = 10
    MAX_TOKENS = 1024  # Model's input token limit

    # Extract all 'text' fields from the input data
    texts = [item['text'] for item in data if item.get('text')]

    chunk_summaries = []
    for i in range(0, len(texts), COMMENTS_PER_CHUNK):
        chunk = texts[i:i+COMMENTS_PER_CHUNK]
        joined = " ".join(chunk)

        # Truncate long input if needed
        inputs = tokenizer.encode(joined, return_tensors="pt", truncation=True, max_length=MAX_TOKENS)
        decoded_input = tokenizer.decode(inputs[0], skip_special_tokens=True)

        # Generate summary for the chunk with longer output
        sum_text = summarizer(
            decoded_input,
            max_length=150,   # Increased from 60 to 150
            min_length=80,    # Increased for more detail
            do_sample=False
        )[0]["summary_text"]

        chunk_summaries.append(sum_text)

    # Combine all chunk summaries and summarize again
    final_input = " ".join(chunk_summaries)
    inputs = tokenizer.encode(final_input, return_tensors="pt", truncation=True, max_length=MAX_TOKENS)
    final_input_trimmed = tokenizer.decode(inputs[0], skip_special_tokens=True)

    # Final detailed decision summary
    decision = summarizer(
        final_input_trimmed,
        max_length=200,   # Increased for final summary
        min_length=100,
        do_sample=False
    )[0]["summary_text"]

    st.subheader("📌 Final Decision / Summary of Public Opinion:")
    st.success(decision)
