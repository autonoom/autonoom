# File for DC motor actions
import threading
import RPi.GPIO as GPIO
import time

MOTOR = 13


class dcMotor(threading.Thread):
    class __dcMotor(threading.Thread):
        def __init__(self):
            self.speed = 0
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(MOTOR, GPIO.OUT)
            self.motor = GPIO.PWM(MOTOR, 100)
            self.motor.start(5)
            self.setZero()

        def __del__(self):
            GPIO.cleanup()

        def setSpeed(self, speed):
            # Formula for speed to actual ms, check which direction the application is set to as well
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
