from flask import Flask, request
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)
supervisor = None


@app.route('/weights')
def weights():
    data = {"Service": 1/6., "Cleanliness": 1/6., "Value": 1/6., "Sleep Quality": 1/6., "Rooms": 1/6., "Location": 1/6.} # mockdata
    # data = supervisor.get_statistics()
    return json.dumps(data)


@app.route('/classify')
def classify():
    # Arguments must be: Service, Cleanliness, Value, Sleep Quality, Location, Rooms
    features = {category: int(request.args[category]) for category in request.args}
    return supervisor.classify(features)


def run(_supervisor):
    global supervisor
    supervisor = _supervisor
    app.run(port=5000)
