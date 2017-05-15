from classes.dcMotor import dcMotor
from classes.servoMotor import servoMotor
from classes.sonicSensor import sonicSensor
import core
import threading
import time
class core(threading.Thread):
    def __init__(self):
        self.dcMotor = dcMotor()
        self.servoMotor = servoMotor()
        self.sonicSensor = sonicSensor()
        self.standardSpeedForward = 15.7 #Standard speed? Put in UML?
	self.standardSpeedBackward = 9.8
	threading.Thread.__init__(self)
	self.start()
	self.goForward()

    def run(self):
	while True:
		if self.sonicSensor.isNearObject():
			self.dcMotor.setZero()

    def goForward(self):
        self.dcMotor.setSpeed(self.standardSpeedForward)

    def goBackward(self):
        self.dcMotor.setSpeed(self.standardSpeedBackward)

    def goStop(self):
        self.dcMotor.setZero() #Full stop





if __name__ == '__main__':
	main = core()
	main.goForward()
	time.sleep(2)
	main.goStop()
