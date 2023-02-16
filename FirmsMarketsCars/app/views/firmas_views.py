from app import app
from flask import request
from ..service import firmas_service
from ..models import CreateFirmaBodyModel, UpdateFirmaBodyModel
from flask_pydantic import validate


@app.route('/firma/create/', methods=['POST'])
@validate()
def create_firma(body: CreateFirmaBodyModel):
    return firmas_service.create_firma(firma_data=body)


@app.route('/firma/all/', methods=['GET'])
def get_all_firms():
    return firmas_service.get_all_firms(request=request)


@app.route('/firma/delete/<firma_id>/', methods=['DELETE'])
@validate()
def delete_firma_by_id(firma_id: int):
    return firmas_service.delete_by_id(firma_id=firma_id)


@app.route('/firma/<firma_id>/update/', methods=['PUT'])
@validate()
def update_firma(body: UpdateFirmaBodyModel, firma_id: int):
    return firmas_service.update(firma_data=body, firma_id=firma_id)
