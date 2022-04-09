import datetime
import uuid

from flask_login import UserMixin
from . import db
from sqlalchemy.dialects.postgresql import UUID
from flask_login import UserMixin
import uuid


class Bungalow(db.Model):
    __tablename__ = 'bungalows'
    uuid = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    title = db.Column(db.String(50), nullable=False, unique=True)
    description = db.Column(db.Text(), nullable=True)
    min_p = db.Column(db.Integer(), nullable=False)
    max_p = db.Column(db.Integer(), nullable=False)
    img_b64 = db.Column(db.String(100), nullable=False, unique=True)
    price = db.Column(db.Float(), nullable=False)
    reservations = db.relationship('Reservation', backref='Bungalow', lazy=True)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)


class User(UserMixin, db.Model):
    __tablename__ = 'users'
    uuid = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    first_name = db.Column(db.String(1000))
    last_name = db.Column(db.String(1000))
    phone_nr = db.Column(db.String(1000))
    role = db.Column(db.String(16), nullable=False, default='user')
    reservations = db.relationship('Reservation', backref='User', lazy=True)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)

    def __init__(self, email, password, fname, lname, phonenr, role):
        self.uuid = uuid.uuid4
        self.email = email
        self.first_name = fname
        self.last_name = lname
        self.phone_nr = phonenr
        self.role = role
        self.password = password
        self.created_at = datetime.datetime.now()


class Reservation(db.Model):
    __tablename__ = 'reservations'
    uuid = db.Column(db.String, primary_key=True, nullable=False, unique=True)
    bungalow = db.Column(db.String(), db.ForeignKey('bungalows.uuid'))
    user = db.Column(db.String(), db.ForeignKey('users.uuid'))
    start_date = db.Column(db.Date(), nullable=False)
    end_date = db.Column(db.Date(), nullable=False)
    total = db.Column(db.Float(), nullable=False)
    created_at = db.Column(db.Date(), nullable=False)
    updated_at = db.Column(db.Date(), nullable=True)
    deleted_at = db.Column(db.Date(), nullable=True)

    def __init__(self, bungalow, user, start, end, total):
        self.uuid = uuid.uuid4
        self.bungalow = bungalow
        self.user = user
        self.start_date = start
        self.end_date = end
        self.total = total
        self.created_at = datetime.datetime.now()
