# __author__ = 'shanshul'

from . import api_blueprint as app
from flask.ext.classy import FlaskView, route
from bidding import models as km
import json
from flask import Response, request, session
from bson import json_util
from datetime import datetime

class Campaign(FlaskView):
    def index(self):
        response = {}

        is_active = request.args.get('is_active')
        is_deleted = request.args.get('is_deleted')

        print is_active, type(is_active), is_deleted

        try:
            if is_active:
                if is_deleted is not None:
                    campaign = km.Campaign.objects.filter(is_deleted=True, is_active=True)
                else:
                    campaign = km.Campaign.objects.filter(is_active=True)
            elif is_deleted:
                campaign = km.Campaign.objects.filter(is_deleted=True)
            else:
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
        campaign.user = km.User.objects.get(user_id=session['user_id'])
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


    @route('/<id>/comment')
    def comment(self, id):
        try:
            comments = km.Comment.objects.filter(campaign_id=id)
            list_of_comment = []
            for comment in comments:
                list_of_comment.append(comment.to_json())
            return Response(json.dumps(list_of_comment, default=json_util.default), status=200, content_type="application/json")
        except Exception, e:
            return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")



Campaign.register(app)