# __author__ = 'shanshul'


from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)

from . import api