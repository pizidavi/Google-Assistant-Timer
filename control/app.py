from json import load
from flask import Flask, request, jsonify
from control.control import Control

app = Flask(__name__)
config = load(open('config.json', 'r'))


@app.route('/trigger/', methods=['POST'])
def trigger_post(action=None):
    data = request.get_json(force=True)

    key = data['key'] if 'key' in data else None
    durationInMinutes = data['durationInMinutes'] if 'durationInMinutes' in data else None
    deviceName = data['deviceName'] if 'deviceName' in data else None
    targetState = data['targetState'] if 'targetState' in data else False

    if (key is None) or (durationInMinutes is None) or (deviceName is None):
        return jsonify({
            "statusCode": 400,
            "message": "Missing data"
        }), 400

    if key != config['SECURITY_KEY']:
        return jsonify({
            "statusCode": 403,
            "message": "Unauthorised"
        }), 403

    print("New action ({}) on {} in {} minutes".format(('on' if targetState else 'off'), deviceName, durationInMinutes))

    durationInSeconds = int(durationInMinutes) * 60
    control = Control(deviceName, config['IFTTT'])

    if targetState:
        control.off_to_on(durationInSeconds)

    elif not targetState:
        control.on_to_off(durationInSeconds)

    else:
        return jsonify({
            "statusCode": 400,
            "message": "Wrong 'targetState' option"
        }), 400

    return jsonify({
        "statusCode": 200
    })


@app.route('/trigger/', methods=['GET'])
def trigger_get(action=None):
    return jsonify({
        "statusCode": 400,
        "message": "Wrong method"
    })


@app.route('/')
def index():
    return '<h1 style="position:relative;top:45%;text-align:center;">GA Timer is working!</h1>'
