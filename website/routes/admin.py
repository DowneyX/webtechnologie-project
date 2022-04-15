from flask import Blueprint, flash, redirect, render_template, url_for
from datetime import date, datetime
from flask_login import current_user, login_required
from ..forms import Create_bungalow_form, Update_reservation_form
from ..models import Bungalow, Reservation, User
from .. import db

admin = Blueprint('admin', __name__)

#landing page for admin dashboard
@login_required
@admin.route("/")
def admin_dashboard():
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))

    return render_template('admin/admin.html', current_user = current_user)


###############
# read routes #
###############

@login_required
@admin.route("bungalow-overview")
def overview_bungalows():

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))

    bungalows_obj = Bungalow().query.all()

    return render_template('admin/bungalow_overview.html', bungalows_obj = bungalows_obj, current_user = current_user)

@login_required
@admin.route("user-overview")
def overview_users():

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))

    users_obj = User().query.all()

    return render_template('admin/user_overview.html', users_obj = users_obj, current_user = current_user)

@login_required
@admin.route("reservation-overview")
def overview_reservations():

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))

    reservations_obj = Reservation().query.all()

    return render_template('admin/reservation_overview.html', reservations_obj = reservations_obj, current_user = current_user)


#################
# create routes #
#################

@login_required
@admin.route("bungalow-create", methods = ['GET', 'POST'])
def create_bungalow():

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))
    
    form = Create_bungalow_form()

    #form submitted
    if form.validate_on_submit():

        # insert data
        bungalow_obj = Bungalow()
        bungalow_obj.title = form.title.data
        bungalow_obj.description = form.description.data
        bungalow_obj.price = form.price.data
        bungalow_obj.max_p = form.max_p.data
        bungalow_obj.img_b64 = 'uploads/bungalow_id_1.jpg'

        # add to database 
        db.session.add(bungalow_obj)
        db.session.commit()

        flash("bungalow has been successfully added")
        return redirect(url_for('views.bungalow',bungalow_id = bungalow_obj.uuid ))

    return render_template('admin/bungalow_create.html', form = form , current_user = current_user)


#################
# update routes #
#################

@login_required
@admin.route("bungalows/update-reservation/<int:reservation_id>", methods = ['GET', 'POST'])
def update_reservation(reservation_id):

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))

    form = Update_reservation_form()
    reservation_obj = Reservation().query.get_or_404(reservation_id)
    bungalow_id = Bungalow().query.get(reservation_obj.bungalow).uuid

    #form submitted
    if form.validate_on_submit():

        #check if selected date is in the past
        if form.start_date.data < date.today():
            flash('cannot make reservations on dates that have already passed')
            return redirect(url_for('views.update_reservation', reservation_id = reservation_id))
        
        #check if selected start_date is not overlapping with another reservation
        if db.session.query(Reservation).filter((Reservation.start_date <= form.end_date.data) & (Reservation.start_date >= form.start_date.data) & (Reservation.bungalow == bungalow_id) & (Reservation.uuid != reservation_id)).first() :
            flash('sorry that week has already been reserved')
            return redirect(url_for('views.update_reservation', reservation_id = reservation_id))

        #check if selected end_date is not overlapping with another reservation
        if db.session.query(Reservation).filter((Reservation.end_date <= form.end_date.data) & (Reservation.end_date >= form.start_date.data) & (Reservation.bungalow == bungalow_id) & (Reservation.uuid != reservation_id)).first():
            flash('sorry that week has already been reserved')
            return redirect(url_for('views.update_reservation', reservation_id = reservation_id))

        # insert data
        reservation_obj.start_date = form.start_date.data
        reservation_obj.end_date = form.end_date.data
        reservation_obj.total = form.total.data
        reservation_obj.updated_at = datetime.now()

        # add to database 
        db.session.add(reservation_obj)
        db.session.commit()

        flash("reservation updated succesfully")
        return redirect(url_for('admin.overview_reservations'))

    #set form values
    form.start_date.data = reservation_obj.start_date
    form.end_date.data = reservation_obj.end_date
    form.total.data = reservation_obj.total

    return render_template('admin/reservation_update.html', current_user = current_user, form = form)

@login_required
@admin.route("bungalow-update/<int:bungalow_id>", methods = ['GET', 'POST'])
def update_bungalow(bungalow_id):

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))

    form = Create_bungalow_form()
    bungalow_obj = Bungalow().query.get_or_404(bungalow_id)

    #form submitted
    if form.validate_on_submit():

        # insert data
        bungalow_obj.title = form.title.data
        bungalow_obj.description = form.description.data
        bungalow_obj.price = form.price.data
        bungalow_obj.max_p = form.max_p.data
        bungalow_obj.img_b64 = 'uploads/bungalow_id_1.jpg'
        bungalow_obj.updated_at = datetime.now()

        #add to database
        db.session.add(bungalow_obj)
        db.session.commit()

        flash("bungalow has been successfully updated")
        return redirect(url_for('views.bungalow',bungalow_id = bungalow_obj.uuid, current_user = current_user ))

    #set form values
    form.title.data = bungalow_obj.title
    form.description.data = bungalow_obj.description
    form.price.data = bungalow_obj.price
    form.max_p.data = bungalow_obj.max_p

    return render_template('admin/bungalow_update.html', form = form, current_user = current_user)


#################
# delete routes #
#################

@login_required
@admin.route("/user-delete/<int:user_id>")
def delete_user(user_id):

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))
    
    user_obj = User().query.get_or_404(user_id)

    if user_obj.role == 'admin':
        flash("cannot delete admin accounts change this user's role to 'user' first")
        return redirect(url_for('admin.overview_users'))


    db.session.delete(user_obj)
    db.session.commit()

    flash("user has been succesfully deleted")
    return redirect(url_for('admin.overview_users'))
    
@login_required
@admin.route("/bungalow-delete/<int:bungalow_id>")
def delete_bungalow(bungalow_id):

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))

    bungalow_obj = Bungalow().query.get_or_404(bungalow_id)
    db.session.delete(bungalow_obj)
    db.session.commit()

    flash("bungalow has been succesfully deleted")
    return redirect(url_for('admin.overview_bungalows'))

@login_required
@admin.route("/reservation-delete/<int:reservation_id>")
def delete_reservation(reservation_id):

    # check if user is admin
    if current_user.role != 'admin':
        flash("only admin accounts can acces this page")
        return redirect(url_for('views.home'))
    
    reservation_obj = Reservation().query.get_or_404(reservation_id)
    db.session.delete(reservation_obj)
    db.session.commit()

    flash("reservation has been succesfully deleted")
    return redirect(url_for('admin.overview_bungalows'))