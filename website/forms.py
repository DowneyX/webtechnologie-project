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
    submit = SubmitField("Submit")
    
class Create_Reservation_form(FlaskForm):
    start_date = StringField("Start date", validators=[DataRequired()])
    end_date = StringField("End date", validators=[DataRequired()])
    submit = SubmitField("Submit") 

class Create_user_form(FlaskForm):
    first_name = StringField("first name", validators=[DataRequired()])
    last_name = StringField("last name", validators=[DataRequired()])
    email = StringField("e-mail", validators=[DataRequired()])
    phone_nr = StringField("phone number", validators=[DataRequired()])
    password1 = StringField("password", validators=[DataRequired()])
    password2 = StringField("password again", validators=[DataRequired()])
    submit = SubmitField("Submit") 

class Login_user_form(FlaskForm):
    email = StringField("e-mail", validators=[DataRequired()])
    password = StringField("password", validators=[DataRequired()])
    remember = BooleanField("remember")
    submit = SubmitField("Submit") 