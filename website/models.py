from flask_login import UserMixin

from . import db


class Bungalow(db.Model):
    __tablename__ = 'bungalows'
    uuid = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=True)
    min_p = db.Column(db.Integer(), nullable=False)
    max_p = db.Column(db.Integer(), nullable=False)
    img_b64 = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    reservations = db.relationship('Reservations', backref='bungalows')
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=False)
    deleted_at = db.Column(db.Date(), nullable=False)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uuid = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    role = db.Column(db.String(16), nullable=False, default='user')
    reservations = db.relationship('Reservations', backref='users')
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=False)
    deleted_at = db.Column(db.Date(), nullable=False)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))


class Reservation(db.Model):
    __tablename__ = 'reservations'
    uuid = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    bungalow = db.Column(db.Integer(), db.ForeignKey('bungalows.uuid'))
    user = db.Column(db.Integer(), db.ForeignKey('users.uuid'))
    begin_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    total = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=False)
    deleted_at = db.Column(db.Date(), nullable=False)
