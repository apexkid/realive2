# __author__ = 'shanshul'

from . import api_blueprint as app
from flask.ext.classy import FlaskView
from bidding import models as km
import json
from flask import Response, Request
from bson import json_util

class Campaign(FlaskView):
    def index(self):
        response = {}
        try:
            campaign = km.Campaign.objects
            response['campaign'] = []
            for c in campaign:
                response['campaign'].append(c.to_json())
            return Response(json.dumps(response, default=json_util.default), status=200, content_type="application/json")
        except Exception, e:
            return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")

    def get(self, c_id):
        try:
            campaign = km.Campaign.objects.get(id=c_id)
            return Response(json.dumps(campaign.to_json(), default=json_util.default), status=200, content_type="application/json")
        except Exception,e:
            return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")

    def post(self):
        return NotImplemented


Campaign.register(app)