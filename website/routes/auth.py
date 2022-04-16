# auth.py
from datetime import datetime
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required, current_user
from ..forms import Create_user_form, Login_user_form, Update_password_form, Update_user_form
from ..models import User
from .. import db

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    
    # check if user is already logged in
    if current_user.is_authenticated:
        flash('U bent al ingelogd.')
        redirect(url_for('views.home'))

    form = Login_user_form()

    # form submited
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not (User.query.filter_by(email=form.email.data).first()) or not check_password_hash(user.password, form.password.data):
            flash('Controleer uw login gegevens en probeer het opnieuw.')
            return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

        # # if the above check passes, then we know the user has the right credentials

        login_user(user)

        flash("Login succes.")
        return redirect(url_for('views.home'))

    return render_template('auth/login.html',form = form)

@auth.route('/sign-up',methods=['GET', 'POST'])
def signup():
    # check if user is already logged in
    if current_user.is_authenticated:
        flash('U bent al ingelogd.')
        redirect(url_for('views.home'))
    
    form = Create_user_form()
    
    #form submitted
    if form.validate_on_submit():
        
        # check if email is already in our database
        if User.query.filter_by(email=form.email.data).first():
            flash('Dit E-mail adres is al in gebruik.')
            return redirect(url_for('auth.signup'))

        # check if passwords match
        if form.password1.data != form.password2.data:
            flash('De wachtwoorden komen niet overeen.')
            return redirect(url_for('auth.signup'))

        #insert form data
        new_user = User()
        new_user.first_name = form.first_name.data
        new_user.last_name = form.last_name.data
        new_user.email = form.email.data
        new_user.phone_nr = form.phone_nr.data
        new_user.password = generate_password_hash(form.password1.data)

        #add to database
        db.session.add(new_user)
        db.session.commit()

        flash("Account aangemaakt.")
        return redirect(url_for('auth.login'))

    return render_template('auth/sign_up.html', form = form)

@login_required
@auth.route('/logout')
def logout():
    flash("Gebruiker uitgelogd")
    logout_user()
    return redirect(url_for('views.home'))

@login_required
@auth.route('/account')
def account():
    return render_template('auth/account.html', current_user = current_user)

@login_required
@auth.route('/password-update', methods = ['GET', 'POST'])
def update_password():
    form = Update_password_form()
    
    if form.validate_on_submit():
        user = User().query.get(current_user.uuid)
        # check if passwords match
        if form.password1.data != form.password2.data:
            flash('De wachtwoorden komen niet overeen.')
            return redirect(url_for('auth.signup'))

        #check if password is correct
        if not check_password_hash(current_user.password, form.current_password.data):
            flash('Controleer uw login gegevens en probeer het opnieuw.')
            return redirect(url_for('auth.login'))


        #insert data
        user.password = generate_password_hash(form.password1.data)
        user.updated_at = datetime.now

        # add to database
        db.session.add(user)
        db.session.commit()

        flash('Wachtwoord aangepast.')
        return redirect(url_for('auth.account'))

    return render_template('auth/password_update.html', form = form, current_user = current_user)

@login_required
@auth.route('/account-update', methods = ['GET', 'POST'])
def update_account():
    form = Update_user_form()
    
    if form.validate_on_submit():
        user = User().query.get(current_user.uuid)

        # check if email is already in our database
        if User.query.filter((User.email == form.email.data) & (User.uuid != current_user.uuid)).first():
            flash('Dit E-mail adres is al in gebruik.')
            return redirect(url_for('auth.update_account'))

        #insert data
        user.first_name = form.first_name.data
        user.last_name = form.last_name.data
        user.email = form.email.data
        user.phone_nr = form.phone_nr.data
        user.updated_at = datetime.now()

        # add to database
        db.session.add(user)
        db.session.commit()

        flash('Account aangepast.')
        return redirect(url_for('auth.account'))
    
    # setting form values
    form.first_name.data = current_user.first_name
    form.last_name.data = current_user.last_name
    form.email.data = current_user.email
    form.phone_nr.data = current_user.phone_nr

    return render_template('auth/account_update.html', form = form, current_user = current_user)

