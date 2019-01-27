# -*- coding: utf-8 -*-

import os

from app import create_app

config_name = os.getenv('FLASK_CONFIG')
app = create_app('instance/config.py')

if __name__ == '__main__':
    app.run(debug=True)
