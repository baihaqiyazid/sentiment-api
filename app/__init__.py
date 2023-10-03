from flask import Flask

from app.response import ResponseFormat
from .extension import api
from .resources import ns
from werkzeug.exceptions import BadRequest

app = Flask(__name__)

api.init_app(app)
api.add_namespace(ns)

@api.errorhandler(BadRequest)
def badRequest(error):
    response = ResponseFormat(
        code=error.code,
        data=None, 
        message=error.description, 
        status=error.name
    ).to_dict()

    return response, error.code

@app.errorhandler(400)
def badRequest(error):
    response = ResponseFormat(
        code=error.code,
        data=None, 
        message=error.description, 
        status=error.name
    ).to_dict()

    return response, error.code

@app.errorhandler(404)
def notFound(error):
    response = ResponseFormat(
        code=error.code,
        data=None, 
        message=error.description, 
        status=error.name
    ).to_dict()

    return response, error.code

if __name__ == '__main__':
    app.run()

