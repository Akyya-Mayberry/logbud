# Python libs

# 3rd party libs
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('config-dev')
db = SQLAlchemy(app)

# My libs
# Load the views etc
from app import views, forms, views
