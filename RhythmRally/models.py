from test import db

class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50), nullable=False)
    surname = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(50), nullable=False)
    user_status = db.Column(db.String(20), nullable=False)

    # Relationships
    reviews = db.relationship('Review', backref='user', lazy='select')
    purchases = db.relationship('Purchase', backref='user', lazy='select')

    def __repr__(self):
        return f"<User user_id={self.user_id}, name='{self.name}', email='{self.email}', user_status='{self.user_status}'>"


class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key=True)
    artist_name = db.Column(db.String(50), nullable=False)
    event_location = db.Column(db.String(50), nullable=False)
    date = db.Column(db.DateTime, nullable=False)
    category = db.Column(db.String(30), nullable=False)
    description = db.Column(db.String(200), nullable=False)

    # Relationships
    tickets = db.relationship('Ticket', backref='event', lazy='select')
    reviews = db.relationship('Review', backref='event', lazy='select')

    def __repr__(self):
        return f"<Event event_id={self.event_id}, artist_name='{self.artist_name}', location='{self.event_location}', date='{self.date}', category='{self.category}'>"


class Ticket(db.Model):
    __tablename__ = 'tickets'
    ticket_id = db.Column(db.Integer, primary_key=True)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    price = db.Column(db.Float, nullable=True)  # Price may be optional

    # Relationships
    status_records = db.relationship('TicketStatus', backref='ticket', lazy='select')
    purchases = db.relationship('Purchase', backref='ticket', lazy='select')

    def __repr__(self):
        return f"<Ticket ticket_id={self.ticket_id}, event_id={self.event_id}, price={self.price}>"


class TicketStatus(db.Model):
    __tablename__ = 'ticket_status'
    ticket_status_id = db.Column(db.Integer, primary_key=True)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'), nullable=False)
    status_date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        return f"<TicketStatus ticket_status_id={self.ticket_status_id}, ticket_id={self.ticket_id}, status_date={self.status_date}>"


class Purchase(db.Model):
    __tablename__ = 'purchases'
    purchase_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    ticket_id = db.Column(db.Integer, db.ForeignKey('tickets.ticket_id'), nullable=False)
    purchase_date = db.Column(db.DateTime, nullable=False)
    num_tickets = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Purchase purchase_id={self.purchase_id}, user_id={self.user_id}, ticket_id={self.ticket_id}, purchase_date={self.purchase_date}, num_tickets={self.num_tickets}, price={self.price}>"


class Review(db.Model):
    __tablename__ = 'reviews'
    comment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    event_id = db.Column(db.Integer, db.ForeignKey('events.event_id'), nullable=False)
    comment = db.Column(db.String(200), nullable=False)
    posted_date = db.Column(db.DateTime, nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Review comment_id={self.comment_id}, user_id={self.user_id}, event_id={self.event_id}, comment='{self.comment}', posted_date={self.posted_date}, rating={self.rating}>"
