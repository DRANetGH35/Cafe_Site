from flask import Flask
from datetime import timedelta
from sqlalchemy import select
from extensions import db, login_manager, bootstrap


def create_app():
    app = Flask(__name__)

    with open('csrfkey.txt', 'r') as file:
        app.config['SECRET_KEY'] = file.readline().strip('\n')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Time the user out after 30 minutes

    db.init_app(app)
    login_manager.init_app(app)
    bootstrap.init_app(app)



    with app.app_context():
        db.create_all()



    return app