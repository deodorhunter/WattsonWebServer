from flask import Flask
from flask_restful import Api

from src.commons.extensions import cache


def createApi(app):
    api = Api(app)
    return api

def createApp():
    app = Flask(__name__)
    cache.init_app(app, config={'CACHE_TYPE': 'simple'})

    return app