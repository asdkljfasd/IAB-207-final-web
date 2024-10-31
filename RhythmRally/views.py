from flask import Blueprint, request, redirect, url_for, flash, render_template
from . import db
from .forms import RegisterForm
from .models import Event, Review
from flask_login import current_user

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
    event = db.session.scalars(db.select(Event).where(Event.event_id == event_id))
    return render_template("eventdetails.html", event = event)

@mainbp.route("/booking")
def book_event():
    return render_template("bookevent.html")

@mainbp.route("/user")
def user_register():
    form = RegisterForm() 
    return render_template("user.html", form=form, heading='Register')

@mainbp.route('/submit_review', methods=['POST'])
def submit_review():
    if request.method == 'POST':
        rating = request.form.get('rating')
        comment = request.form.get('comment')
        event_id = request.form.get('event_id')
        
        new_review = Review(user_id = current_user.user_id, event_id = event_id, comment = comment, posted_datetime = datetime.now(), rating = int(rating))
        
        try:
            db.session.add(new_review)
            db.session.commit()
            flash("Review submitted.")
        except Exception as e:
                db.session.rollback()
                flash(f"An error occurred: {e}")
                
        return redirect(url_for('main.event_details', event_id=event_id))
    else:
        flash("You need to be logged in to post a review.")
        return redirect(url_for('auth.login'))

