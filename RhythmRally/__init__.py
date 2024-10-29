from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()

def create_app():
    app=Flask(__name__)
    app.debug=True
    app.secret_key = 'testing123'
    
    app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///rhythmrally.db'
    
    db.init_app(app)
    boots
