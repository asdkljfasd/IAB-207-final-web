from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateTimeField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo

# form for user registration
class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired(), Length(max=50)])
    last_name = StringField("Last Name", validators=[DataRequired(), Length(max=50)])
    username = StringField("Username", validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=6)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    contact_number = StringField("Contact Number", validators=[DataRequired(), Length(max=15)])
    street_address = StringField("Street Address", validators=[DataRequired(), Length(max=100)])
    submit = SubmitField("Register")