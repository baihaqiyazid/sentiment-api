from flask_restx import Resource, Namespace
from .api_model import sentiment_input_model
from .sentistrength_id import senti
from .response import ResponseFormat

ns = Namespace("api/v1")

@ns.route("/predict")
class SentimentAPI(Resource):
    @ns.expect(sentiment_input_model)
    def post(self):
        if ns.payload["tweet_text"] == None or ns.payload["tweet_text"] == "":
            return  ResponseFormat(data=None, code=400, status="bad request",  message="no text").to_dict()

        output = senti.main(ns.payload["tweet_text"])
        sentiment_data = {
           "classified_text": output['classified_text'],
            "tweet_text"    : ns.payload["tweet_text"],
            "sentence_score": output['sentence_score'],
            "max_positive"  : output['max_positive'],
            "max_negative"  : output['max_negative'],
            "kelas"         : output['kelas'],
        }
        
        response = ResponseFormat(data=sentiment_data, message="success predict").to_dict()

        return response
