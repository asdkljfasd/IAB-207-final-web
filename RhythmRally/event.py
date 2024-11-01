import os
from flask import Blueprint, request, redirect, url_for, flash, render_template, current_app
from . import db
from .models import Event, Review
from flask_login import current_user, login_required
from datetime import datetime, date, time
from sqlalchemy import select
from werkzeug.utils import secure_filename
from .forms import ReviewForm, EventForm

eventbp = Blueprint('event', __name__, url_prefix='/events')

@eventbp.route("/event_list")
def list_events():
    events = db.session.scalars(select(Event)).all()
    return render_template("events.html", events=events)

# Function for event creation
@eventbp.route('/create_event', methods=['GET', 'POST'])
@login_required
def create_event():
    form = EventForm()  # Instantiate the form
    
    # Make sure form data is valid
    if form.validate_on_submit():
        try:
            db_file_path = check_upload_file(form)
            
            # Create a new Event instance with form data
            event = Event(
                event_name=form.event_name.data,
                artist_name=form.artist_name.data,
                event_venue=form.event_venue.data,
                event_date=form.date.data,
                event_start_time = form.start_time.data,
                event_end_time = form.end_time.data,
                event_ticket_price=form.ticket_price.data,
                tickets_available=form.number_of_tickets.data,
                event_description=form.description.data,
                event_category=form.category.data,
                event_creator_id=current_user.user_id,
                event_image=db_file_path)
            
            
            # Add event to the session and commit
            db.session.add(event)
            db.session.commit()
            
            flash('Successfully created new event', 'success')
            return redirect(url_for('event.list_events'))  # Redirect to an event list or details page
        except Exception as e:
            # If an error occurs, flash the error message
            flash(f"An error occurred while creating the event: {str(e)}", 'danger')

    return render_template('create_event.html', form=form)


def check_upload_file(form):
    fp = form.image.data
    filename = secure_filename(fp.filename)
    
    # Use the static/uploads directory for storing uploaded files
    BASE_PATH = os.path.join(current_app.static_folder, 'uploads')
    
    # Create the full upload path
    upload_path = os.path.join(BASE_PATH, filename)
    
    # Make sure the directory exists
    if not os.path.exists(BASE_PATH):
        os.makedirs(BASE_PATH)
    
    # Save the file
    fp.save(upload_path)
    
    # Return the path to be saved in the database
    # This ensures the returned path is relative and accessible for use in templates
    db_upload_path = f'uploads/{filename}'
    return db_upload_path

@eventbp.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(current_app.config['UPLOAD_FOLDER'], filename)

@eventbp.route('/details/<event_id>')
# Show selected event details
def event_details(event_id):
    event = db.session.scalar(db.select(Event).where(Event.event_id == event_id))
    
    # Update the event state if necessary
    if event:
        event.update_event_state()
        db.session.commit()
    else:
        flash("Event not found", 'danger')
        return redirect(url_for('event.list_events'))
    
    # Fetch reviews for the event
    reviews = db.session.scalars(db.select(Review).where(Review.event_id == event_id)).all()
    
    # Initialize an empty review form
    form = ReviewForm()

    return render_template('eventdetails.html', event=event, reviews=reviews, form=form)




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
    
    
