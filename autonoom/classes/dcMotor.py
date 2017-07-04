# File for DC motor actions
import RPi.GPIO as GPIO

GPIO.setwarnings(False)
ZEROSPEED = 12.6


class dcMotor():
    def __init__(self, motorPin):
        self.motorPin = motorPin
        # Setup GPIO
        # Broadcom SOCKET channel is used as standard
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.motorPin, GPIO.OUT)
        # Setup PWM with 100KHz
        self.motor = GPIO.PWM(self.motorPin, 100)
        # Start PWM
        self.motor.start(0)
        # Start on speed zero
        self.setZero()

    def __del__(self):
        GPIO.cleanup()

    def setSpeed(self, speed):
        self.motor.ChangeDutyCycle(speed)

    def setZero(self):  # Set the speed to zero.
        self.setSpeed(ZEROSPEED)
