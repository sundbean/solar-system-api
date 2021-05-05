from app import db
from app.models.planet import Planet
from flask import Blueprint, make_response, request, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def handle_planets():

    if request.method == "POST":
    
        request_body = request.get_json()

        new_planet = Planet(name=request_body['name'], 
                            description=request_body['description'],
                            radius_in_miles=request_body['radius_in_miles'],
                            day_length_in_hours=request_body['day_length_in_hours'],
                            year_length_in_earth_days=request_body['year_length_in_earth_days'],
                            average_temp=request_body['average_temp'])

        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} has been created", 201)

    elif request.method == "GET":

        planets = Planet.query.all()
        planets_response = []

        for planet in planets:
            planets_response.append({
                "id": planet.id,
                "name": planet.name,
                "description": planet.description,
                "radius_in_miles": planet.radius_in_miles,
                "day_length_in_hours": planet.day_length_in_hours,
                "year_length_in_earth_days": planet.year_length_in_earth_days,
                "average_temp": planet.average_temp
            })

        return jsonify(planets_response)

@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):

    planet = Planet.query.get(planet_id)

    if request.method == "GET":

        return {
            "id": planet.id,
            "name": planet.name,
            "description": planet.description,
            "radius_in_miles": planet.radius_in_miles,
            "day_length_in_hours": planet.day_length_in_hours,
            "year_length_in_earth_days": planet.year_length_in_earth_days,
            "average_temp": planet.average_temp
        }