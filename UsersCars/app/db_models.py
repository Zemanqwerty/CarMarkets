from app import db
import datetime

class Users(db.Model):
    __tablename__ = 'users'

    def __init__(self, nickname, email, password) -> None:
        self.nickname = nickname
        self.email = email
        self.password = password

    id = db.Column(db.Integer, primary_key=True)
    nickname = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True)
    password = db.Column(db.String())
    date_reg = db.Column(db.DateTime, default=datetime.datetime.now())
    cars = db.relationship('Cars', backref = 'owner', lazy = 'dynamic')

    def __repr__(self) -> str:
        return f'USER - {self.nickname}'


class Cars(db.Model):
    __tablename__ = 'cars'

    # def __init__(self, name, number, users_id) -> None:
    #     self.name = name
    #     self.number = number
    #     self.users_id = users_id

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    number = db.Column(db.String(), unique=True)
    users_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self) -> str:
        return f'CAR - {self.number}'
