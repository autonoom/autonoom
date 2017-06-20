import threading
import time

#import all classes
from classes.dcMotor import dcMotor
from classes.comProt import comProt
from classes.servoMotor import servoMotor
from classes.sonicSensor import sonicSensor


STANDARDSPEEDFORWARD = 14.5
STANDARDSPEEDBACKWARD = 9.3

#core class
class core(threading.Thread):
    def __init__(self):
        #create objects
        self.comProt = comProt(5005) #Give port number to object
        self.servoMotor = servoMotor(18) #PWM pin for the servo is 18
        self.sonicSensor = sonicSensor(23,24,60) #Trigger pin, Echo pin and maxdistance
        #self.dcMotor = dcMotor(13) #PWM pin for the engine is 13
        self.stopFlag = False
        #initialize thread
        threading.Thread.__init__(self)
        #start thread
        self.start()

    def run(self):
        while True:
            if self.sonicSensor.isNearObject():
                #self.goStop()
                if self.stopFlag is False:
                    #self.goBackward()
                    self.servoMotor.turnLeft(12)
                self.stopFlag = True
                #self.goStop()
            self.stopFlag = False
            #self.servoMotor.zeroPosition() kan niet


    # def goForward(self):
    #     if not self.sonicSensor.isNearObject():
    #         self.dcMotor.setSpeed(STANDARDSPEEDFORWARD) #Call setSpeed
    #
    # def goBackward(self):
    #     self.dcMotor.setSpeed(STANDARDSPEEDBACKWARD) #Call setSpeed
    #
    # def goStop(self):
    #     self.dcMotor.setZero()  #Call setZero


if __name__ == '__main__':
    main = core()
    # start with going forward
    #main.goForward()
    counter = 0
    counter2= 0
    data = 0
    data2 =0
    while True:
        if main.comProt.data == 'stop':  # if the telnet connection sends a stop signal. Stop
            main.goStop()
        if main.comProt.data == 'start':  # if the telnet connection sends a start signal. Start
            main.goForward()
        if main.comProt.data is not None:  # Output the data is its not NULL
            if counter < 10:
                counter +=1
                data += int(main.comProt.data)
            elif counter is 10:
                #avg from avg
                data = float(data) /100
                if counter2 < 5:
                    counter2 += 1
                    data2 += data
                elif counter is 5:
                    data2 = float(data2) / 5
                    if(float(data2) <= 0):
                        main.servoMotor.turnRight(data2)
                    else:
                        main.servoMotor.turnLeft(data2)
                    print "Avg data = " + str(data2)
                data = 0
                counter = 0
            else:
                print "Received data = " + main.comProt.data
        if main.comProt.data == 'zero':  # Output the data is its not NULL
            main.servoMotor.zeroPosition()
        if main.comProt.data == '5':  # Output the data is its not NULL
            main.servoMotor.turnLeft(5)