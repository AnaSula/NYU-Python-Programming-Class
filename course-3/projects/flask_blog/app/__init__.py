from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import LoginManager
from flask_openid import OpenID
from config import basedir
#from .momentjs import momentjs


app = Flask(__name__)
app.config.from_object('config')
db=SQLAlchemy(app)


lm = LoginManager()
lm.init_app(app)
oid = OpenID(app, os.path.join(basedir, 'tmp'))

#app.jinja_env.globals['momentjs'] = momentjs

from app import views, models
