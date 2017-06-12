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
            self.distance = 90 #Start at 90 so the engine doesnt stop right away
            self.MAXDISTANCE = 60  #Stop when 60 cm in front of object
            #setup GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(TRIG, GPIO.OUT)
            GPIO.setup(ECHO, GPIO.IN)

        def __del__(self):
            GPIO.cleanup()

        def isNearObject(self):
            #from https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
            while True:
                GPIO.output(TRIG, False)

                time.sleep(0.1)
                GPIO.output(TRIG, True)
                time.sleep(0.00001)
                GPIO.output(TRIG, False)

                while GPIO.input(ECHO) == 0:
                    pulse_start = time.time()

                while GPIO.input(ECHO) == 1:
                    pulse_end = time.time()

                pulse_duration = pulse_end - pulse_start
                dist = pulse_duration * 17150
                dist = round(dist, 2)
                self.distance = dist
                if dist < self.MAXDISTANCE: #If distance is closer than MAXDISTANCE return true.
                    return True
                else:
                    return False

    # From https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    instance = None

    # Singleton implementation
    def __new__(cls):  # __new__ always a classmethod
        if not sonicSensor.instance:
            sonicSensor.instance = sonicSensor.__sonicSensor()
        return sonicSensor.instance

