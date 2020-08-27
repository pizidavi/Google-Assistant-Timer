from json import load
from flask import Flask, request, jsonify
from control.control import Control

app = Flask(__name__)
config = load(open('config.json', 'r'))


@app.route('/trigger/<string:action>', methods=['POST'])
def trigger_post(action=None):
    data = request.get_json(force=True)

    key = data['key'] if 'key' in data else None
    durationInMinutes = data['durationInMinutes'] if 'durationInMinutes' in data else None
    deviceName = data['deviceName'] if 'deviceName' in data else None
    targetState = data['targetState'] if 'targetState' in data else None

    if action != 'on' and action != 'off':
        return jsonify({
            "statusCode": 400,
            "message": "Missing action"
        }), 400

    if (key is None) or (durationInMinutes is None) or (deviceName is None) or (targetState is None):
        return jsonify({
            "statusCode": 400,
            "message": "Missing data"
        }), 400

    if key != config['SECURITY_KEY']:
        return jsonify({
            "statusCode": 403,
            "message": "Unauthorised"
        }), 403
    print("New action ({}) on {} {} {} minutes".format(action, deviceName, targetState, durationInMinutes))

    durationInSeconds = int(durationInMinutes) * 60
    control = Control(deviceName, config['IFTTT'])

    if targetState:  # True -> After X minutes
        if action == 'on':
            control.on_after(durationInSeconds)
        elif action == 'off':
            control.off_after(durationInSeconds)

    elif not targetState:  # False -> For X minutes
        if action == 'on':
            control.on_for(durationInSeconds)
        elif action == 'off':
            control.off_for(durationInSeconds)

    else:
        return jsonify({
            "statusCode": 400,
            "message": "Wrong 'targetState' option"
        }), 400

    return jsonify({
        "statusCode": 200
    })


@app.route('/trigger/', methods=['GET'])
@app.route('/trigger/<string:action>', methods=['GET'])
def trigger_get(action=None):
    return jsonify({
        "statusCode": 400,
        "message": "Wrong method"
    })


@app.route('/')
def index():
    return '<h1 style="position:relative;top:45%;text-align:center;">GA Timer is working!</h1>'
