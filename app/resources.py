from flask_restx import Resource, Namespace
from .api_model import sentiment_input_model, response_success, response_method_not_allowed, response_bad_request, response_parameter_not_valid
from .sentistrength_id import senti
from .response import ResponseFormat
from werkzeug.exceptions import BadRequest, InternalServerError

ns = Namespace("api/v1")

@ns.route("/predict")
class SentimentAPI(Resource):
    @ns.expect(sentiment_input_model)
    @ns.response(200, 'Success', response_success)
    @ns.response(405, 'Method Not Allowed', response_method_not_allowed)
    @ns.response(400, 'Bad Request', response_bad_request)
    @ns.response(500, 'Parameter Not Valid', response_parameter_not_valid)
    def post(self):

        if "sentence" not in ns.payload:
            raise InternalServerError("parameter not valid")
        
        
        if ns.payload["sentence"] == None or ns.payload["sentence"] == "":
            raise BadRequest("No text provided")
        

        output = senti.main(ns.payload["sentence"])
        sentiment_data = {
        "classified_text": output['classified_text'],
            "tweet_text"    : ns.payload["sentence"],
            "sentence_score": output['sentence_score'],
            "max_positive"  : output['max_positive'],
            "max_negative"  : output['max_negative'],
            "kelas"         : output['kelas'],
        }
        
        response = ResponseFormat(data=sentiment_data, message="").to_dict()

        return response    