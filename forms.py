from flask_wtf import FlaskForm
from wtforms import StringField , PasswordField , SubmitField  ,BooleanField
from wtforms.validators import DataRequired , Length , Email , EqualTo
#DataRequired - Check that the name field is not empty
#Length - Check that the name does not extends the limit specified



class RegistrationForm(FlaskForm):
    username = StringField('Username' , validators = [DataRequired() , 
                                                            Length(min = 2 , max = 20)])
    email = StringField('Email' , validators = [DataRequired() , Email()])
    password = PasswordField('Password' , validators = [DataRequired()])
    confirm_password = PasswordField('Confirm Password' , validators = [DataRequired() , EqualTo('password')])

    submit = SubmitField('Sign Up')

class LoginForm(FlaskForm):
    email = StringField('Email' , validators = [DataRequired() , Email()])              
    password = PasswordField('Password' , validators = [DataRequired ()]) 
    remember = BooleanField('Remember Me')                   
    submit = SubmitField('Login')                                                     