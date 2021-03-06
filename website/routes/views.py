from datetime import date, datetime
from flask import Blueprint, flash, redirect, render_template, url_for
from flask_login import current_user, login_required
from ..forms import Date_form, Contact_form
from ..models import Bungalow, Reservation, Contact
from .. import db

views = Blueprint('views', __name__)

###############
# read routes #
###############

@views.route('/')
@views.route('/bungalows')
def home():
    bungalows_obj = Bungalow().query.all()
    return render_template('bungalows.html', bungalows_obj = bungalows_obj , current_user = current_user)

@login_required
@views.route('/reservations')
def reservations():
    join = db.session.query(Reservation, Bungalow).join(Bungalow).filter(Reservation.user == current_user.uuid).all()
    return render_template('reservations.html',joinlist = join, current_user = current_user)


#################
# create routes #
#################

@views.route("bungalows/bungalow/<int:bungalow_id>", methods = ['GET', 'POST'])
def bungalow(bungalow_id):
    form = Date_form()
    bungalow_obj = Bungalow().query.get_or_404(bungalow_id)

    #form submitted
    if form.validate_on_submit():
        #check if user is logged in
        if not current_user.is_authenticated:
            flash("U moet ingelogd zijn om een boeking te maken")
            return redirect(url_for('auth.login'))

        #check if selected date is in the past
        if form.start_date.data < date.today():
            flash('Kan geen boeking maken voor een datum die al is geweest.')
            return redirect(url_for('views.bungalow', bungalow_id=bungalow_id))

        #check if selected start_date is not overlapping with another reservation
        if db.session.query(Reservation).filter((Reservation.start_date <= form.end_date.data) & (Reservation.start_date >= form.start_date.data) & (Reservation.bungalow == bungalow_id)).first():
            flash('Sorry, deze datum is al geboekt.')
            return redirect(url_for('views.bungalow', bungalow_id=bungalow_id))

        #check if selected end_date is not overlapping with another reservation
        if db.session.query(Reservation).filter((Reservation.end_date <= form.end_date.data) & (Reservation.end_date >= form.start_date.data) & (Reservation.bungalow == bungalow_id)).first():
            flash('Sorry, deze datum is al geboekt.')
            return redirect(url_for('views.bungalow', bungalow_id=bungalow_id))
        
        # insert form data
        reservation_obj = Reservation()
        reservation_obj.bungalow = bungalow_obj.uuid
        reservation_obj.user = current_user.uuid 
        reservation_obj.start_date = form.start_date.data
        reservation_obj.end_date = form.end_date.data
        reservation_obj.total = bungalow_obj.price

        # add to database 
        db.session.add(reservation_obj)
        db.session.commit()

        flash("Boeking gemaakt.")
        return redirect(url_for('views.reservations'))

    return render_template('bungalow.html', bungalow_obj = bungalow_obj, form = form , current_user = current_user)

@views.route('/contact', methods = ['GET', 'POST'])
def contact():
    form = Contact_form()

    if form.validate_on_submit():
        contact_obj = Contact()

        #insert data
        contact_obj.email = form.email.data
        contact_obj.message = form.message.data

        #add to database
        db.session.add(contact_obj)
        db.session.commit()

        flash("Contact formulier verzonden.")
        return redirect(url_for('views.contact'))

    return render_template('contact.html',form = form , current_user = current_user)
#################
# update routes #
#################

@login_required
@views.route("bungalows/update-reservation/<int:reservation_id>", methods = ['GET', 'POST'])
def update_reservation(reservation_id):
    form = Date_form()
    reservation_obj = Reservation().query.get_or_404(reservation_id)
    bungalow_id = Bungalow().query.get(reservation_obj.bungalow).uuid

    # check if user owns the reservation
    if int(current_user.uuid) != int(reservation_obj.user):
            flash("U kunt niet op deze pagina komen met dit account.")
            return redirect(url_for('views.home'))

    #form submitted
    if form.validate_on_submit():

        #check if selected date is in the past
        if form.start_date.data < date.today():
            flash('Kan geen boeking maken voor een datum die al is geweest.')
            return redirect(url_for('views.update_reservation', reservation_id = reservation_id))
        
        #check if selected start_date is not overlapping with another reservation
        if db.session.query(Reservation).filter((Reservation.start_date <= form.end_date.data) & (Reservation.start_date >= form.start_date.data) & (Reservation.bungalow == bungalow_id) & (Reservation.uuid != reservation_id)).first() :
            flash('Sorry, deze datum is al geboekt.')
            return redirect(url_for('views.update_reservation', reservation_id = reservation_id))

        #check if selected end_date is not overlapping with another reservation
        if db.session.query(Reservation).filter((Reservation.end_date <= form.end_date.data) & (Reservation.end_date >= form.start_date.data) & (Reservation.bungalow == bungalow_id) & (Reservation.uuid != reservation_id)).first():
            flash('Sorry, deze datum is al geboekt.')
            return redirect(url_for('views.update_reservation', reservation_id = reservation_id))

        # insert form data
        reservation_obj.start_date = form.start_date.data
        reservation_obj.end_date = form.end_date.data
        reservation_obj.updated_at = datetime.now()

        # add to database 
        db.session.add(reservation_obj)
        db.session.commit()

        flash("Boeking aangepast")
        return redirect(url_for('views.reservations'))

    return render_template('reservation_update.html', current_user = current_user, form = form)

#################
# delete routes #
#################

@login_required
@views.route("bungalows/reservation-delete/<int:reservation_id>")
def delete_reservation(reservation_id):
    reservation_obj = Reservation().query.get_or_404(reservation_id)

    # check if user owns the reservation
    if int(current_user.uuid) != int(reservation_obj.user):
            flash("U kunt niet op deze pagina komen met dit account.")
            return redirect(url_for('views.home'))

    db.session.delete(reservation_obj)
    db.session.commit()

    flash("Boeking verwijderd.")
    return redirect(url_for('views.reservations'))