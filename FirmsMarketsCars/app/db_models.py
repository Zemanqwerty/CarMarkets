from app import db
import datetime

class Firma(db.Model):
    __tablename__ = 'firma'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(), unique=True)
    auto_markets = db.relationship('AutoMarket', backref = 'owner', lazy = 'dynamic')

    def __repr__(self) -> str:
        return f'FIRMA - {self.name}'


class AutoMarket(db.Model):
    __tablename__ = 'automarket'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    firma_id = db.Column(db.Integer, db.ForeignKey('firma.id'))
    cars = db.relationship('Cars', backref = 'owner', lazy = 'dynamic')

    def __repr__(self) -> str:
        return f'AUTOMARKET - {self.name}'


class Cars(db.Model):
    __tablename__ = 'cars'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    number = db.Column(db.String())
    auto_market_id = db.Column(db.Integer, db.ForeignKey('automarket.id'))

    def __repr__(self) -> str:
        return f'CAR - {self.number}'