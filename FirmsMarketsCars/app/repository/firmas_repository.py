from app import app, db, db_models

def create(firma_data):
    firma = db_models.Firma(name=firma_data.name)
    db.session.add(firma)
    db.session.commit()

    return f'firma {firma_data.name} created'


def get_all():
    firmas_list = []

    for firma in db_models.Firma.query.all():
        firmas_list.append(
            {   
                'id': firma.id,
                'name': firma.name,
            }
        )

    return firmas_list


def delete_by_id(firma_id: int):
    firma = db_models.Firma.query.filter_by(id=firma_id).delete()
    db.session.commit()

    return f'firma with id {firma_id} deleted'


def update(firma_data, firma_id: int):
    # user = db_models.Users.query.filter_by(id=user_id)
    firma = db.session.query(db_models.Firma).get(firma_id)
    firma.name = firma_data.name
    db.session.commit()
    