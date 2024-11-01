import os
from flask import Blueprint, request, redirect, url_for, flash, render_template
from . import db
from .models import Event, Review
from flask_login import current_user, login_required
from datetime import datetime
from werkzeug.utils import secure_filename

eventbp = Blueprint('event', __name__, url_prefix='/events')



# Function for event creation
@eventbp.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()  # Instantiate the form
    if form.validate_on_submit():
        db_file_path = check_upload_file(form)
        event = Event(event_name = form.event_name.data,artist_name = form.artist_name.data, 
                event_venue = form.event_venue.data, event_date = form.date.data, 
                event_start_time = form.start_time.data, event_end_time = form.end_time.data, 
                event_ticket_price = form.ticket_price.data, event_ticket_available = form.number_of_tickets.data, 
                event_description = form.description.data, event_category = form.category.data, event_creator_id = current_user.user_id, event_image = db_file_path)
        db.session.add(event)
        db.session.commit()
        flash('Successfully created new event', 'success')
        return redirect(url_for('event.create_event'))
    return render_template('create_event.html', form=form)

# function for obtaining image file path
def check_upload_file(form):
    fp = form.image.data
    filename = fp.filename
    BASE_PATH = os.path.dirname(__file__)
    upload_path = os.path.join(BASE_PATH, 'static/image', secure_filename(filename))
    db_upload_path = '/static/image/' + secure_filename(filename)
    fp.save(upload_path)
    return db_upload_path



@eventbp.route('/details/<event_id>')
# show selected event details
def event_details(event_id):
    event = db.session.scalar(db.select(Event).where(Event.event_id == event_id))
    reviews = db.session.scalars(db.select(Review).where(Review.event_id == event_id)).all()
    form = ReviewForm()
    return render_template('eventdetails.html', event = event, reviews = reviews)



@eventbp.route('<event_id>/review', methods=['GET','POST'])
@login_required
# function for submitting review
def submit_review(event_id):
    form = ReviewForm(event_id) 
    event = db.session.scalar(db.select(Event).where(Event.event_id == event_id))
    if form.validate_on_submit():
        review = Review(user_id = current_user.user_id, event_id = event_id, comment = form.comment.data, posted_datetime = datetime.now(), rating = form.rating.data)
        db.session.add(review)
        db.session.commit()
        flash('Review submitted successfully.','success' )
    return redirect(url_for('event.event_details', event_id=event_id))
    
    
