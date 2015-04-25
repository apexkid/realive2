# __author__ = 'shanshul'


from . import db

class User(db.Document):
    userid = db.StringField(required=True)
    name = db.StringField(required=True)

