from flask import Blueprint, render_template, request

views = Blueprint('views', __name__)

@views.route('/bungalows')
@views.route('/')
def home():
    return render_template('bungalows.html')
 