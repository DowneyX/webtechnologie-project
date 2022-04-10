# auth.py
from flask import Blueprint, render_template, redirect, url_for, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import login_user, logout_user, login_required
from ..forms import Create_user_form, Login_user_form
from ..models import User
from .. import db

auth = Blueprint('auth', __name__)

@auth.route('/login',methods=['GET','POST'])
def login():
    form = Login_user_form()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()

        # check if user actually exists
        # take the user supplied password, hash it, and compare it to the hashed password in database
        if not user or not check_password_hash(user.password, form.password.data):
            flash('Please check your login details and try again.')
            return redirect(url_for('auth.login'))  # if user doesn't exist or password is wrong, reload the page

        # # if the above check passes, then we know the user has the right credentials

        login_user(user)

        flash("login succesfull")
        return redirect(url_for('views.home'))

    return render_template('auth/login.html',form = form)

@auth.route('/signup',methods=['GET', 'POST'])
def signup():
    form = Create_user_form()

    if form.validate_on_submit():
        user_exists = User.query.filter_by(email=form.email.data).first()

        if user_exists:
            flash('Email address already exists')
            return redirect(url_for('auth.signup'))

        if form.password1.data != form.password2.data:
            flash('passwords do not match')
            return redirect(url_for('auth.signup'))

        new_user = User()
        new_user.first_name = form.first_name.data
        new_user.last_name = form.last_name.data
        new_user.email = form.email.data
        new_user.phone_nr = form.phone_nr.data
        new_user.password = generate_password_hash(form.password1.data)

        db.session.add(new_user)
        db.session.commit()
        return redirect(url_for('auth.login'))

    return render_template('auth/sign_up.html', form = form)


@auth.route('/logout')
@login_required
def logout():

    flash("user logged out")
    logout_user()
    return redirect(url_for('views.home'))