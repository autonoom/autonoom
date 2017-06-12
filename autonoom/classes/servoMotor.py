#File for servo motor actions
import threading
import RPi.GPIO as GPIO
import time

SERVO = 18

class servoMotor:
    class __servoMotor:
        def __init__(self):
            self.position = 0
            self.steps = 0
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(SERVO, GPIO.OUT)
            self.servo = GPIO.PWM(SERVO, 100)
            self.servo.start(5)
            self.zeroPosition() #Set position to zero at start

        def turnLeft(self, steps):
            self.steps -= steps
            self.servo.ChangeDutyCycle(self.steps)

        def turnRight(self, steps):
            self.steps += steps
            self.servo.ChangeDutyCycle(self.steps)

        def zeroPosition(self):
            zeroPosition = 13.4
            self.servo.ChangeDutyCycle(zeroPosition)
            self.steps = zeroPosition

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not servoMotor.instance:
            servoMotor.instance = servoMotor.__servoMotor()
        return servoMotor.instance



