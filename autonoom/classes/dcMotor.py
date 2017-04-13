#File for DC motor actions
from sonicSensor import sonicSensor
import threading
import time

class dcMotor(threading.Thread):
    speed = 0
    direction = 0
    def __init__(self):
        self.speed = 0
        self.direction = 0
        self.setSpeed(self.speed) #Set initial speed to 0, else the car would start driving right away.
        self.sonicSensor = sonicSensor()
        self.start()

    def run(self):
        while True:
            time.sleep(1)
            if self.sonicSensor.isNearObject():
                self.setSpeed(0) #Emergency stop
            else:
                self.setSpeed(self.speed) #return to previous speed


    def setSpeed(self, speed):
        #Formula for speed to actual ms, check which direction the application is set to as well
        self.speed = speed

    def setDirection(self, direction):
        self.direction = direction


