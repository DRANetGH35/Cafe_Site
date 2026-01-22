from flask import render_template

from extensions import db
from models import cafe
from app import create_app

app = create_app()
def extract_coords_from_google_link(url):
    if not url:
        return None
    for section in url.split('/'):
        if section.startswith('@'):
            lat = section.split(',')[0].replace("@", "")
            lng = section.split(',')[1]
            return [lat, lng]
    return None

@app.route('/')
def index():
    data = db.session.query(cafe).all()
    for loc in data:

        feature = {
                                "type": 'Feature',
                                "geometry": {
                                    "type": 'Point',
                                    "coordinates": [-118.84150346378853, 34.21002705418738]   // [lng, lat]
                                },
                                "properties": {
                                    "title": 'Five 07',
                                    "icon": 'monument'
                                }
                            }
    return render_template('index.html', data=data)