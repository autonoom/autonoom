import threading
import time

#import all classes
from classes.dcMotor import dcMotor
from classes.comProt import comProt
from classes.servoMotor import servoMotor


STANDARDSPEEDFORWARD = 13.9
STANDARDSPEEDBACKWARD = 9.3

#core class
class core():
    def __init__(self):
        #create objects
        self.comProt = comProt(5005) #Give port number to object
        self.servoMotor = servoMotor(18) #PWM pin for the servo is 18
        self.dcMotor = dcMotor(13) #PWM pin for the engine is 13
        self.stopFlag = False
        #initialize thread
        threading.Thread.__init__(self)

    def goForward(self):
        self.dcMotor.setSpeed(STANDARDSPEEDFORWARD) #Call setSpeed

    def goBackward(self):
        self.dcMotor.setSpeed(STANDARDSPEEDBACKWARD) #Call setSpeed

    def goStop(self):
        self.dcMotor.setZero()  #Call setZero

    def getInstruction(self):
        return self.comProt.getData()

    def executeInstruction(self, instruction):
        if instruction == 'stop':
            self.goStop()
        elif instruction == 'start':
            self.goForward()
        else:
            try:
                data = float(instruction)
                if (data > 0):
                    self.servoMotor.turnRight(data)
                elif (data == 0):
                    self.servoMotor.zeroPosition()
                elif (data < 0):
                    self.servoMotor.turnLeft(-(data))
                else:
                    pass
            except ValueError:
                print "not a good value"



if __name__ == '__main__':
    main = core()
    while True:
        data = main.getInstruction()
        if data is not None:
            main.executeInstruction(data)
