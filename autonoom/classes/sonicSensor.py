import RPi.GPIO as GPIO
import time

TRIG = 23
ECHO = 24

class sonicSensor:
    def __init__(self):
        self.distance = 0
        self.MAXDISTANCE = 15
        GPIO.setmode(GPIO.BCM)



    def isNearObject(self):
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)

        GPIO.output(TRIG, False)
        print("Waiting for sensor to settle")
        time.sleep(2)
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

        GPIO.cleanup
        if distance < self.MAXDISTANCE:
            return True
        else:
            return False
        #If something went wrong return false
        return False
