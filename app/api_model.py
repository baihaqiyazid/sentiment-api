from flask_restx import fields

from .extension import api

response_success = api.model('ResponseSuccess', {
    "code": fields.Integer(200),
    "status": fields.String("success"),
    "message": fields.String(""),
    "result": fields.Nested(api.model('Sentiment', {
        "classified_text": fields.String("agnezmo pintar [4] dan cantik [6] sekali tetapi lintah darat [-4] :) [3]"),
    "tweet_text": fields.String("agnezmo pintar dan cantik sekali tetapi lintah darat :)"),
    "sentence_score": fields.Raw([
            "agnezmo pintar [4] dan cantik [6] sekali tetapi lintah darat [-4] :) [3]"
        ]),
    "max_positive": fields.Integer(6),
    "max_negative": fields.Integer(-4),
    "kelas": fields.String("positive"),
    })),
})

response_method_not_allowed = api.model('ResponseMethodNotAllowed', {
    "code": fields.Integer(405),
    "status": fields.String("NOK"),
    "message": fields.String("Method Not Found!"),
})

response_bad_request = api.model('ResponseBadRequest', {
    "code": fields.Integer(400),
    "status": fields.String("Bad Request"),
    "message": fields.String("No text provided"),
})

response_parameter_not_valid = api.model('ResponseParameterNotValid', {
    "code": fields.Integer(500),
    "status": fields.String("NOK"),
    "message": fields.String("parameter not valid"),
})

sentiment_model = api.model('SentimentModel', {
    "classified_text": fields.String("agnezmo pintar [4] dan cantik [6] sekali tetapi lintah darat [-4] :) [3]"),
    "tweet_text": fields.String("agnezmo pintar dan cantik sekali tetapi lintah darat :)"),
    "sentence_score": fields.Raw([
            "agnezmo pintar [4] dan cantik [6] sekali tetapi lintah darat [-4] :) [3]"
        ]),
    "max_positive": fields.Integer(6),
    "max_negative": fields.Integer(-4),
    "kelas": fields.String("positive"),
})

sentiment_input_model = api.model("SentimentInput", {
    "sentence": fields.String("agnezmo pintar dan cantik sekali tetapi lintah darat :)"),
})