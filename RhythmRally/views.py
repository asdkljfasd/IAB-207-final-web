from flask import Blueprint, render_template
from . import db
from .forms import RegisterForm
from .models import Event

# Create a Blueprint
mainbp = Blueprint('main', __name__)

# Define routes using the Blueprint\

@mainbp.route("/")
def home():
    return render_template("index.html")

@mainbp.route("/history")
def booking_history():
    return render_template("bookinghistory.html")

@mainbp.route("/details")
def event_details():
    events = db.session.scalars(db.select(Event)).all() 
    print(events[0])
    
    return render_template("eventdetails.html", event = events[0])

@mainbp.route("/booking")
def book_event():
    return render_template("bookevent.html")

@mainbp.route("/user")
def user_register():
    form = RegisterForm() 
    return render_template("user.html", form=form, heading='Register')

