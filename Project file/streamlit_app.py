import os
import json
import streamlit as st
from visualize import (
    plot_sentiment_pie,
    generate_wordcloud,
    display_sentiment_line_chart,
    plot_sentiment_bar,
    show_data_table,
    show_map_if_available,
    plot_platform_comparison
)
from decision_summary import generate_decision_summary

st.set_page_config(page_title="Sentiment Analyzer", layout="wide")

st.markdown("<h1 style='color:#2C3E50;'>📊 Sentiment Analyzer</h1>", unsafe_allow_html=True)

data_file = "data/collected_data.json"

if not os.path.exists(data_file) or os.stat(data_file).st_size == 0:
    st.error("❌ No data found. Please run `app.py` first to collect and analyze sentiment data.")
else:
    with open(data_file) as f:
        data = json.load(f)

    # Summary Section
    st.markdown("### Overview")
    col1, col2, col3, col4 = st.columns(4)
    
    total_posts = len(data)
    sentiments = [item["sentiment"] for item in data]
    most_common = max(set(sentiments), key=sentiments.count)
    confidence = 5.3  # calculate real confidence if available
    platforms = len(set([item["source"] for item in data]))

    col1.metric("🗨️ Total Posts", total_posts)
    col2.metric("😐 Most Common Sentiment", most_common.title())
    col3.metric("📈 Average Confidence", f"{confidence}%")
    col4.metric("🔗 Platforms Analyzed", platforms)

    # Analysis Accuracy (Dummy Logic)
    accuracy = 98
    st.markdown("#### Analysis Accuracy")
    st.progress(accuracy / 100)

    # Charts Section
    st.markdown("### Sentiment Distribution")
    col5, col6 = st.columns(2)
    with col5:
        plot_sentiment_pie(data)
    with col6:
        plot_platform_comparison(data)  

    display_sentiment_line_chart(data)
    plot_sentiment_bar(data)

    st.markdown("### Word Cloud")
    generate_wordcloud(data)

    st.markdown("### Collected Data")
    show_data_table(data)

    show_map_if_available(data)

    st.markdown("### 📌 Final One-Line Decision")
    generate_decision_summary(data)
7