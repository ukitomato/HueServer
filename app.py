from flask import Flask, jsonify, request
from phue import Bridge

bridge = Bridge('192.168.1.101')
bridge.connect()
bridge.get_api()

lights = bridge.lights

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'My Hue API!'


@app.route('/api/lights/<int:index>', methods=['GET', 'POST'])
def lights(index):
    light = bridge.lights[index]
    switch = request.args.get('switch', None)
    brightness = request.args.get('brightness', None)
    color_temperature = request.args.get('color_temperature', None)
    if switch is not None:
        light.on = (switch == 'on')
    if brightness is not None:
        light.brightness = int(brightness)
    if color_temperature is not None:
        light.colortemp = int(color_temperature)
    return jsonify(
        {'index': index, 'switch': switch, 'brightness': brightness, 'color_temperature': color_temperature})


if __name__ == '__main__':
    app.run()
