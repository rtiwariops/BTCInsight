# # -*- coding: utf-8 -*-

# third-party imports
from flask import Flask

# local imports
from instance.config import app_config

app = Flask(__name__, instance_relative_config=True)


def create_app(config_name):
    app.config.from_object(app_config[config_name])
    app.config.from_pyfile('config.py')
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    return app
