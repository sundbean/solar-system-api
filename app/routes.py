from app import db
from app.models.planet import Planet
from flask import Blueprint, make_response, request, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST", "GET"])
def handle_planet():

    if request.method == "POST":
    
        request_body = request.get_json()

        new_planet = Planet(name=request_body['name'], description=request_body['description'], size=request_body['size'])

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
                "size": planet.size
            })

            return jsonify(planets_response)