from flask import Flask
from datetime import timedelta
from sqlalchemy import select
from extensions import db, login_manager, bootstrap
from flask_migrate import Migrate

def create_app():
    app = Flask(__name__)

    with open('csrfkey.txt', 'r') as file:
        app.config['SECRET_KEY'] = file.readline().strip('\n')

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
    app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(minutes=30)  # Time the user out after 30 minutes

    db.init_app(app)
    bootstrap.init_app(app)
    migrate = Migrate(app, db)

    from models import cafe




    return app