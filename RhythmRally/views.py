from flask import Blueprint, request, redirect, url_for, flash, render_template
from . import db
from .forms import RegisterForm
from .models import Event, Review, Purchase
from flask_login import current_user, login_required
from datetime import datetime
from sqlalchemy import select

# Create a Blueprint
mainbp = Blueprint('main', __name__)

# Define routes using the Blueprint\

@mainbp.route("/")
def home():
    events = db.session.scalars(select(Event)).all()
    for event in events:
        event.update_event_state()
    db.session.commit()
    return render_template("index.html", events = events)

@mainbp.route("/history")
@login_required
def booking_history():
    user_purchases = db.session.scalars(select(Purchase).where(Purchase.user_id == current_user.user_id)).all()
    return render_template("bookinghistory.html", purchases = user_purchases)


@mainbp.route("/user")
def user_register():
    form = RegisterForm() 
    return render_template("user.html", form=form, heading='Register')



