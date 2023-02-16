from flask import request, jsonify
from app import db, db_models
from ..repository import cars_repository
from ..security import security
import hashlib
import requests
import json

def create_car(car_data):
    try:
        cars_list = requests.get('http://127.0.0.1:8000/cars/all', headers={'Accept': 'application/json'})
        cars_list_data = cars_list.json()
        for car in cars_list_data:
            if car_data.name == car['name'] and car_data.number == car['number']:
                cars_repository.create(car_data=car_data)
                return jsonify({'status': 200})
            else:
                return jsonify({'status': 400, 'message': f'car with name {car_data.name} and number {car_data.number} not found'})
    except Exception as e:
        return jsonify({'status': 500})


def get_all_cars(request: request):
    try:
        cars_list = cars_repository.get_all()
        return jsonify(cars_list)
    except Exception as e:
        return jsonify({'status': 500})


def delete_by_id(car_id: int):
    try:
        cars_repository.delete_by_id(car_id=car_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})


def update(car_data, car_id):
    try:
        cars_repository.update(car_data=car_data, car_id=car_id)
        return jsonify({'status': 200})
    except Exception as e:
        return jsonify({'status': 500})