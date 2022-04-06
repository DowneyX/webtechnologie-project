from . import db
from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin
import uuid

class Bungalow(db.Model):
    __tablename__ = 'bungalows'
    uuid = db.Column(db.Integer(), primary_key=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=True)
    max_p = db.Column(db.Integer(), nullable=False)
    img_b64 = db.Column(db.String(100), nullable=False, unique=False)
    price = db.Column(db.Float(), nullable=False)
    reservations = db.relationship('Reservation', backref='bungalows')
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=False)
    deleted_at = db.Column(db.Date(), nullable=True)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uuid = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(32), nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.Text(), nullable=False)
    role = db.Column(db.String(16), nullable=False, default='user')
    reservations = db.relationship('Reservation', backref='users')
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=False)
    deleted_at = db.Column(db.Date(), nullable=True)


class Reservation(db.Model):
    __tablename__ = 'reservations'
    uuid = db.Column(db.Integer(), primary_key=True)
    bungalow = db.Column(db.Integer(), db.ForeignKey('bungalows.uuid'))
    user = db.Column(db.Integer(), db.ForeignKey('users.uuid'))
    begin_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    total = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=False)
    deleted_at = db.Column(db.Date(), nullable=True)
