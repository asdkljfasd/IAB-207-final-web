from flask import Blueprint, render_template
from .models import User, Event, Ticket, TicketStatus, Purchase, Review
from . import db

mainbp = Blueprint('main', __name__)

@mainbp.route('/')
def index():
    return render_template('index.html')