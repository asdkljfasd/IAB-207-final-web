from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap5
import os
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()

def create_app():
    app = Flask(__name__)

    Bootstrap5(app)
    app.secret_key = 'testing123'
    # Initialize SQLAlchemy with the Flask app

    # Configue and initialise DB
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///rhythm_rally.sqlite'
    db.init_app(app)

    login_manager.login_view = 'auth.login'  # Redirect to the login page if not logged in
    login_manager.init_app(app)

    # Define user_loader callback
    from .models import User
    @login_manager.user_loader
    def load_user(user_id):
       return db.session.scalar(db.select(User).where(User.id==user_id))
    
    @app.errorhandler(404) 
    # inbuilt function which takes error as parameter 
    def not_found(e): 
      return render_template("404.html", error=e)
    
    from .views import mainbp
    app.register_blueprint(mainbp)
    from . import auth
    app.register_blueprint(auth.authbp)
    
    return app

