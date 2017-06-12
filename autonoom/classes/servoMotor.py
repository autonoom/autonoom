#File for servo motor actions
import threading
import RPi.GPIO as GPIO
import time

SERVO = 18

class servoMotor(threading.Thread):
    class __servoMotor:
        def __init__(self):
            self.position = 0
            self.steps = 0
            # Setup GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(SERVO, GPIO.OUT)
            # Setup PWM with 100KHz
            self.servo = GPIO.PWM(SERVO, 100)
            # Start PWM
            self.servo.start(5)
            self.zeroPosition() #Set position to zero at start

        def turnLeft(self, steps): #Turn left with .. steps.
            self.steps -= steps
            self.servo.ChangeDutyCycle(self.steps)

        def turnRight(self, steps): #Turn right with .. steps.
            self.steps += steps
            self.servo.ChangeDutyCycle(self.steps)

        def zeroPosition(self): #set position to 0 .. steps.
            zeroPosition = 13.4
            self.servo.ChangeDutyCycle(zeroPosition)
            self.steps = zeroPosition

    # From https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    instance = None

    # Singleton implementation
    def __new__(cls):  # __new__ always a classmethod
        if not servoMotor.instance:
            servoMotor.instance = servoMotor.__servoMotor()
        return servoMotor.instance



