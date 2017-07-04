#File for servo motor actions
import RPi.GPIO as GPIO
import time
GPIO.setwarnings(False)

ZEROPOSITION = 13.4

class servoMotor():
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
	self.servo.start(0)
        self.zeroPosition() #Set position to zero at start

    def turnLeft(self, steps): #Turn left with .. steps.
        self.servo.ChangeDutyCycle(ZEROPOSITION - steps)

    def turnRight(self, steps): #Turn right with .. steps.
        self.servo.ChangeDutyCycle(ZEROPOSITION + steps)

    def zeroPosition(self): #set position to 0 .. steps.
        self.servo.ChangeDutyCycle(ZEROPOSITION)
        self.steps = ZEROPOSITION
