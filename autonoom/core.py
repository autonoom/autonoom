import threading

from classes.dcMotor import dcMotor
from classes.comProt import comProt
from classes.servoMotor import servoMotor
from classes.sonicSensor import sonicSensor
from classes.flask.cam import cam

STANDARDSPEEDFORWARD = 15.7
STANDARDSPEEDBACKWARD = 9.8

class core(threading.Thread):
    def __init__(self):
        self.comProt = comProt()
        self.servoMotor = servoMotor()
        self.sonicSensor = sonicSensor()
        self.dcMotor = dcMotor()
        cam() # Just call it.
        self.goForward()
        threading.Thread.__init__(self)
        self.start()

    def run(self):
        while True:
            if self.comProt.data == 'test':
                print 'test'

    def goForward(self):
        self.dcMotor.setSpeed(STANDARDSPEEDFORWARD)

    def goBackward(self):
        self.dcMotor.setSpeed(STANDARDSPEEDBACKWARD)

    def goStop(self):
        self.dcMotor.setZero() #Full stop

if __name__ == '__main__':
    main = core()
