# python std libs
import os

# 3rd party libs
from flask_debugtoolbar import DebugToolbarExtension

# my libs
from app import app


if __name__ == "__main__":
    # from flask_sqlalchemy import SQLAlchemy

    # db = SQLAlchemy()
    # def connect_to_db(app):
    #     """ Connect application to database """
    #     app.config['SQLALCHEMY_DATABASE_URI'] = "postgres:///logbud"
    #     # app.config['SQLALCHEMY_ECHO'] = True
    #     # db.app = app
    #     db.app = app
    #     db.init_app(app)
    #     db.create_all(app=app)

    # connect_to_db(app)
    # # Use the DebugToolbar
    # # DebugToolbarExtension(app)
    # PORT = int(os.environ.get("PORT", 8000))
    app.run()
