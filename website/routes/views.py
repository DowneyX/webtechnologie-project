from crypt import methods
from flask import Blueprint, render_template, request
from ..forms import bungalow_form
from ..models import Bungalows
from .. import db

views = Blueprint('views', __name__)


@views.route('/bungalows')
@views.route('/')
def home():
    bungalows = Bungalows().query.all()
    return render_template('bungalows.html', bungalows=bungalows)


@views.route('bungalows/bungalow/<int:bungalow_id>')
def bungalow(bungalow_id):
    bungalow_obj = Bungalows().query.get_or_404(bungalow_id)
    return render_template('bungalow.html', bungalow_obj=bungalow_obj)

@views.route("/bungalows/create", methods= ['GET', 'POST'])
def create_bungalow():
    form = bungalow_form()
    if form.validate_on_submit():
        bungalow_obj = Bungalows()
        bungalow_obj.name = form.name.data
        bungalow_obj.Description = form.description.data
        bungalow_obj.price = form.price.data
        bungalow_obj.num_people = form.num_people.data
        bungalow_obj.image = 'uploads/bungalow_id_1.jpg'

        db.session.add(bungalow_obj)
        db.session.commit()

    return render_template('bungalow_create.html', form=form)


@views.route("/bungalows/update/<int:bungalow_id>", methods= ['GET', 'POST'])
def update_bungalow(bungalow_id):
    form = bungalow_form()
    bungalow_obj = Bungalows().query.get_or_404(bungalow_id)

    form.name.data = bungalow_obj.name
    form.description.data = bungalow_obj.Description
    form.price.data = bungalow_obj.price
    form.num_people.default = bungalow_obj.num_people

    return render_template('bungalow_update.html', form=form)