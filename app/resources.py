from flask_restx import Resource, Namespace
from .api_model import sentiment_input_model, sentiment_model
from .models import Sentiment 
from .sentistrength_id import senti

ns = Namespace("api/v1")

@ns.route("/predict")
class SentimentAPI(Resource):

    @ns.expect(sentiment_input_model)
    @ns.marshal_with(sentiment_model)
    def post(self):
        output = senti.main(ns.payload["tweet_text"])
        sentiment = Sentiment(
            classified_text=output['classified_text'],
            tweet_text=ns.payload["tweet_text"],
            sentence_score=output['sentence_score'],
            max_positive=output['max_positive'],
            max_negative=output['max_negative'],
            kelas=output['kelas'],
        )
       
        return sentiment
