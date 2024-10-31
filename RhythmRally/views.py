from flask import Blueprint, request, redirect, url_for, flash, render_template
from . import db
from .forms import RegisterForm
from .models import Event, Review, Purchase
from flask_login import current_user, login_required
from datetime import datetime

# Create a Blueprint
mainbp = Blueprint('main', __name__)

# Define routes using the Blueprint\

@mainbp.route("/")
def home():
    return render_template("index.html")

@mainbp.route("/history")
@login_required
def booking_history():
    user_purchases = db.session.scalars(select(Purchase).where(Purchase.user_id == current_user.user_id)).all()
    return render_template("bookinghistory.html", purchases = user_purchases)
@mainbp.route("/user")
def user_register():
    form = RegisterForm() 
    return render_template("user.html", form=form, heading='Register')



