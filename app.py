# ---- YOUR APP STARTS HERE ----
# -- Import section --
from flask import Flask
from flask import render_template
from flask import request
from flask import redirect
from flask_pymongo import PyMongo


# -- Initialization section --
app = Flask(__name__)

# events = [
#         {"event":"First Day of Classes", "date":"2019-08-21"},
#         {"event":"Winter Break", "date":"2019-12-20"},
#         {"event":"Finals Begin", "date":"2019-12-01"}
#     ]

# name of database
app.config['MONGO_DBNAME'] = 'database'

# URI of database
app.config['MONGO_URI'] = 'mongodb+srv://admin:kirkland2$@cluster0.bvl1d.mongodb.net/database?retryWrites=true&w=majority'

mongo = PyMongo(app)

# -- Routes section --
# INDEX

@app.route('/')
@app.route('/index')

def index():
    events = mongo.db.events
    events = events.find({})
    return render_template('index.html', events = events)


# CONNECT TO DB, ADD DATA

@app.route('/add')

def add():
    # connect to the database
    events = mongo.db.events
    # # insert new data
    # events.insert({"event": "First Day of Class", "date": "2021-09-13"})
    # # return a message to the user
    # return "event added"
    # insert new data
    events.insert({"event": "College Move In Day", "date": "2021-08-14"})
    # return a message to the user
    return "event added!"

@app.route("/events/new", methods = ["GET", "POST"])
def new_event():
    if request.method == "GET":
        return render_template("newevent.html")
    else:
        event_name = request.form["event_name"]
        event_date = request.form["event_date"]
        user_name = request.form["user_name"]
        events = mongo.db.events
        events.insert({
            "event": event_name,
            "date": event_date,
            "user": user_name
        })
        return redirect("/")