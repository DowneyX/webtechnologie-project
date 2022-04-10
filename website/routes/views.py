from datetime import datetime
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required
from psutil import users
from ..forms import Create_bungalow_form, Create_Reservation_form
from ..models import Bungalow, Reservation, User
from .. import db

views = Blueprint('views', __name__)

@login_required
@views.route('/account')
def account():
    return render_template('account.html', user = current_user)

@views.route('/bungalows')
@views.route('/')
def home():
    bungalows_obj = Bungalow().query.all()
    return render_template('bungalows.html', bungalows_obj = bungalows_obj , user = current_user)

@views.route("bungalows/bungalow/<int:bungalow_id>", methods = ['GET', 'POST'])
def bungalow(bungalow_id):
    form = Create_Reservation_form()
    bungalow_obj = Bungalow().query.get_or_404(bungalow_id)

    #form submitted
    if form.validate_on_submit():
        if not current_user.is_authenticated:
            return redirect(url_for('auth.login'))

        reservation_obj = Reservation()
        reservation_obj.bungalow = bungalow_obj.uuid
        reservation_obj.user = current_user.uuid 
        reservation_obj.start_date = form.start_date.data
        reservation_obj.end_date = form.end_date.data
        reservation_obj.total = bungalow_obj.price

        # add to database 
        db.session.add(reservation_obj)
        db.session.commit()
        return redirect(url_for('views.reservations'))

    return render_template('bungalow.html', bungalow_obj = bungalow_obj, form = form , user = current_user)

@login_required
@views.route('/reservations')
def reservations():
    join = db.session.query(Reservation, Bungalow).join(Bungalow).filter(Reservation.user == current_user.uuid).all()

    return render_template('reservations.html',joinlist = join, user = current_user)