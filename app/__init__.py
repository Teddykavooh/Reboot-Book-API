from flask import Flask
from flask_restplus import Api
from instance.config import app_config


def create_app(config_name):

    app = Flask(__name__, instance_relative_config=True)

    api = Api(app=app)

    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    app.url_map.strict_slashes = False

    from resources.books import book_api
    api.add_namespace(book_api, path='/api/v1')
    from resources.admin import user_api
    api.add_namespace(user_api, path='/api/v1')
    from resources.users import register_user_api
    api.add_namespace(register_user_api, path='/api/v1')
    return app
