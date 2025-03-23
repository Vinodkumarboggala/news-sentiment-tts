import requests
from bs4 import BeautifulSoup
from textblob import TextBlob
from gtts import gTTS


def fetch_news(company):
    """Scrapes news articles related to the company."""
    search_url = f"https://news.google.com/search?q={company}"
    response = requests.get(search_url)
    soup = BeautifulSoup(response.text, "html.parser")

    articles = []
    for item in soup.find_all("article")[:10]:  # Get top 10 articles
        title = item.find("h3").text
        link = "https://news.google.com" + item.find("a")["href"][1:]
        articles.append({"title": title, "link": link})

    return articles


def analyze_sentiment(articles):
    """Performs sentiment analysis on each article."""
    for article in articles:
        response = requests.get(article["link"])
        soup = BeautifulSoup(response.text, "html.parser")
        content = " ".join([p.text for p in soup.find_all("p")])

        article["summary"] = content[:500]  # Simple summarization
        sentiment_score = TextBlob(content).sentiment.polarity
        if sentiment_score > 0:
            article["sentiment"] = "Positive"
        elif sentiment_score < 0:
            article["sentiment"] = "Negative"
        else:
            article["sentiment"] = "Neutral"

    return articles


def generate_hindi_tts(articles):
    """Converts sentiment summary to Hindi speech."""
    text = " ".join([f"{a['title']} is {a['sentiment']} news." for a in articles])
    tts = gTTS(text=text, lang="hi")
    tts.save("output.mp3")
    return "output.mp3"
