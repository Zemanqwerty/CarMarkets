from flask import request, jsonify
from app import db, db_models
from ..repository import users_repository
from ..security import security
import hashlib

def create_user(user_data):
    try:
        user_data.password = security.hashing_password(user_data.password)
        users_repository.create(user_data=user_data)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def get_all_users(request: request):
    try:
        users_list = users_repository.get_all()
        return jsonify(users_list)
    except Exception as e:
        return jsonify({'status': 500})


def delete_by_id(user_id: int):
    try:
        users_repository.delete_by_id(user_id=user_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def update(user_data, user_id):
    try:
        user_data.password = security.hashing_password(user_data.password)
        users_repository.update(user_data=user_data, user_id=user_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})