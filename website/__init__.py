from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
DB_NAME = 'database.db'


def create_app():
    app = Flask(__name__)
    upload_folder = 'static/uploads'

    # WHEN IN PRODUCTION NEVER SHARE THIS KEY AND CHANGE IT TO SOMETHING THAT MAKES MORE SENSE
    app.config['SECRET_KEY'] = 'ThisIsSecret'
    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{DB_NAME}"
    app.config['UPLOAD_FOLDER'] = upload_folder
    db.init_app(app)

    from .routes.views import views
    from .routes.auth import auth

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/auth')

    from .models import User, Bungalow, Reservation

    db.create_all(app=app)

    return app
