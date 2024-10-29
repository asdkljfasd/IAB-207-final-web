from test import db 

#defining models
class User(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(30), nullable = False)
    email = db.Column(db.String(50),nullable = False)
    password = db.Column(db.String(30),nullable = False)
    user_status = db.Column(db.String(20)nullable = False)
    
    def __repr(self):
        return f"<User user_id={self.user_id}, username='{self.username}', email='{self.email}', user_status ='{self.user_status}'>"
    
    
    
    
class Event(db.Model):
    __tablename__ = 'events'
    event_id = db.Column(db.Integer, primary_key = True)
    artist_name = db.Column(db.String(50),nullable = False)
    event_location = db.Column(db.String(50),nullable = False)
    event_date = db.Column(db.DateTime,nullable = False)
    category = db.Column(db.String(30),nullable = False)
    description = db.Column(db.String(200),nullable = False)
    def __repr(self):
        return f"<Event event_id={self.event_id}, artist_name='{self.artist_name}', event_location='{self.event_location}', event_date= '{self.event_date}',category='{self.category}', description = '{self.description}'>"
    
    
    
class Ticket(db.Model):
    __tablename__ = 'tickets'
    ticket_id = db.Column(db.Integer, primary_key = True)
    event_id = db.Column(db.Integer,nullable = False)
    price = db.Column(db.Float,nullable = False)
    def __repr(self):
        return f"<Ticket user_id={self.user_id}, event_id='{self.event_id}', price='{self.price}'>"
    
    
class Ticket_status(db.Model):
    __tablename__ = 'ticket status'
    ticket_status_id = db.Column(db.Integer, primary_key = True)
    ticket_id = db.Column(db.Integer,nullable = False)
    status_date = db.Column(db.DateTime,nullable = False)
    def __repr(self):
        return f"<Ticket_status ticket_status_id={self.ticket_status_id}, ticket_id='{self.ticket_id}', status_date='{self.status_date}'>"
        
        
class Purchase(db.Model):
    __tablename__ = 'purchases'
    purchase_id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer,nullable = False)
    ticket_id = db.Column(db.Integer,nullable = False)
    purchase_date = db.Column(db.DateTime,nullable = False)
    num_ticket = db.Column(db.Integer,nullable = False)
    price = db.Column(db.Float,nullable = False)
    def __repr(self):
        return f"Purchase purchase_id={self.purchase_id}, user_id='{self.user_id}', ticket_id='{self.ticket_id}', purchase_date ='{self.purchase_date}', num_ticket = '{self.num_ticket}, price = '{self.price}'>"
    

class Review(db.Model):
    __tablename__ = 'reviews'
    comment_id = db.Column(db.Integer, primary_key = True)
    user_id  = db.Column(db.Integer,nullable = False)
    username = db.Column(db.String(30), nullable = False)
    event_id = db.Column(db.Integer,nullable = False)
    comment = db.Column(db.String(30),nullable = False)
    posted_date = db.Column(db.DateTime,nullable = False)
    rating = db.Column(db.Float,nullable = False)
    def __repr(self):
        return f"<Review comment_id = {self.comment_id} ,user_id={self.user_id}, username='{self.username}', event_id='{self.email}', comment ='{self.user_status}', pposted_date ={self.posted_date}, rating = {self.rating}>"
    
    