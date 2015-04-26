# __author__ = 'shanshul'

from flask import Flask, render_template, send_from_directory, url_for, request, session, redirect
from flask_oauth import OAuth
from bidding import app
from bidding import models
from datetime import datetime

#----------------------------------------
# initialization
#----------------------------------------


#----------------------------------------
# controllers
#----------------------------------------

oauth = OAuth()

facebook = oauth.remote_app('facebook',
    base_url='https://graph.facebook.com/',
    request_token_url=None,
    access_token_url='/oauth/access_token',
    authorize_url='https://www.facebook.com/dialog/oauth',
    consumer_key=FACEBOOK_APP_ID,
    consumer_secret=FACEBOOK_APP_SECRET,
    request_token_params={'scope': ('email, ')}
)

@facebook.tokengetter
def get_facebook_token():
    return session.get('facebook_token')

def pop_login_session():
    session.pop('logged_in', None)
    session.pop('facebook_token', None)

@app.route("/facebook_login")
def facebook_login():
    return facebook.authorize(callback=url_for('facebook_authorized',
        next=request.args.get('next'), _external=True))

@app.route("/facebook_authorized")
@facebook.authorized_handler
def facebook_authorized(resp):
    next_url = request.args.get('next') or url_for('index')
    if resp is None or 'access_token' not in resp:
        return redirect(next_url)

    session['logged_in'] = True
    session['facebook_token'] = (resp['access_token'], '')

    data = facebook.get('/me').data
    if 'id' in data and 'name' in data:
        user_id = data['id']
        user_name = data['name']
        session['name'] = user_name
        session['user_id'] = user_id
        try:
            user = models.User.objects.get(user_id=user_id)
        except Exception,e:
            user = models.User()
            user.user_id = user_id
            user.name = user_name
            user.added_on = datetime.now()
            user.save()
        print user_id
        print user_name

    return redirect('/static/campaign')

@app.route("/logout")
def logout():
    pop_login_session()
    return redirect(url_for('index'))

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/test")
def test():
    return render_template('testing.html')