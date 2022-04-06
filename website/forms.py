from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, FloatField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField)
from wtforms.validators import DataRequired 

class bungalow_form(FlaskForm):
    title = StringField("title.", validators=[DataRequired()])
    description =  StringField("Description.", validators=[DataRequired()])
    price = FloatField("Price.", validators=[DataRequired()])
    max_p = RadioField('max number of people', choices=[(2,'num_2'),(4,'num_4'),(8,'num_8')], validators=[DataRequired()],coerce=int)
    
