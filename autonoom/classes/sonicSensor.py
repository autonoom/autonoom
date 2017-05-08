import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

class sonicSensor:
    def __init__(self):
        self.distance = 0
        self.MAXDISTANCE = 15
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

    def __del__(self):
        GPIO.cleanup()

    def isNearObject(self):
        GPIO.output(TRIG, False)

        time.sleep(0.2)
        GPIO.output(TRIG, True)
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        while GPIO.input(ECHO) == 0:
            pulse_start = time.time()

        while GPIO.input(ECHO) == 1:
            pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        distance = pulse_duration * 17150
        distance = round(distance, 2)

        if distance < self.MAXDISTANCE:
            return True
        else:
            return False

        #If something went wrong return false
        return False