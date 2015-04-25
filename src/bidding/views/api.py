# __author__ = 'shanshul'

from . import api_blueprint as app
from flask.ext.classy import FlaskView
from bidding import models as km
import json
from flask import Response, request
from bson import json_util
from datetime import datetime

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
        data = request.form
        if not data:
            data = request.json
        campaign = km.Campaign()
        keys = data.keys()
        if 'city' in keys:
            campaign.city = data['city']
        if 'officeLocation' in keys:
            campaign.officeLocation = data['officeLocation']
        if 'localityPref' in keys:
            campaign.localityPref = data['localityPref']
        if 'poi' in keys:
            campaign.poi = data['poi']
        if 'livingCost' in keys:
            try:
                campaign.livingCost = int(data['livingCost'])
            except Exception,e :
                return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")
        if 'priorities' in keys:
            campaign.priorities = data['priorities']
        campaign.added_on = datetime.now()
        try:
            campaign.save()
            return Response(json.dumps(campaign.to_json(), default=json_util.default), status=200, content_type="application/json")
        except Exception,e :
            return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")

    def delete(self, c_id):
        try:
            campaign = km.Campaign.objects.get(id=c_id)
            campaign.is_active = False
            campaign.is_deleted = True
            campaign.save()
            return Response(json.dumps(campaign.to_json(), default=json_util.default), status=200, content_type="application/json")
        except Exception,e:
            return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")



Campaign.register(app)