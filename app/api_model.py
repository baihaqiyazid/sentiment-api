from flask_restx import fields

from .extension import api

sentiment_model = api.model('Sentiment', {
    "classified_text": fields.String,
    "tweet_text": fields.String,
    "sentence_score": fields.String,
    "max_positive": fields.Integer,
    "max_negative": fields.Integer,
    "kelas": fields.String,
})

sentiment_input_model = api.model("SentimentInput", {
    "tweet_text": fields.String,
})