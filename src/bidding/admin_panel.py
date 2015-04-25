# __author__ = 'shanshul'


from . import admin
from models import *

from flask.ext.admin.contrib.mongoengine import ModelView


class UserAdmin(ModelView):
    list_template = 'list.html'
    column_searchable_list = ('user_id', 'name')
    column_filters = ('user_id', 'name')
    can_delete = False

admin.add_view(UserAdmin(User))

class CampaignAdmin(ModelView):
    list_template = 'list.html'
    column_searchable_list = ('city', 'officeLocation')
    can_delete = False


admin.add_view(CampaignAdmin(Campaign))