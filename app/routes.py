from app import db
from app.models.planet import Planet
from flask import Blueprint, make_response, request, jsonify

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["POST"])
def handle_planet():
    
    request_body = request.get_json()

    new_planet = Planet(name=request_body['name'], description=request_body['description'], size=request_body['size'])

    db.session.add(new_planet)
    db.session.commit()

    return make_response(f"Planet {new_planet.name} has been created", 201)


