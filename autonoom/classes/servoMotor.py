# File for servo motor actions
import RPi.GPIO as GPIO

GPIO.setwarnings(False)

ZEROPOSITION = 13.4


class servoMotor():
    def __init__(self, servoPin):
        self.servoPin = servoPin
        # Setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.servoPin, GPIO.OUT)
        # Setup PWM with 100KHz
        self.servo = GPIO.PWM(self.servoPin, 100)
        # Start PWM with dutycycle of 0%
        self.servo.start(0)
        self.zeroPosition()  # Set position to zero at start

    def turnLeft(self, steps):  # Turn left with .. dutycycle %.
        self.servo.ChangeDutyCycle(ZEROPOSITION - steps)

    def turnRight(self, steps):  # Turn right with .. dutycycle %.
        self.servo.ChangeDutyCycle(ZEROPOSITION + steps)

    def zeroPosition(self):  # set position to 0 .. dutycycle %.
        self.servo.ChangeDutyCycle(ZEROPOSITION)
