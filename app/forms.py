# python std libs

# 3rd party libs
from wtforms_components import TimeField
from wtforms import StringField, PasswordField, validators, TextAreaField
from flask_wtf import Form

# my libs


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
