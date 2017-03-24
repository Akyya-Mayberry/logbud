# Python libs

# 3rd party libs
from flask_sqlalchemy import SQLAlchemy
from wtforms import StringField, PasswordField, validators, SubmitField, TextAreaField
from flask_wtf import Form
from flask_login import UserMixin

# My libs
from app import app


db = SQLAlchemy(app)


class LoggerLoginForm(Form):
    """ Login for logger user accounts """

    email = StringField('Email Address', [validators.Length(min=6, max=35)])
    password = PasswordField('Password')
    # submit = SubmitField('Submit')


class VisitorSignInForm(Form):
    """ Sign form for visitors """

    firstname = StringField('First Name')
    lastname = StringField('Last Name')
    visiting = StringField('Visiting')
    purpose = TextAreaField('Reason for Visit')


class UserProfile(db.Model, UserMixin):
    """Users model"""

    __tablename__ = "user_profiles"

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), nullable=True)
    password = db.Column(db.String(100), nullable=True)


class Visitor(db.Model):
    """ Visitors model """

    __tablename__ = "visitors"

    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname = db.Column(db.String(50))
    visiting = db.Column(db.String(50))
    purpose = db.Column(db.String(50))

    def __init__(self, firstname, lastname, visiting, purpose):
        self.firstname = firstname
        self.lastname = lastname
        self.visiting = visiting
        self.purpose = purpose

    def __repr__(self):

        return "%s %s visiting: %s" % (self.firstname, self.lastname, self.visiting)


def connect_to_db(app, db_uri=None):
    """ Connect application to database """
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///logbud'
    # app.config['SQLALCHEMY_ECHO'] = True
    db.app = app
    db.init_app(app)
    db.create_all(app=app)
