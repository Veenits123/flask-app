# setting up
import os 
from flask import Flask
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate 

basedir = os.path.abspath(os.path.dirname(__file__))
# __file__ is the file name of current script file
# inner part gets the foldername and later returns the actua path according to current os

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///'+os.path.join(basedir, 'data.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 

db = SQLAlchemy(app)

Migrate(app,db)