from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, TextAreaField, DateTimeField, IntegerField, FloatField
from wtforms.validators import DataRequired, Email, Length, EqualTo

class RegistrationForm(FlaskForm):
    first_name = StringField("First name", validators=[InputRequired()])
    last_name = StringField("Last name", validators=[InputRequired()])
    username = StringField("User name", validators=[InputRequired()])
    email = StringField("Email", validators=[InputRequired()])
    password = PasswordField("Password", validators =[InputRequired()])