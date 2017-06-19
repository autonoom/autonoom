# File for DC motor actions
import threading
import RPi.GPIO as GPIO
import time
from sonicSensor import sonicSensor

ZEROSPEED = 13.2

class dcMotor(threading.Thread):
        def __init__(self, motorPin):
            self.speed = 0
            self.motorPin = motorPin
            #Setup GPIO
            #Broadcom SOCKET channel is used as standard 
            GPIO.setmode(GPIO.BCM)
            GPIO.setup(self.motorPin, GPIO.OUT)
            #Setup PWM with 100KHz
            self.motor = GPIO.PWM(self.motorPin, 100)
            #Start PWM
            self.motor.start(5)
            #Implement sonicSensor class
            #Start on speed zero
            self.setZero()
            threading.Thread.__init__(self)
            self.start() #Start thread

        def __del__(self):
            GPIO.cleanup()

        def setSpeed(self, speed):
            self.motor.ChangeDutyCycle(speed)
            self.speed = speed

        def setZero(self): #Set the speed to zero.
	    self.setSpeed(11.7)
