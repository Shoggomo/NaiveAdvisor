from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)


@app.route('/weights')
def weights():
    data = {"Service": 1/6., "Cleanliness": 1/6., "Value": 1/6., "Sleep Quality": 1/6., "Rooms": 1/6., "Location": 1/6.} # mockdata
    return json.dumps(data)


@app.route('/classify', methods=['POST'])
def classify():
    service = request.form['service']
    cleanliness = request.form['cleanliness']
    value = request.form['value']
    sleep_quality = request.form['sleep-quality']
    rooms = request.form['rooms']
    location = request.form['location']
    # classify(service, ...)
    return "3.4" # mockdata

app.run(port=5000)
