# __author__ = 'shanshul'


from flask import Blueprint

api_blueprint = Blueprint('api_blueprint', __name__)

comment_blueprint = Blueprint('comment_blueprint', __name__)

from . import api
from . import comment_api