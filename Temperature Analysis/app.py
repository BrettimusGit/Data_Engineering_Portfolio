import datetime as dt
import numpy as np
import pandas as pd
from flask import Flask, jsonify
import json
from sqlHelper import SQLHelper

#######################################################

app = Flask(__name__)

sqlHelper = SQLHelper()

@app.route("/")
def home():
    print("Client requested the home page from the server")
    return(
        """<h4>Routes Available:</h4>
        <p>/api/v1.0/precipitation</p>
        <p>/api/v1.0/stations"</p>
        <p>/api/v1.0/tobs"</p>
        <p>/api/v1.0/&lt;start&gt;</p>
        <p>/api/v1.0/&lt;start&gt;/&lt;end&gt;</p>
        <h4>Links Available</h4>
        <p><a href="/api/v1.0/precipitation">Precipitation</a></p>
        <p><a href="/api/v1.0/stations">Stations</a></p>
        <p><a href="/api/v1.0/tobs">TOBS</a></p>
        """)

@app.route("/api/v1.0/precipitation")
def get_precipitation():
    data = sqlHelper.get_precipitation()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/stations")
def get_stations():
    data = sqlHelper.get_stations()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/tobs")
def get_tobs():
    data = sqlHelper.get_tobs()
    return jsonify(json.loads(data.to_json(orient="records")))

@app.route("/api/v1.0/<start>")
def get_temp_start(start):
    data=sqlHelper.get_temp_start(start)
    return jsonify(json.loads(data.to_json(orient="records")))

# Start/End date API
@app.route("/api/v1.0/<start>/<end>")
def get_temp_dates(start, end):
    data = sqlHelper.get_temp_dates(start, end)
    return jsonify(json.loads(data.to_json(orient="records")))

if __name__ == "__main__":
    app.run(debug=True)