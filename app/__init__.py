from flask import Flask
from .extension import api
from .resources import ns

def create_app():
    app = Flask(__name__)

    api.init_app(app)
    api.add_namespace(ns)

    return app