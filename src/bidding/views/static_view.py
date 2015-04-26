# __author__ = 'shanshul'

from . import static_blueprint as app
from flask import render_template

@app.route('/static/index')
def index():
    return render_template('mockup/index.html')


@app.route('/static/campaign')
def campaign():
    return render_template('mockup/campaigns.html')
