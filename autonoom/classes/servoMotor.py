#File for servo motor actions
import threading
import RPi.GPIO as GPIO
import time

class servoMotor(threading.Thread):
        def __init__(self, servoPin):
            self.position = 0
            self.steps = 0
            self.servoPin = servoPin
            # Setup GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.servoPin, GPIO.OUT)
            # Setup PWM with 100KHz
            self.servo = GPIO.PWM(self.servoPin, 100)
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


