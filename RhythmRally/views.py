from flask import Blueprint, render_template
from .models import User, Event, Ticket, TicketStatus, Purchase, Review
from . import db


# Create a Blueprint
mainbp = Blueprint('main', __name__)

# Define routes using the Blueprint
@mainbp.route("/")
def home():
    return render_template("index.html")

@mainbp.route("/history")
def booking_history():
    return render_template("bookinghistory.html")

@mainbp.route("/details")
def event_details():
    return render_template("eventdetails.html")

@mainbp.route("/booking")
def book_event():
    return render_template("bookevent.html")

@mainbp.route("/login")
def login_form():
    return render_template('loginform.html')

@mainbp.route("/register")
def register():
    return render_template('register.html')
#@app.route("/update")
#def event_update():
    #return render_template("eventupdate.html")