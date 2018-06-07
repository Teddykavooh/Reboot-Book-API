from flask import Flask
from flask_restplus import Api
from instance.config import app_config


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    api = Api(app=app)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False

    @app.route('/')
    def index_page():
            return {'It bloody works'}
    return app
