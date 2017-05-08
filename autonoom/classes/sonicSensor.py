import RPi.GPIO as GPIO
import time

#Constants
TRIG = 23
ECHO = 24

class sonicSensor:
    def __init__(self):
        self.MAXDISTANCE = 15
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(TRIG, GPIO.OUT)
        GPIO.setup(ECHO, GPIO.IN)


    def isNearObject(self):
        # set Trigger to HIGH
        GPIO.output(TRIG, True)

        # set Trigger after 0.01ms to LOW
        time.sleep(0.00001)
        GPIO.output(TRIG, False)

        StartTime = time.time()
        StopTime = time.time()

        # save StartTime
        while GPIO.input(ECHO) == 0:
            StartTime = time.time()

        # save time of arrival
        while GPIO.input(ECHO) == 1:
            StopTime = time.time()

        # time difference between start and arrival
        TimeElapsed = StopTime - StartTime
        # multiply with the sonic speed (34300 cm/s)
        # and divide by 2, because there and back
        distance = (TimeElapsed * 34300) / 2

        if distance < 15.0:
            return True
        else:
            return False

        return False
