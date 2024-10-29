from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
import os


app = Flask(__name__)

# Configure the database
basedir = os.path.abspath(os.path.dirname(__file__))
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'database.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Initialize SQLAlchemy with the Flask app
db = SQLAlchemy(app)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/history")
def booking_history():
    return render_template("bookinghistory.html")

@app.route("/details")
def event_details():
    return render_template("eventdetails.html")

@app.route("/booking")
def book_event():
    return render_template("bookevent.html")

if __name__ == "__main__":
    app.run(debug=True)
