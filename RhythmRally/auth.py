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
        # Hash the password entered by the user
        hashed_password = generate_password_hash(form.password.data).decode('utf-8')

        # Create a new user instance with the hashed password
        new_user = User(
            first_name=form.first_name.data,
            surname=form.surname.data,
            email=form.email.data,
            password_hash=hashed_password,  # Store the hashed password
            contact_number=form.contact_number.data,
            street_address=form.street_address.data
        )

        # Add the user to the session and commit it to the database
        db.session.add(new_user)
        db.session.commit()

        flash('Registration successful. Please log in.', 'success')
        return redirect(url_for('auth.login'))

    return render_template('user.html', form=form, heading='Register')

    



@authbp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Get the email and password from the form
        user_email = form.email.data
        user_password = form.password.data

        # Query the user from the database by email
        user = db.session.scalar(db.select(User).where(User.email == user_email))

        # If the user doesn't exist or the password is incorrect
        if user is None:
            flash('Incorrect email. Please try again.', 'danger')
        elif not bcrypt.check_password_hash(user.password_hash, user_password):
            flash('Incorrect password. Please try again.', 'danger')
        else:
            # Log the user in using Flask-Login
            login_user(user)
            flash('Logged in successfully!', 'success')
            return redirect(url_for('main.home'))

    return render_template('user.html', form=form, heading='Login')


@authbp.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.index'))
