from . import db
from datetime import date, time
from flask_login import UserMixin

class User(db.Model, UserMixin):
    __tablename__ = 'users' 
    user_id = db.Column(db.Integer, primary_key=True)  
    first_name = db.Column(db.String(50), index=True, unique=True, nullable=False)
    surname = db.Column(db.String(50), index=True, unique=True, nullable=False)
    emailid = db.Column(db.String(100), index=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    contact_number = db.Column(db.String(15), nullable=False)  
    street_address = db.Column(db.String(100), nullable=False)
    
        # Relationships
    reviews = db.relationship('Review', backref='user', lazy='select')
    purchases = db.relationship('Purchase', backref='user', lazy='select')
    events = db.relationship('Event', backref='user', lazy='select')
    tickets = db.relationship('Ticket', backref='user', lazy='select')

    
    # String representation method
    def __repr__(self):
        return f"User(user_id={self.user_id}, name={self.first_name} {self.surname})"

class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    event_name = db.Column(db.String(100), nullable=False)
    event_creator_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  
    artist_name = db.Column(db.String(50), nullable=False)
    event_venue = db.Column(db.String(50), nullable=False)
    event_date = db.Column(db.Date, nullable=False)
    event_start_time = db.Column(db.Time, nullable=False)
    event_end_time = db.Column(db.Time, nullable=False)
    event_ticket_price = db.Column(db.Float, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)
    #event_status = 

    # Relationships
    tickets = db.relationship('Ticket', backref='event', lazy='select')
    reviews = db.relationship('Review', backref='event', lazy='select')

    def __repr__(self):
        return f"<Event event_id={self.event_id}, event_name='{self.event_name}', artist_name='{self.artist_name}', venue='{self.event_venue}', date={self.event_date}, category={self.category}>"

class Ticket(db.Model):
    __tablename__ = 'tickets'
    ticket_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    price = db.Column(db.Float, nullable=False)  

    # Relationships
    purchases = db.relationship('Purchase', backref='ticket', lazy='select')

    def __repr__(self):
        return f"<Ticket ticket_id={self.ticket_id}, event_id={self.event_id}, owner_id={self.owner_id}, price={self.price}>"



class Purchase(db.Model):
    __tablename__ = 'purchases'
    purchase_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)  
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'), nullable=False)  
    purchase_datetime = db.Column(db.DateTime, nullable=False)
    ticket_quantity = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Purchase purchase_id={self.purchase_id}, user_id={self.user_id}, ticket_id={self.ticket_id}, purchase_datetime={self.purchase_datetime}, ticket_quantity={self.ticket_quantity}, price={self.price}>"

class Review(db.Model):
    __tablename__ = 'reviews'
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False) 
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False) 
    comment = db.Column(db.String(200), nullable=False)
    posted_datetime = db.Column(db.DateTime, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    
    # Relationships
    user = db.relationship('User', backref='user_reviews', lazy='select')

    def __repr__(self):
        return f"<Review comment_id={self.comment_id}, user_id={self.user_id}, event_id={self.event_id}, comment='{self.comment}', posted_datetime={self.posted_datetime}, rating={self.rating}>"
