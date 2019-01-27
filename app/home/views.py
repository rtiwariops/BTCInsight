from flask import current_app, render_template
from . import home
from .. import app


@home.route('/', methods=['GET'])
def index():
    """
    Render the dashboard template on the /dashboard route
    """
    return render_template('home/bitcoin.html')
