from flask import Blueprint, redirect, render_template, url_for
import datetime
from flask_login import current_user, login_required

from website.routes.views import bungalow, reservations
from ..forms import Create_bungalow_form, Create_Reservation_form
from ..models import Bungalow, Reservation, User
from .. import db

admin = Blueprint('admin', __name__)

@login_required
@admin.route("/")
def admin_dashboard():
    if current_user.role != 'admin':
        return redirect(url_for('views.home'))

    return render_template('admin/admin.html', user = current_user)

@login_required
@admin.route("bungalowoverview")
def overview_bungalows():
    if current_user.role != 'admin':
        return redirect(url_for('views.home'))

    bungalows_obj = Bungalow().query.all()

    return render_template('admin/bungalow_overview.html', bungalows_obj = bungalows_obj, user = current_user)

@login_required
@admin.route("useroverview")
def overview_users():
    if current_user.role != 'admin':
        return redirect(url_for('views.home'))

    users_obj = User().query.all()

    return render_template('admin/user_overview.html', users_obj = users_obj, user = current_user)

@login_required
@admin.route("reservationoverview")
def overview_reservations():
    if current_user.role != 'admin':
        return redirect(url_for('views.home'))

    reservations_obj = Reservation().query.all()

    return render_template('admin/reservation_overview.html', reservations_obj = reservations_obj, user = current_user)

@login_required
@admin.route("bungalowcreate", methods = ['GET', 'POST'])
def create_bungalow():
    if current_user.role != 'admin':
        return redirect(url_for('views.home'))
    
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

    return render_template('admin/bungalow_create.html', form = form , user = current_user)

@login_required
@admin.route("bungalowupdate/<int:bungalow_id>", methods = ['GET', 'POST'])
def update_bungalow(bungalow_id):

    if current_user.role != 'admin':
        return redirect(url_for('views.home'))

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

    return render_template('admin/bungalow_update.html', form = form, user = current_user)

