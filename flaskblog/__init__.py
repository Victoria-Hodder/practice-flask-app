from flask import Flask
from flask_sqlalchemy import SQLAlchemy #added this in models video
import os

app = Flask(__name__)
SECRET_KEY = os.urandom(16)
app.config['SECRET_KEY'] = SECRET_KEY
        #app.config['SECRET KEY'] = '21f61b7d2435cceca0c077d9e94125ad'

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)

from flaskblog import routes