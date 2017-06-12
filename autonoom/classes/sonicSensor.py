import RPi.GPIO as GPIO
import time
import threading

TRIG = 23
ECHO = 24
pulse_end = 0
pulse_start = 0

class sonicSensor(threading.Thread):
    class __sonicSensor(threading.Thread):
        def __init__(self):
            self.distance = 0
            self.MAXDISTANCE = 90
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.setup(ECHO, GPIO.IN)

        def __del__(self):
            GPIO.cleanup()

        def isNearObject(self):
            GPIO.output(TRIG, False)

            time.sleep(0.5)
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
	    self.distance = distance
            if distance < self.MAXDISTANCE:
                return True
            else:
                return False

            #If something went wrong return false
            return False

    instance = None

    def __new__(cls):  # __new__ always a classmethod
        if not sonicSensor.instance:
            sonicSensor.instance = sonicSensor.__sonicSensor()
        return sonicSensor.instance
