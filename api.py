from fastapi import FastAPI
from utils import fetch_news, analyze_sentiment, generate_hindi_tts

app = FastAPI()


@app.get("/analyze")
def analyze(company: str):
    articles = fetch_news(company)
    sentiments = analyze_sentiment(articles)
    audio_file = generate_hindi_tts(sentiments)

    return {"articles": sentiments, "audio_file": audio_file}
