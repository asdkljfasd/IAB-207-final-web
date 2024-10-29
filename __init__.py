from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap


db = SQLAlchemy()

def creat_app():
    app=Flask(__name__)
    app.debug=True
    app.secret_key='testing123'
    
    #db config for app
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///RythmRally.db'
    
    # initialise database with Flask
    db.init_app(app)
    
    bootstrap=Bootstrap(app)
    
    return app
    