# File for DC motor actions
import threading
import RPi.GPIO as GPIO
import time
from sonicSensor import sonicSensor

MOTOR = 13


class dcMotor(threading.Thread):
    class __dcMotor(threading.Thread):
        def __init__(self):
            self.speed = 0
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(MOTOR, GPIO.OUT)
            self.motor = GPIO.PWM(MOTOR, 100)
            self.motor.start(5)
            self.sonicSensor = sonicSensor()
            self.setZero()
            threading.Thread.__init__(self)
            self.start()

        def run(self):
            if self.sonicSensor.isNearObject():
                self.setZero()
                time.sleep(0.1)

        def __del__(self):
            GPIO.cleanup()

        def setSpeed(self, speed):
            # Formula for speed to actual ms, check which direction the application is set to as well
            if self.sonicSensor.distance > self.sonicSensor.MAXDISTANCE:
                self.motor.ChangeDutyCycle(speed)
                self.speed = speed

        def setZero(self):
            zeroSpeed = 13.4
            self.setSpeed(zeroSpeed)

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not dcMotor.instance:
            dcMotor.instance = dcMotor.__dcMotor()
        return dcMotor.instance
