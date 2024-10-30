from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
import os


db = SQLAlchemy()
        
def create_app():
    app = Flask(__name__)

    Bootstrap5(app)
    app.secret_key = 'somerandomvalue'
    # Initialize SQLAlchemy with the Flask app


    # Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///traveldb.sqlite'
    db.init_app(app)
    from .models import User, Event, Ticket, TicketStatus, Purchase, Review
    return app