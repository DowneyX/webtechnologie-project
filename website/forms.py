from flask_wtf import FlaskForm
from wtforms import (StringField, BooleanField, FloatField, RadioField, TextAreaField, SubmitField,DateField, EmailField, PasswordField,)
from wtforms.validators import DataRequired, Email, Length

class Create_bungalow_form(FlaskForm):
    title = StringField("Titel", validators=[DataRequired(), Length(2,50)])
    description =  TextAreaField("Omschrijving", validators=[DataRequired(), Length(2,2000)])
    price = FloatField("Prijs", validators=[DataRequired()])
    max_p = RadioField('Max hoeveelheid mensen', choices=[(4,'4 Mensen'),(6,'6 Mensen'),(8,'8 Mensen')], validators=[DataRequired()],coerce=int)
    submit = SubmitField("Submit")
    
class Date_form(FlaskForm):
    start_date = DateField("Start datum", validators=[DataRequired()])
    end_date = DateField("Eind datum", validators=[DataRequired()])
    submit = SubmitField("Boeken") 

class Update_reservation_form(FlaskForm):
    start_date = DateField("Start datum", validators=[DataRequired()])
    end_date = DateField("Eind datum", validators=[DataRequired()])
    total = FloatField("Totaal", validators=[DataRequired()])
    submit = SubmitField("Update") 

class Create_user_form(FlaskForm):
    first_name = StringField("Voornaam", validators=[DataRequired(), Length(2,1000)])
    last_name = StringField("Achternaam", validators=[DataRequired(), Length(2,1000)])
    email = EmailField("E-mail", validators=[DataRequired(), Email(),Length(3,50)])
    phone_nr = StringField("Telefoon", validators=[DataRequired(), Length(0,16)])
    password1 = PasswordField("Wachtwoord", validators=[DataRequired(), Length(2,100)])
    password2 = PasswordField("Wachtwoord opnieuw", validators=[DataRequired(), Length(2,100)])
    submit = SubmitField("Registreer") 

class Update_password_form(FlaskForm):
    current_password = PasswordField("Huidige wachtwoord", validators=[DataRequired(), Length(2,100)])
    password1 = PasswordField("Nieuwe wachtwoord", validators=[DataRequired(), Length(2,100)])
    password2 = PasswordField("Nieuwe wachtwoord opnieuw", validators=[DataRequired(), Length(2,100)])
    submit = SubmitField("Update") 

class Update_user_form(FlaskForm):
    first_name = StringField("Voornaam", validators=[DataRequired(), Length(2,1000)])
    last_name = StringField("Achternaam", validators=[DataRequired(), Length(2,1000)])
    email = EmailField("E-mail", validators=[DataRequired(), Email(),Length(3,50)])
    phone_nr = StringField("Telefoon", validators=[DataRequired(), Length(1,16)])
    submit = SubmitField("Update")

class Update_user_role_form(FlaskForm):
    role = RadioField('welke rol dien je aan deze gebruiker toe', choices=[('admin','administrator'),('user','gebruiker')], validators=[DataRequired()])
    submit = SubmitField("Update")

class Login_user_form(FlaskForm):
    email = StringField("E-mail", validators=[DataRequired()])
    password = PasswordField("Wachtwoord", validators=[DataRequired()])
    remember = BooleanField("Onthoud mij")
    submit = SubmitField("Login") 

class Contact_form(FlaskForm):
    email = EmailField("E-mail", validators=[DataRequired(), Email(),Length(3,50)])
    message =  TextAreaField("Bericht", validators=[DataRequired(), Length(2,2000)])
    submit = SubmitField("Verstuur")

