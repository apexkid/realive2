# __author__ = 'shanshul'


from . import db
from datetime import datetime


class User(db.Document):
    user_id = db.StringField(required=True)
    name = db.StringField(required=True)
    is_active = db.BooleanField(default=True)
    is_deleted = db.BooleanField(default=False)
    added_on = db.DateTimeField()
    modified_on = db.DateTimeField()

    def save(self, *args, **kwargs):
        self.modified_on = datetime.now()
        super(User, self).save(*args, **kwargs)


class Campaign(db.Document):
    city = db.StringField(max_length=30)
    officeLocation = db.StringField(max_length=100)
    localityPref = db.StringField(max_length=100)
    poi = db.StringField(max_length=100)
    livingCost = db.IntField()
    priorities = db.StringField(max_length=100)
    is_active = db.BooleanField(default=True)
    is_deleted = db.BooleanField(default=False)
    added_on = db.DateTimeField()
    modified_on = db.DateTimeField()

    def save(self, *args, **kwargs):
        self.modified_on = datetime.now()
        super(Campaign, self).save(*args, **kwargs)

    def to_json(self):
        return {
            'id': self.id,
            'city': self.city,
            'officeLocation': self.officeLocation,
            'localityPref': self.localityPref,
            'poi': self.poi,
            'livingCost': self.livingCost,
            'priorities': self.priorities,
            'is_active': self.is_active,
            'is_deleted': self.is_deleted,
            'added_one': self.added_on,
            'modified_on': self.modified_on

        }