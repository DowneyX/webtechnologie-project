from crypt import methods
from datetime import date, datetime
from flask import Blueprint, redirect, render_template, request, url_for
from ..forms import bungalow_form
from ..models import Bungalow
from .. import db

views = Blueprint('views', __name__)


@views.route('/bungalows')
@views.route('/')
def home():
    bungalows_obj = Bungalow().query.all()
    return render_template('bungalows.html', bungalows_obj=bungalows_obj)


@views.route('bungalows/bungalow/<int:bungalow_id>')
def bungalow(bungalow_id):
    bungalow_obj = Bungalow().query.get_or_404(bungalow_id)
    return render_template('bungalow.html', bungalow_obj=bungalow_obj)

@views.route("/bungalows/create", methods= ['GET', 'POST'])
def create_bungalow():
    form = bungalow_form()

    #form submitted
    if form.validate_on_submit():
        bungalow_obj = Bungalow()
        bungalow_obj.title = form.title.data
        bungalow_obj.description = form.description.data
        bungalow_obj.price = form.price.data
        bungalow_obj.max_p = form.max_p.data
        bungalow_obj.img_b64 = 'uploads/bungalow_id_1.jpg'
        bungalow_obj.created_at = datetime.now()
        bungalow_obj.updated_at = datetime.now()

        # add to database 
        db.session.add(bungalow_obj)
        db.session.commit()
        return redirect(url_for('views.bungalow',bungalow_id = bungalow_obj.uuid ))

    return render_template('bungalow_create.html', form=form)


@views.route("/bungalows/update/<int:bungalow_id>", methods= ['GET', 'POST'])
def update_bungalow(bungalow_id):
    form = bungalow_form()
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
        return redirect(url_for('views.bungalow',bungalow_id = bungalow_obj.uuid ))

    form.title.data = bungalow_obj.title
    form.description.data = bungalow_obj.description
    form.price.data = bungalow_obj.price
    form.max_p.data = bungalow_obj.max_p

    return render_template('bungalow_update.html', form=form)