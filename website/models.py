from datetime import datetime
from flask_login import UserMixin
from . import db

class Bungalow(db.Model):
    __tablename__ = 'bungalows'
    uuid = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=True)
    min_p = db.Column(db.Integer(), nullable=False, default=1)
    max_p = db.Column(db.Integer(), nullable=False)
    img_b64 = db.Column(db.String(100), nullable=False, unique=False)
    price = db.Column(db.Float(), nullable=False)
    reservations = db.relationship('Reservation', backref='Bungalow', lazy=True)
    created_at = db.Column(db.Date(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)

class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uuid = db.Column(db.Integer(), primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    phone_nr = db.Column(db.String(1000))
    role = db.Column(db.String(16), nullable=False, default='user')
    reservations = db.relationship('Reservation', backref='User', lazy=True)
    created_at = db.Column(db.Date(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)

    def get_id(self):
        return (self.uuid)

class Reservation(db.Model):
    __tablename__ = 'reservations'
    uuid = db.Column(db.Integer(), primary_key=True)
    bungalow = db.Column(db.String(), db.ForeignKey('bungalows.uuid'))
    user = db.Column(db.String(), db.ForeignKey('users.uuid'))
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    total = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False, default=datetime.now())
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)