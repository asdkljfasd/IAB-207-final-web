from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
import os
from flask_login import LoginManager
from flask_bcrypt import Bcrypt

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)
    bcrypt = Bcrypt(app)
    Bootstrap5(app)
    app.secret_key = 'testing123'
    # Initialize SQLAlchemy with the Flask app

    # Configure and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rhythm_rally.sqlite'
    # Configure image upload folder
    UPLOAD_FOLDER = '/static/Image'
    app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER 
    db.init_app(app)

    login_manager.login_view = 'auth.login'  # Redirect to the login page if not logged in
    login_manager.init_app(app)

    # Define user_loader callback
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
      return db.session.scalar(db.select(User).where(User.user_id==user_id))
    
    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)
    
    @app.errorhandler(500) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("500.html", error=e)
    
    from . import views
    app.register_blueprint(views.mainbp)
    from . import auth
    app.register_blueprint(auth.authbp)
    from . import event
    app.register_blueprint(event.eventbp)
    
    return app

