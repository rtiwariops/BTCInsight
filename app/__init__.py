# # -*- coding: utf-8 -*-

# third-party imports
from flask import Flask

# local imports
from instance.config import app_config

app = Flask(__name__)


def create_app(config_name):
    app.config.from_pyfile('instance/config.py')
    from .home import home as home_blueprint
    app.register_blueprint(home_blueprint)
    return app
