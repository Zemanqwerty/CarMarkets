from app import app, db, db_models

def create(car_data):
    user = db_models.Users.query.get(car_data.users_id)
    print(user)
    car = db_models.Cars(name=car_data.name, number=car_data.number, owner=user)
    print(car)
    db.session.add(car)
    db.session.commit()

    return f'car {car_data.number} created'


def get_all():
    cars = []

    for car in db_models.Cars.query.all():
        cars.append(
            {   
                'id': car.id,
                'name': car.name,
                'number': car.number,
                'users_id': car.users_id,
            }
        )

    return cars


def delete_by_id(car_id: int):
    car = db_models.Cars.query.filter_by(id=car_id).delete()
    db.session.commit()

    return f'car with id {car_id} deleted'


def update(car_data, car_id):
    # user = db_models.Users.query.filter_by(id=user_id)
    car = db.session.query(db_models.Cars).get(car_id)
    user = db_models.Users.query.get(car_data.users_id)
    car.name = car_data.name
    car.number = car_data.number
    car.owner = user
    db.session.commit()
    