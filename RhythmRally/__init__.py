from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
import os



db = SQLAlchemy()
        
def create_app():
    app = Flask(__name__)

    Bootstrap5(app)
    app.secret_key = 'testing123'
    # Initialize SQLAlchemy with the Flask app


    # Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rhythm_rally.sqlite'
    db.init_app(app)
    
    from .models import User, Event, Ticket, TicketStatus, Purchase, Review
    from .views import mainbp
    app.register_blueprint(mainbp)
    
    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)
    
    
    return app