from app import app
from flask import request
from ..service import car_service
from ..models import CreateCarBodyModel, UpdateCarBodyModel
from flask_pydantic import validate


@app.route('/cars/create/', methods=['POST'])
@validate()
def create_car(body: CreateCarBodyModel):
    return car_service.create_car(car_data=body)


@app.route('/cars/all/', methods=['GET'])
def get_all_cars():
    return car_service.get_all_cars(request=request)


@app.route('/cars/delete/<car_id>/', methods=['DELETE'])
@validate()
def delete_car_by_id(car_id: int):
    return car_service.delete_by_id(car_id=car_id)


@app.route('/cars/<car_id>/update/', methods=['PUT'])
@validate()
def update_car(body: UpdateCarBodyModel, car_id: int):
    return car_service.update(car_data=body, car_id = car_id)