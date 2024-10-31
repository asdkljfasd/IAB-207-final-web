from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateTimeField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

#User login
class LoginForm(FlaskForm):
    user_name = StringField("User Name", validators=[InputRequired('Enter user name')])
    password = PasswordField("Password", validators=[InputRequired('Enter user password')])
    submit = SubmitField("Login")

class RegisterForm(FlaskForm):
    username = StringField("Username", validators=[InputRequired()])
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
    
class EventForm(FlaskForm):
    eventname = StringField('Event Name', validators= [InputRequired("Please Enter the Event Name")])
    artistname = StringField('Artist Name', validators= [InputRequired("Please Enter the Artist Name")])
    description = TextAreaField('Description', validators= [InputRequired("Please Enter a Description")])
    image = StringField('Event Image', validators= [InputRequired("Please Provide an Image")])
    date = DateTimeField('Event Date', validators= [InputRequired("Please Enter the Date of the Event")])
    start_time = DateTimeField('Start Time', validators= [InputRequired("Please Enter a Start Time")])
    end_time = DateTimeField('End Time', validators= [InputRequired("Please Enter an End Time")])
    ticket_price = StringField('Ticket Price', validators= [InputRequired("Please Enter a Ticket Price")])
