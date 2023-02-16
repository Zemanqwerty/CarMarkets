from flask import request, jsonify
from app import db, db_models
from ..repository import automarket_repository

def create_automarket(automarket_data):
    try:
        automarket_repository.create(automarket_data=automarket_data)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def get_all_automarkets(request: request):
    try:
        return jsonify(automarket_repository.get_all())
    except Exception as e:
        return jsonify({'status': 500})


def delete_by_id(automarket_id: int):
    try:
        automarket_repository.delete_by_id(automarket_id=automarket_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def update(automarket_data, automarket_id: int):
    try:
        automarket_repository.update(automarket_data=automarket_data, automarket_id=automarket_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})