import matplotlib.pyplot as plt
import streamlit as st
import pandas as pd
import plotly.express as px
from wordcloud import WordCloud
from sklearn.metrics import accuracy_score

def plot_sentiment_pie(data):
    sentiments = [item['sentiment'] for item in data]
    labels = ['Positive', 'Negative', 'Neutral']
    sizes = [sentiments.count('positive'), sentiments.count('negative'), sentiments.count('neutral')]

    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%', startangle=140)
    ax.axis('equal')
    st.pyplot(fig)

def generate_wordcloud(data):
    text = " ".join(item['text'] for item in data)
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text)

    fig, ax = plt.subplots()
    ax.imshow(wordcloud, interpolation='bilinear')
    ax.axis('off')
    st.pyplot(fig)
    
def display_sentiment_line_chart(data):
    """
    Displays a sentiment trend line chart over time.
    Accepts a list of dicts with at least 'timestamp' and 'sentiment'.
    """

    if not data or 'timestamp' not in data[0] or 'sentiment' not in data[0]:
        st.warning("⏳ No timestamp or sentiment data available to show trend.")
        return

    df = pd.DataFrame(data)
    df['timestamp'] = pd.to_datetime(df['timestamp'], errors='coerce')
    df['date'] = df['timestamp'].dt.date  # Group by date only
    df['count'] = 1

    # Grouping sentiment counts by date and sentiment
    grouped = df.groupby(['date', 'sentiment'])['count'].count().reset_index()
    pivoted = grouped.pivot(index='date', columns='sentiment', values='count').fillna(0)

    # Plotly line chart for better control and style
    fig = px.line(
        pivoted,
        x=pivoted.index,
        y=pivoted.columns,
        labels={'value': 'Post Count', 'date': 'Date'},
        title="📈 Sentiment Trend Over Time",
        markers=True
    )

    st.subheader("📅 Sentiment Over Time")
    st.plotly_chart(fig, use_container_width=True)
        
def plot_sentiment_bar(data):
    sentiments = [item['sentiment'] for item in data]
    df = pd.DataFrame(sentiments, columns=['Sentiment'])
    count = df.value_counts().reset_index(name='Count')

    st.subheader("📊 Sentiment Count - Bar Chart")
    st.bar_chart(count.set_index("Sentiment"))
    
def show_data_table(data):
    df = pd.DataFrame(data)
    st.subheader("📋 Raw Data Table")
    st.dataframe(df)
    
def show_map_if_available(data):
    # Check if any location fields exist
    locations = []
    for item in data:
        if 'lat' in item and 'lon' in item:
            locations.append({'lat': item['lat'], 'lon': item['lon']})
    if locations:
        df_map = pd.DataFrame(locations)
        st.subheader("🗺️ Map of Locations (if any)")
        st.map(df_map)
        
def plot_platform_comparison(data):
    st.markdown("#### Sentiment by Platform")

    df = pd.DataFrame(data)

    # Accuracy (optional)
    if 'true_sentiment' in df.columns and 'sentiment' in df.columns:
        accuracy = accuracy_score(df['true_sentiment'], df['sentiment'])
        st.success(f"✅ Sentiment Prediction Accuracy: **{accuracy*100:.2f}%**")

    # Platform Sentiment Chart
    if "source" in df.columns and "sentiment" in df.columns:
        platform_sentiment = df.groupby(['source', 'sentiment']).size().unstack(fill_value=0)

        fig, ax = plt.subplots(figsize=(10, 5))
        platform_sentiment.plot(kind="bar", stacked=True, ax=ax, colormap="Set3")
        plt.title("Sentiment Distribution by Platform")
        plt.xlabel("Platform")
        plt.ylabel("Number of Posts")
        plt.xticks(rotation=45)
        st.pyplot(fig)
    else:
        st.warning("Required fields 'source' and 'sentiment' not found in data.")
      