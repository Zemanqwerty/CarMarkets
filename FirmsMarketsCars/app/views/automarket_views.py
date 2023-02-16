from app import app
from flask import request
from ..service import automarket_service
from ..models import CreateAutoMarketBodyModel, UpdateAutoMarketBodyModel
from flask_pydantic import validate


@app.route('/automarket/create/', methods=['POST'])
@validate()
def create_automarket(body: CreateAutoMarketBodyModel):
    return automarket_service.create_automarket(automarket_data=body)


@app.route('/automarket/all/', methods=['GET'])
def get_all_automarkets():
    return automarket_service.get_all_automarkets(request=request)


@app.route('/automarket/delete/<automarket_id>/', methods=['DELETE'])
@validate()
def delete_automarket_by_id(automarket_id: int):
    return automarket_service.delete_by_id(automarket_id=automarket_id)


@app.route('/automarket/<automarket_id>/update/', methods=['PUT'])
@validate()
def update_automarket(body: UpdateAutoMarketBodyModel, automarket_id: int):
    return automarket_service.update(automarket_data=body, automarket_id=automarket_id)
