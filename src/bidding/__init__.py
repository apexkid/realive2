# __author__ = 'shanshul'

# -*- coding: utf-8 -*-

from flask import Flask
from celery import Celery
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin import Admin
from flask_oauth import OAuth

import jinja2
import os

from flask import Flask

admin = None
db = MongoEngine()
app = None
oauth = OAuth()

def create_app(package_name='bidding'):
    """Returns a :class:`Flask` application instance configured with common
    functionality for the korath platform.

    :param package_name: application package name
    :param package_path: application package path
    :param config_name: can have one of [production, development, testing]
    """
    global app, admin
    app = Flask(package_name, instance_relative_config=True)

    config_name = os.environ.get('bidding_CONFIG_NAME', 'Production')

    app.config.from_object('configurations.%s'%config_name.title())

    app.jinja_loader = jinja2.ChoiceLoader([
        app.jinja_loader,
        jinja2.FileSystemLoader('bidding/templates/'),
    ])

    db.init_app(app)
    admin = Admin(app, 'Our own CMS', base_template='layout.html')

    from . import views
    from views import api_blueprint
    app.register_blueprint(api_blueprint)
    from views import comment_blueprint
    app.register_blueprint(comment_blueprint)
    from views import fb_blueprint
    app.register_blueprint(fb_blueprint)
    from views import static_blueprint
    app.register_blueprint(static_blueprint)


    from . import models

    # for admin panel
    from . import admin_panel
    return app

