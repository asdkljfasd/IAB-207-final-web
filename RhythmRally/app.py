from flask import Flask, render_template, url_for

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

@app.route("/login")
def login_form():
    return render_template('loginform.html')

@app.route("/register")
def register():
    return render_template('register.html')

#@app.route("/update")
#def event_update():
    #return render_template("eventupdate.html")

if __name__ == "__main__":
    app.run(debug=True)