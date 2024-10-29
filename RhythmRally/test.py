from flask import Flask, render_template

app = Flask(__name__)

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
