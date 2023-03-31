from flask import Flask, request
from flask import render_template
import RPi.GPIO as rpi
import time

app = Flask(__name__)

led_pins = [3, 5, 7]
led_states = [False, False, False]

rpi.setwarnings(False)
rpi.setmode(rpi.BOARD)
for led_pin in led_pins:
    rpi.setup(led_pin, rpi.OUT)
    rpi.output(led_pin, 0)
print("Done")

@app.route('/')
def index():
    global led_states
    return render_template('index.html', led_states=led_states)

@app.route('/led/<int:led_id>/<state>')
def led_control(led_id, state):
    global led_states
    if state == "on":
        rpi.output(led_pins[led_id-1], 1)
        led_states[led_id-1] = True
    else:
        rpi.output(led_pins[led_id-1], 0)
        led_states[led_id-1] = False
    return "OK"

if __name__ == "__main__":
    print("Start")
    app.run(debug=True, host='172.29.95.233')

