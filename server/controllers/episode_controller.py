from flask import Blueprint, jsonify, request
from flask_jwt_extended import jwt_required
from server.models.episode import Episode
from server.models.appearance import Appearance
from server.app import db

episode_bp = Blueprint('episode', __name__)

@episode_bp.route('/episodes', methods=["GET"])
def get_episodes():
    episodes = Episode.query.all()
    return jsonify([{
        "id": ep.id,
        "date": ep.date.isoformat(),
        "number": ep.number
    } for ep in episodes]), 200

@episode_bp.route('/episodes/<int:id>', methods=["GET"])
def get_episode(id):
    ep = Episode.query.get(id)
    if not ep:
        return jsonify(error="Episode not found"), 404

    appearances = [
        {
            "id": ap.id,
            "rating": ap.rating,
            "guest": ap.guest.name
        } for ap in ep.appearances
    ]

    return jsonify({
        "id": ep.id,
        "date": ep.date.isoformat(),
        "number": ep.number,
        "appearances": appearances
    }), 200

@episode_bp.route('/episodes/<int:id>', methods=["DELETE"])
@jwt_required()
def delete_episode(id):
    ep = Episode.query.get(id)
    if not ep:
        return jsonify(error="Episode not found"), 404

    db.session.delete(ep)
    db.session.commit()
    return jsonify(message="Episode deleted"), 200