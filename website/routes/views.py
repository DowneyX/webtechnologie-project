from flask import Blueprint, render_template, request
from ..models import Bungalows

views = Blueprint('views', __name__)

@views.route('/bungalows')
@views.route('/')
def home():
    bungalows = Bungalows().query.all()
    return render_template('bungalows.html', bungalows = bungalows)
 