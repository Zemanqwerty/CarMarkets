from app import app, db, db_models

def create(user_data):
    user = db_models.Users(email=user_data.email, nickname=user_data.nickname, password=user_data.password)
    db.session.add(user)
    db.session.commit()

    return f'user {user_data.nickname} created'


def get_all():
    users = []

    for user in db_models.Users.query.all():
        users.append(
            {   
                'id': user.id,
                'email': user.email,
                'nickname': user.nickname,
                'password': user.password,
                'date_reg': user.date_reg
            }
        )

    return users


def delete_by_id(user_id: int):
    user = db_models.Users.query.filter_by(id=user_id).delete()
    db.session.commit()

    return f'user with id {user_id} deleted'


def update(user_data, user_id):
    # user = db_models.Users.query.filter_by(id=user_id)
    user = db.session.query(db_models.Users).get(user_id)
    user.email = user_data.email
    user.nickname = user_data.nickname
    user.password = user_data.password
    db.session.commit()
    