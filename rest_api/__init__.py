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
    categories = ['service', 'cleanliness', 'value', 'sleep-quality', 'rooms', 'location']
    features = {category: request.json[category] for category in categories}
    # classify(service, ...)
    return str(reduce(lambda pre, curr: pre + int(curr), features.values(), 0))  # mockdata

app.run(port=5000)
