from . import db

class Bungalows(db.Model):
    __tablename__ = 'bungalows'
    id = db.Column(db.Integer(),primary_key=True, nullable=False, unique=True)
    name = db.Column(db.String(50), nullable=False, unique=True )
    Description = db.Column(db.Text(), nullable=True)
    num_people = db.Column(db.Integer(), nullable=False)
    image = db.Column(db.String(100), nullable=False, unique=True )
    price = db.Column(db.Float(), nullable=False)
    reservations = db.relationship('Reservations', backref='bungalows')

class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer(),primary_key=True, nullable=False, unique=True)
    username = db.Column(db.String(32) , nullable=False, unique=True )
    password = db.Column(db.Text() , nullable=False)
    role = db.Column(db.String(16) , nullable=False, default='user')
    reservations = db.relationship('Reservations', backref='users')

class Reservations(db.Model):
    __tablename__ = 'reservations'
    id = db.Column(db.Integer(),primary_key=True, nullable=False, unique=True)
    bunglalows = db.Column(db.Integer(), db.ForeignKey('bungalows.id'))
    user = db.Column(db.Integer(), db.ForeignKey('users.id'))
    beg_date = db.Column(db.Date(),nullable=False)
    end_date = db.Column(db.Date(),nullable=False)
    total = db.Column(db.Float(),nullable=False)