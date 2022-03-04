from flask import Blueprint, render_template, request

auth = Blueprint('auth', __name__)

@auth.route('/sign-in', methods=['GET', 'POST'])
def login():
    return "<p>sign-in</p>"


@auth.route('/sign-out')
def logout():
    return "<p>logout</p>"


@auth.route('/sign-up', methods=['GET', 'POST'])
def sign_up():
    return "<p>sign-up</p>"
 