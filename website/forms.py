import email
from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, FloatField,
                                  RadioField,
                                  TextAreaField, SubmitField,DateField, EmailField, PasswordField, IntegerField)
from wtforms.validators import DataRequired, Email, Length, EqualTo

class Create_bungalow_form(FlaskForm):
    title = StringField("Title.", validators=[DataRequired(), Length(2,50)])
    description =  TextAreaField("Description.", validators=[DataRequired(), Length(2,2000)])
    price = FloatField("Price.", validators=[DataRequired()])
    max_p = RadioField('Max number of people', choices=[(2,'num_2'),(4,'num_4'),(8,'num_8')], validators=[DataRequired()],coerce=int)
    submit = SubmitField("Submit")
    
class Date_form(FlaskForm):
    start_date = DateField("Start date", validators=[DataRequired()])
    end_date = DateField("End date", validators=[DataRequired()])
    submit = SubmitField("Submit") 

class Update_reservation_form(FlaskForm):
    start_date = DateField("Start date", validators=[DataRequired()])
    end_date = DateField("End date", validators=[DataRequired()])
    total = FloatField("Total", validators=[DataRequired()])
    submit = SubmitField("Submit") 

class Create_user_form(FlaskForm):
    first_name = StringField("First name", validators=[DataRequired(), Length(2,1000)])
    last_name = StringField("Last name", validators=[DataRequired(), Length(2,1000)])
    email = EmailField("E-mail", validators=[DataRequired(), Email(),Length(3,50)])
    phone_nr = StringField("Phone number", validators=[DataRequired(), Length(0,16)])
    password1 = PasswordField("Password", validators=[DataRequired(), Length(2,100)])
    password2 = PasswordField("Password again", validators=[DataRequired(), Length(2,100)])
    submit = SubmitField("Sign up") 

class Login_user_form(FlaskForm):
    email = EmailField("E-mail", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login") 