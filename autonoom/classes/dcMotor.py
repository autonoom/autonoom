#File for DC motor actions
import threading
import RPi.GPIO as GPIO
import time

MOTOR = 18


class dcMotor(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.speed = 11.5
        self.direction = 0
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(MOTOR, GPIO.OUT)
        self.motor = GPIO.PWM(MOTOR, 100)
        self.motor.start(0)
        self.setSpeed(self.speed) #Set initial speed to 0, else the car would start driving right away.

    def __del__(self):
        GPIO.cleanup()

    def setSpeed(self, speed):
        #Formula for speed to actual ms, check which direction the application is set to as well
        self.motor.changeDutyCycle(speed)
        self.speed = speed


