from flask import Blueprint, render_template, request
from ..models import Bungalow

views = Blueprint('views', __name__)


@views.route('/bungalows')
@views.route('/')
def home():
    bungalows = Bungalow().query.all()
    return render_template('bungalows.html', bungalows=bungalows)


@views.route('bungalows/bungalow/<int:bungalow_id>')
def bungalow(bungalow_id):
    bungalow = Bungalow().query.get_or_404(bungalow_id)
    return render_template('bungalow.html', bungalow=bungalow)
