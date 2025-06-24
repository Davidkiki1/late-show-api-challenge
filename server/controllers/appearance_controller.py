from flask import Blueprint, request, jsonify
from flask_jwt_extended import jwt_required
from server.models.appearance import Appearance
from server.app import db

appearance_bp = Blueprint('appearance', __name__)

@appearance_bp.route('/appearances', methods=["POST"])
@jwt_required()
def create_appearance():
    data = request.get_json()

    try:
        appearance = Appearance(
            rating=data['rating'],
            guest_id=data['guest_id'],
            episode_id=data['episode_id']
        )
        db.session.add(appearance)
        db.session.commit()

        return jsonify(message="Appearance created successfully"), 201

    except Exception as e:
        return jsonify(error=str(e)), 400
