import threading
import time

#import all classes
from classes.dcMotor import dcMotor
from classes.comProt import comProt
from classes.servoMotor import servoMotor
from classes.sonicSensor import sonicSensor

#core class
class core(threading.Thread):
    def __init__(self):
        #create objects
        self.comProt = comProt(5005) #Give port number to object
        self.servoMotor = servoMotor(18) #PWM pin for the servo is 18
        self.sonicSensor = sonicSensor(23,24,60) #Trigger pin, Echo pin and maxdistance
        self.dcMotor = dcMotor(13) #PWM pin for the engine is 13
        #initialize thread
        threading.Thread.__init__(self)
        #start thread
        self.start()

    def run(self):
        #start with going forward
        self.goForward()
        while True:
            if self.comProt.data == 'stop': #if the telnet connection sends a stop signal. Stop
                self.goStop()
            if self.comProt.data == 'start': #if the telnet connection sends a start signal. Start
                self.goForward()
            if self.comProt.data is not None: #Output the data is its not NULL
                print "Received data = " + self.comProt.data

    def goForward(self):
        self.dcMotor.setSpeed(self.dcMotor.STANDARDSPEEDFORWARD) #Call setSpeed

    def goBackward(self):
        self.dcMotor.setSpeed(self.dcMotor.STANDARDSPEEDBACKWARD) #Call setSpeed

    def goStop(self):
        self.dcMotor.setZero()  #Call setZero


if __name__ == '__main__':
    #main = core() #Start the program
    sonicSensor1 = sonicSensor(23, 24, 60)  # Trigger pin, Echo pin and maxdistance
    while True:
        time.sleep(0.2)
    if sonicSensor1.isNearObject() is True:
        print sonicSensor1.giveDist()
    else:
        print "False"
