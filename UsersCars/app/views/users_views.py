from app import app
from flask import request
from ..service import user_service
from ..models import CreateUserBodyModel, UpdateUserBodyModel
from flask_pydantic import validate


@app.route('/users/create/', methods=['POST'])
@validate()
def create(body: CreateUserBodyModel):
    return user_service.create_user(user_data=body)


@app.route('/users/all/', methods=['GET'])
def get_all():
    return user_service.get_all_users(request=request)


@app.route('/users/delete/<user_id>/', methods=['DELETE'])
@validate()
def delete_by_id(user_id: int):
    return user_service.delete_by_id(user_id=user_id)


@app.route('/users/<user_id>/update/', methods=['PUT'])
@validate()
def update(body: UpdateUserBodyModel, user_id: int):
    return user_service.update(user_data=body, user_id = user_id)