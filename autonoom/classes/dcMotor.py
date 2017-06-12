# File for DC motor actions
import threading
import RPi.GPIO as GPIO
import time
from sonicSensor import sonicSensor

MOTOR = 13 #MOTOR pin on the Pi


class dcMotor(threading.Thread):
    class __dcMotor(threading.Thread):
        def __init__(self):
            self.speed = 0
            #Constants that can be used outside of this class
            self.ZEROSPEED = 12.5
            self.STANDARDSPEEDFORWARD = 13.9
            self.STANDARDSPEEDBACKWARD = 9.7
            #Setup GPIO
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(MOTOR, GPIO.OUT)
            #Setup PWM with 100KHz
            self.motor = GPIO.PWM(MOTOR, 100)
            #Start PWM
            self.motor.start(5)
            #Implement sonicSensor class
            self.sonicSensor = sonicSensor()
            #Start on speed zero
            self.setZero()
            threading.Thread.__init__(self)
            self.start() #Start thread

        def run(self):
            while True:
                if self.sonicSensor.isNearObject():
                    self.setZero()
                    while self.sonicSensor.isNearObject():
                        time.sleep(0.5)
                    self.setSpeed(self.STANDARDSPEEDFORWARD)

        def __del__(self):
            GPIO.cleanup()

        def setSpeed(self, speed):
            # If sonicSensor distance is bigger than the required distance, then change the speed. Else, please dont.
            if self.sonicSensor.distance > self.sonicSensor.MAXDISTANCE:
                self.motor.ChangeDutyCycle(speed)
                self.speed = speed
            else:
                print "Cant do anything cause i am blocked by something"

        def setZero(self): #Set the speed to zero.
            self.motor.ChangeDutyCycle(self.ZEROSPEED)
            self.speed = self.ZEROSPEED

    # From https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
    instance = None

    # Singleton implementation
    def __new__(cls):  # __new__ always a classmethod
        if not dcMotor.instance:
            dcMotor.instance = dcMotor.__dcMotor()
        return dcMotor.instance
