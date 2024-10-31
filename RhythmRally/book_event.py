from flask import Blueprint, render_template
from .models import Event
from .forms import EventForm

eventsbp = Blueprint('events', __name__)



# Function for event booking
@eventsbp.route('/book_event', methods=['GET', 'POST'])
def book_event():
    form = EventForm()  # Instantiate the form
    if form.validate_on_submit():
        print('Successfully Created Event!')
    # Pass the form instance to the template
    return render_template("create.html", form=form)