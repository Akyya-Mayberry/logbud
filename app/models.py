# Python libs

# 3rd party libs
from flask_login import UserMixin
from flask_sqlalchemy import SQLAlchemy

# My libs
from app import db


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

    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __repr__(self):

        return "Name: %s %s" % (self.firstname, self.lastname)


class Visit(db.Model):
    """ Logs all visits """

    __tablename__ = "visits"

    id = db.Column(db.Integer, primary_key=True)

    visitor_id = db.Column(db.Integer, db.ForeignKey('visitors.id'))
    visiting = db.Column(db.String(100))
    purpose = db.Column(db.Text)
    active = db.Column(db.Boolean, default=False)

    visitor = db.relationship('Visitor', backref=db.backref('visits', lazy='dynamic'))

    def __init__(self, visitor_id, visiting, purpose):
        self.visitor_id = visitor_id
        self.visiting = visiting
        self.purpose = purpose
        self.active = True

    def is_active(self):
        return self.active

    def __repr__(self):
        return "Visitor: %s, Visiting: %s, Purpose: %s" % (self.visitor_id, self.visiting, self.purpose)


# def connect_to_db(app, db_uri=None):
#     """ Connect application to database """
#     app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///logbud'
#     # app.config['SQLALCHEMY_ECHO'] = True
#     db.app = app
#     db.init_app(app)
#     db.create_all(app=app)
def connect_to_db(app):
    """ Connect application to database """
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///party"
    # app.config['SQLALCHEMY_ECHO'] = True
    # db.app = app
    db.init_db(app)
    db.create_all(app=app)


if __name__ == "__main__":
    from app import app
    connect_to_db(app)
    print "Connected to DB."
