from app import db

class Planet(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String)
    description = db.Column(db.String)
    day_length = db.Column(db.Float)
    year_length = db.Column(db.Float)
    average_temp = db.Column(db.Float)
    size = db.Column(db.Float)