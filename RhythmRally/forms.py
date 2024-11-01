from flask_wtf import FlaskForm
from wtforms.fields import TextAreaField, SubmitField, StringField, PasswordField, DateField, TimeField, IntegerField, FloatField, SelectField
from wtforms.validators import InputRequired, Length, Email, EqualTo
from flask_wtf.file import FileRequired, FileField, FileAllowed

#User login
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[InputRequired('Enter user email.')])
    password = PasswordField('Password', validators=[InputRequired('Enter user password')])
    submit = SubmitField('Login')

class RegisterForm(FlaskForm):
    first_name = StringField('First name', validators=[InputRequired('Please enter your first name.')])
    surname = StringField('Surname', validators=[InputRequired('Please enter your surname.')])
    email = StringField('Email Address', validators=[InputRequired('Please enter a valid email.')])
    password = PasswordField('Password', validators=[
        InputRequired(),
        EqualTo('confirm', message='Passwords should match')
    ])
    confirm = PasswordField('Confirm Password')
    contact_number = StringField('Contact Number', validators=[InputRequired()])
    street_address = StringField('Street Address', validators=[InputRequired()])
    
    # Submit button
    submit = SubmitField('Register')
    
class EventForm(FlaskForm):
    event_name = StringField('Event Name', validators= [InputRequired("Please enter the event's name.")])
    artist_name = StringField('Artist Name', validators= [InputRequired("Please enter the performing artist's name.")])
    event_venue = StringField('Event venue', validators= [InputRequired('Please enter the venue where your event will be held.')])
    description = TextAreaField('Description', validators= [InputRequired('Please enter a description for your event.')])
    image = FileField('Event Image', validators= [InputRequired('Please provide an image related to your event.'), FileAllowed(['jpg', 'jpeg','png'])])
    date = DateField('Event Date', validators= [InputRequired('Please enter the date of the event.')])
    start_time = TimeField('Start Time', validators= [InputRequired('Please enter the planned starting time of your event.')])
    end_time = TimeField('End Time', validators= [InputRequired('Please enter the planned end time of your event.')])
    ticket_price = FloatField('Ticket Price', validators= [InputRequired('Please enter the price per ticket.')])
    number_of_tickets = IntegerField('Number Of Tickets', validators= [InputRequired('Please enter the number of tickets available for sale.')])
    category = SelectField('Category',choices=[('Jazz', 'Jazz'), ('Pop', 'Pop'), ('Rock', 'Rock'), ('RnB', 'RnB'), ('Country', 'Country'), ('HipHop', 'HipHop'),('Others','Others')],validators=[InputRequired('Please select the category closest to your event.')])
    submit = SubmitField('Create')
    

class ReviewForm(FlaskForm):
    rating = SelectField('Rating (1-5)',choices=[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')],
            validators=[InputRequired(message='Rate your experience!')])
    comment = TextAreaField('Comment', render_kw={'placeholder': 'What do you think about this event?'})
    submit = SubmitField('Submit')

