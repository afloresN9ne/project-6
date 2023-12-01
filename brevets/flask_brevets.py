"""
Replacement for RUSA ACP brevet time calculator
(see https://rusa.org/octime_acp.html)

"""

import flask
from flask import request
import arrow  # Replacement for datetime, based on moment.js
import acp_times  # Brevet time calculations
import config
from mydb import insert_db,fetch_db

from pymongo import MongoClient
import logging

###
# Globals
###
app = flask.Flask(__name__)
CONFIG = config.configuration()

###
# Pages
###


@app.route("/")
@app.route("/index")
def index():
    app.logger.debug("Main page entry")
    return flask.render_template('calc.html')


@app.errorhandler(404)
def page_not_found(error):
    app.logger.debug("Page not found")
    return flask.render_template('404.html'), 404




@app.route("/insert", methods=["POST"])
def insert():
    app.logger.debug("Received POST request to /insert")
    """
    /insert : inserts a to-do list into the database.

    Accepts POST requests ONLY!

    JSON interface: gets JSON, responds with JSON
    """
    try:
        # Read the entire request body as a JSON
        # This will fail if the request body is NOT a JSON.
        input_json = request.json
        # if successful, input_json is automatically parsed into a python dictionary!

        # Because input_json is a dictionary, we can do this:
        brevet_distance = input_json["brevet_distance"] # Should be a string
        start_date = input_json["start_date"]
        times = input_json["times"]


        insert_id = insert_db(brevet_distance,start_date,times)

        return flask.jsonify(result={},
                        message="Inserted!",
                        status=1, # This is defined by you. You just read this value in your javascript.
                        mongo_id=insert_id)
    except:
        # The reason for the try and except is to ensure Flask responds with a JSON.
        # If Flask catches your error, it means you didn't catch it yourself,
        # And Flask, by default, returns the error in an HTML.
        # We want /insert to respond with a JSON no matter what!
        return flask.jsonify(result={},
                        message="Oh no! Server error!",
                        status=0,
                        mongo_id='None')


@app.route("/fetch")
def fetch():
    """
    /fetch : fetches the newest to-do list from the database.

    Accepts GET requests ONLY!

    JSON interface: gets JSON, responds with JSON
    """
    try:
        brevet_distance,start_date,times = fetch_db()
        return flask.jsonify(
                result={"brevet_distance": brevet_distance, "start_date": start_date,"times":times},
                status=1,
                message="Successfully fetched a db list!")
    except:
        return flask.jsonify(
                result={},
                status=0,
                message="Something went wrong, couldn't fetch any lists!")


###############
#
# AJAX request handlers
#   These return JSON, rather than rendering pages.
#
###############
@app.route("/_calc_times")
def _calc_times():
    """
    Calculates open/close times from miles, using rules
    described at https://rusa.org/octime_alg.html.
    Expects one URL-encoded argument, the number of miles.
    """
    app.logger.debug("Got a JSON request")
    km = request.args.get('km', 999, type=float)
    
    #gets arguments 
    begin = request.args.get('begin',type = str)
    bd = request.args.get('bd',type = float)

    
    app.logger.debug("bd={}".format(bd))
    app.logger.debug("begin={}".format(begin))
    #end of my code


    app.logger.debug("km={}".format(km))
    app.logger.debug("request.args: {}".format(request.args))
    
    # FIXME!
    # Right now, only the current time is passed as the start time
    # and control distance is fixed to 200
    # You should get these from the webpage!

    #calls functions in acp_times.py using arguments gotten with reqquest.args.get
    open_time = acp_times.open_time(km, bd, begin).isoformat()
    close_time = acp_times.close_time(km, bd, begin).isoformat()
    result = {"open": open_time, "close": close_time}
    return flask.jsonify(result=result)


#############

app.debug = CONFIG.DEBUG
if app.debug:
    app.logger.setLevel(logging.DEBUG)

if __name__ == "__main__":
    print("Opening for global access on port {}".format(CONFIG.PORT))
    app.run(port=CONFIG.PORT, host="0.0.0.0")
