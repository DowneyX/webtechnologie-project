from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, FloatField,
                                  RadioField, SelectField,
                                  TextAreaField, SubmitField)
from wtforms.validators import DataRequired 

class Create_bungalow_form(FlaskForm):
    title = StringField("Title.", validators=[DataRequired()])
    description =  StringField("Description.", validators=[DataRequired()])
    price = FloatField("Price.", validators=[DataRequired()])
    max_p = RadioField('Max number of people', choices=[(2,'num_2'),(4,'num_4'),(8,'num_8')], validators=[DataRequired()],coerce=int)
    
class Create_Reservation_form(FlaskForm):
    begin_date = StringField("begin date", validators=[DataRequired()])
    end_date = StringField("end date", validators=[DataRequired()])
    submit = SubmitField("submit")