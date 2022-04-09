from datetime import datetime
from flask import Blueprint, redirect, render_template, url_for
from flask_login import current_user, login_required
from ..forms import Create_bungalow_form, Create_Reservation_form
from ..models import Bungalow, Reservation
from .. import db

views = Blueprint('views', __name__)

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
        reservation_obj = Reservation()
        reservation_obj.bungalow = bungalow_obj.uuid
        reservation_obj.user = None
        reservation_obj.start_date = form.start_date
        reservation_obj.end_date = form.end_date
        reservation_obj.total = bungalow_obj.price

        # add to database 

        # db.session.add(reservation_obj)
        # db.session.commit()
        # return redirect(url_for('<url>'))

    return render_template('bungalow.html', bungalow_obj = bungalow_obj, form = form , user = current_user)

@login_required
@views.route("/bungalows/create", methods = ['GET', 'POST'])
def create_bungalow():
    form = Create_bungalow_form()

    #form submitted
    if form.validate_on_submit():
        bungalow_obj = Bungalow()
        bungalow_obj.title = form.title.data
        bungalow_obj.description = form.description.data
        bungalow_obj.price = form.price.data
        bungalow_obj.max_p = form.max_p.data
        bungalow_obj.img_b64 = 'uploads/bungalow_id_1.jpg'

        # add to database 
        db.session.add(bungalow_obj)
        db.session.commit()

        return redirect(url_for('views.bungalow',bungalow_id = bungalow_obj.uuid ))

    return render_template('bungalow_create.html', form = form , user = current_user)

@login_required
@views.route("/bungalows/update/<int:bungalow_id>", methods = ['GET', 'POST'])
def update_bungalow(bungalow_id):
    form = Create_bungalow_form()
    bungalow_obj = Bungalow().query.get_or_404(bungalow_id)

    #form submitted
    if form.validate_on_submit():
        bungalow_obj.title = form.title.data
        bungalow_obj.description = form.description.data
        bungalow_obj.price = form.price.data
        bungalow_obj.max_p = form.max_p.data
        bungalow_obj.img_b64 = 'uploads/bungalow_id_1.jpg'
        bungalow_obj.updated_at = datetime.now()

        #add to database
        db.session.add(bungalow_obj)
        db.session.commit()
        return redirect(url_for('views.bungalow',bungalow_id = bungalow_obj.uuid, user = current_user ))

    form.title.data = bungalow_obj.title
    form.description.data = bungalow_obj.description
    form.price.data = bungalow_obj.price
    form.max_p.data = bungalow_obj.max_p

    return render_template('bungalow_update.html', form = form, user = current_user)

@login_required
@views.route('/account')
def account():
    return render_template('account.html', user = current_user)

@login_required
@views.route('/reservations')
def reservations():
    return render_template('reservations.html', user = current_user)