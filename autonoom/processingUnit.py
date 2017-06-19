import threading
import time

#import all classes
from classes.dcMotor import dcMotor
from classes.comProt import comProt
from classes.servoMotor import servoMotor
from classes.sonicSensor import sonicSensor


STANDARDSPEEDFORWARD = 14.8
STANDARDSPEEDBACKWARD = 9.3

#core class
class core(threading.Thread):
    def __init__(self):
        #create objects
        self.comProt = comProt(5005) #Give port number to object
        self.servoMotor = servoMotor(18) #PWM pin for the servo is 18
        self.sonicSensor = sonicSensor(23,24,60) #Trigger pin, Echo pin and maxdistance
        self.dcMotor = dcMotor(13) #PWM pin for the engine is 13
        self.stopFlag = False
        #initialize thread
        threading.Thread.__init__(self)
        #start thread
        self.start()

    def run(self):
        while True:
            if self.sonicSensor.isNearObject():
               #self.dcMotor.setZero()
               if self.stopFlag is False:
                   #self.dcMotor.goBackward()
                   self.servoMotor.turnLeft(2)
               self.stopFlag = True
            self.stopFlag = False
            main.servoMotor.zeroPosition()


    def goForward(self):
        if not self.sonicSensor.isNearObject():
            self.dcMotor.setSpeed(STANDARDSPEEDFORWARD) #Call setSpeed

    def goBackward(self):
        self.dcMotor.setSpeed(STANDARDSPEEDBACKWARD) #Call setSpeed

    def goStop(self):
        self.dcMotor.setZero()  #Call setZero


if __name__ == '__main__':
    main = core()
    # start with going forward
    #main.goForward()
    while True:
        if main.comProt.data == 'stop':  # if the telnet connection sends a stop signal. Stop
            #main.goStop()
        if main.comProt.data == 'start':  # if the telnet connection sends a start signal. Start
            #main.goForward()
            main.servoMotor.zeroPosition()
        if main.comProt.data is not None:  # Output the data is its not NULL
            print "Received data = " + main.comProt.data