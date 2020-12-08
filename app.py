from flask import Flask, render_template
import RPi.GPIO as GPIO
from time import sleep

GPIO.setmode(GPIO.BOARD)
GPIO.setup(11,GPIO.OUT)
servo1 = GPIO.PWM(11,50)
servo1.start(0)

GPIO.setwarnings(False)

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/lightson')
def lightson():
    GPIO.output(11, True)
    servo1.ChangeDutyCycle(135/18 +2)
    sleep(2)
    servo1.ChangeDutyCycle(90/18 +2)
    sleep(2)
    servo1.ChangeDutyCycle(0)
    GPIO.output(11, False)
    return render_template('index.html')


@app.route('/lightsoff')
def lightsoff():
    GPIO.output(11, True)
    servo1.ChangeDutyCycle(90/18 +2)
    sleep(2)
    servo1.ChangeDutyCycle(45/18 +2)
    sleep(2)
    servo1.ChangeDutyCycle(0)
    GPIO.output(11, False)
    return render_template('index.html')


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80, debug=True)
