from flask import render_template

from extensions import db
from models import cafe
from app import create_app

app = create_app()

@app.route('/')
def index():
    data = db.session.query(cafe).all()
    return render_template('index.html', data=data)