# __author__ = 'shanshul'

from . import api_blueprint as app
from flask.ext.classy import FlaskView

class API(FlaskView):
    def get(self):
        return NotImplemented

    def post(self):
        return NotImplemented


API.register(app)