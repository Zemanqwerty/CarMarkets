from flask import request, jsonify
from app import db, db_models
from ..repository import cars_repository

def create_car(car_data):
    try:
        cars_repository.create(car_data=car_data)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def get_all_cars(request: request):
    try:
        return jsonify(cars_repository.get_all())
    except Exception as e:
        return jsonify({'status': 500})


def delete_by_id(car_id: int):
    try:
        cars_repository.delete_by_id(car_id=car_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def update(car_data, car_id: int):
    try:
        cars_repository.update(car_data=car_data, car_id=car_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})