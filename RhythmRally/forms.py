from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

#User login
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    first_name = StringField("First Name", validators=[InputRequired()])
    surname = StringField("Surname", validators=[InputRequired()])
    email = StringField("Email Address", validators=[Email("Please enter a valid email")])
    password = PasswordField("Password", validators=[
        InputRequired(),
        EqualTo('confirm', message="Passwords should match")
    ])
    confirm = PasswordField("Confirm Password")
    contact_number = StringField("Contact Number", validators=[InputRequired()])
    street_address = StringField("Street Address", validators=[InputRequired()])
    
    # Submit button
    submit = SubmitField("Register")
