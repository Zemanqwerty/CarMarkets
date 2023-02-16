from flask import request, jsonify
from app import db, db_models
from ..repository import firmas_repository
import hashlib

def create_firma(firma_data):
    try:
        firmas_repository.create(firma_data=firma_data)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def get_all_firms(request: request):
    try:
        return jsonify(firmas_repository.get_all())
    except Exception as e:
        return jsonify({'status': 500})


# def delete_by_id(firma_id: int):
#     try:
#         firmas_repository.delete_by_id(firma_id=firma_id)
#         return jsonify({'status': 200})
#     except Exception as e:
#         return jsonify({'status': 500})


# def update(firma_data, firma_id: int):
#     try:
#         firmas_repository.update(firma_data=firma_data, firma_id=firma_id)
#         return jsonify({'status': 200})
#     except Exception as e:
#         return jsonify({'status': 500})