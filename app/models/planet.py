from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    day_length_in_hours = db.Column(db.Float)
    year_length_in_earth_days = db.Column(db.Float)
    average_temp = db.Column(db.Float)
    radius_in_miles = db.Column(db.Float)