from app import app, db, db_models

def create(car_data):
    auto_market = db_models.AutoMarket.query.get(car_data.auto_market_id)
    print(auto_market)
    car = db_models.Cars(name=car_data.name, number=car_data.number, owner=auto_market)
    db.session.add(car)
    db.session.commit()

    return f'car {car.number} created'


def get_all():
    cars_list = []

    for car in db_models.Cars.query.all():
        cars_list.append(
            {   
                'id': car.id,
                'name': car.name,
                'number': car.number,
                'auto_market_id': car.auto_market_id
            }
        )

    return cars_list


def delete_by_id(car_id: int):
    car = db_models.Cars.query.filter_by(id=car_id).delete()
    db.session.commit()

    return f'car with id {car_id} deleted'


def update(car_data, car_id: int):
    # user = db_models.Users.query.filter_by(id=user_id)
    car = db.session.query(db_models.Cars).get(car_id)
    car.name = car_data.name
    car.number = car_data.number
    car.auto_market_id = car_data.auto_market_id
    db.session.commit()
    