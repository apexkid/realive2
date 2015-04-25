# __author__ = 'shanshul'


from . import admin
from models import *

from flask.ext.admin.contrib.mongoengine import ModelView


class UserAdmin(ModelView):
    list_template = 'list.html'
    column_searchable_list = ('userid', 'name')
    column_filters = ('userid', 'name')
    can_delete = False

admin.add_view(UserAdmin(User))