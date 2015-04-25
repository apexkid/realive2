# __author__ = 'shanshul'

from . import api_blueprint as app
from flask.ext.classy import FlaskView
from bidding import models as km
from flask import Response, request
from bson import json_util
import json
from datetime import datetime

class CommentAPI(FlaskView):
    def get(self, comment_id):
        try:
            comment = km.Comment.objects.get(id=comment_id)
            return Response(json.dumps(comment.to_json(), default=json_util.default), status=200, content_type="application/json")
        except Exception,e :
            return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")

    def post(self):
        data = request.form
        if not data:
            data = request.json
        comment = km.Comment()
        keys = data.keys()
        if 'campaign_id' in keys:
            campaign = km.Campaign.objects.get(id=data['campaign_id'])
            comment.campaign_id = campaign
        if 'user' in keys:
            user = km.User.objects.get(id=data['user'])
            comment.user = user
        if 'content' in keys:
            comment.content = data['content']
        if 'longitude' in keys:
            comment.longitude = data['longitude']
        if 'latitude' in keys:
            comment.latitude = data['latitude']

        comment.added_on = datetime.now()
        try:
            comment.save()
            return Response(json.dumps(comment.to_json(), default=json_util.default), status=200, content_type="application/json")
        except Exception,e :
            return Response(json.dumps({'details':'Exception: %s'%repr(e)}), status=403, content_type="application/json")



CommentAPI.register(app)