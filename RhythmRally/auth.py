from flask import Blueprint, render_template, redirect, url_for, flash
from .forms import LoginForm, RegisterForm
from flask_login import current_user, login_required, logout_user
from flask_bcrypt import generate_password_hash, check_password_hash
from .models import User
from . import db
from sqlalchemy import select
from flask_bcrypt import Bcrypt

# create a blueprint
authbp = Blueprint('auth', __name__ )

@authbp.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        new_user = User(first_name = form.first_name.data,
                        surname = form.surname.data,email = form.email.data,
                        password_hash = form.password.data, 
                        contact_number = form.contact_number.data, street_address = form.street_address.data ) 
        

        # Check if a user exists
        existing_user = db.session.scalar(db.select(User).where(User.email == new_user.email))
        if existing_user:  # This returns true when user is not None
            flash('Email already exists, please try another')
            return redirect(url_for('auth.register'))

        # Hash the password
        pwd_hash = generate_password_hash(new_user.password_hash)

        # Create a new User model object
        db.session.add(new_user)
        db.session.commit()

        # Redirect to the main index page
        return redirect(url_for('main.home'))

    # Called if the HTTP request is GET
    return render_template('user.html', form=form, heading='Register')

    
bcrypt = Bcrypt()  # This should ideally be done globally, e.g., in app factory function.

@authbp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Get the email and password from the form
        user_email = form.email.data
        user_password = form.password.data

        # Query the user from the database by email
        user = db.session.scalar(db.select(User).where(User.email == user_email))

        # If there is no user with that email
        if user is None:
            flash('Incorrect email. Please try again.', 'danger')
        # Check the password using the hash function
        elif not check_password_hash(user.password_hash, user_password):
            flash('Incorrect password. Please try again.', 'danger')
        else:
            # Log the user in using Flask-Login
            login_user(user)
            return redirect(url_for('main.home'))

    return render_template('user.html', form=form, heading='Login')


@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
