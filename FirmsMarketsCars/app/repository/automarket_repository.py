from app import app, db, db_models

def create(automarket_data):
    firma = db_models.Firma.query.get(automarket_data.firma_id)
    print(firma)
    automarket = db_models.AutoMarket(name=automarket_data.name, owner=firma)
    db.session.add(automarket)
    db.session.commit()

    return f'automarket {automarket_data.name} created'


def get_all():
    automarkets_list = []

    for automarket in db_models.AutoMarket.query.all():
        automarkets_list.append(
            {   
                'id': automarket.id,
                'name': automarket.name,
                'firma_id': automarket.firma_id
            }
        )

    return automarkets_list


def delete_by_id(automarket_id: int):
    automarket = db_models.AutoMarket.query.filter_by(id=automarket_id).delete()
    db.session.commit()

    return f'automarket with id {automarket_id} deleted'


def update(automarket_data, automarket_id: int):
    # user = db_models.Users.query.filter_by(id=user_id)
    automarket = db.session.query(db_models.AutoMarket).get(automarket_id)
    automarket.name = automarket_data.name
    automarket.firma_id = automarket_data.firma_id
    db.session.commit()
    