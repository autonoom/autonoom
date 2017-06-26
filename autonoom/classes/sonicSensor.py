import RPi.GPIO as GPIO
import time
import threading

TRIG = 23
ECHO = 24
pulse_end = 0
pulse_start = 0


class sonicSensor(threading.Thread):
    def __init__(self, trig, echo, maxdistance):
        self.distance = 90  # Start at 90 so the engine doesnt stop right away
        self.maxdistance = maxdistance  # Stop when 60 cm in front of object
        self.trig = trig
        self.echo = echo
        self.dangour_counter = 0
        # setup GPIO
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(self.trig, GPIO.OUT)
        GPIO.setup(self.echo, GPIO.IN)

    def __del__(self):
        GPIO.cleanup()

    def giveDist(self):
        return self.distance

    def isNearObject(self):
        # from https://www.modmypi.com/blog/hc-sr04-ultrasonic-range-sensor-on-the-raspberry-pi
        global pulse_end
        global pulse_start
        while True:
            GPIO.output(self.trig, False)

            time.sleep(0.1)
            GPIO.output(self.trig, True)
            time.sleep(0.00001)
            GPIO.output(self.trig, False)

            while GPIO.input(self.echo) == 0:
                pulse_start = time.time()

            while GPIO.input(self.echo) == 1:
                pulse_end = time.time()

            pulse_duration = pulse_end - pulse_start
            dist = pulse_duration * 17150
            dist = round(dist, 2)
            self.distance = dist
            self.dangour_counter = 0
            while self.dangour_counter < 3:
                if dist < self.maxdistance:  # If distance is closer than MAXDISTANCE return true.
                    self.dangour_counter += 1
                else:
                    break
            if self.dangour_counter is 3:
                return True
            else:
                return False
