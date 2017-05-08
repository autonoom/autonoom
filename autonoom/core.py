from classes.dcMotor import dcMotor
from classes.servoMotor import servoMotor
from classes.sonicSensor import sonicSensor

class core:
    #core functions go here
    def __init__(self):
        self.dcMotor = dcMotor()
        self.servoMotor = servoMotor()
        self.sonicSensor = sonicSensor()
        self.standardSpeed = 10 #Standard speed? Put in UML?

    def decideAction(self):


    def goForward(self):
        dcMotor.setDirection(1)
        dcMotor.setSpeed(self.standardSpeed)

    def goBackward(self):
        dcMotor.setDirection(0)
        dcMotor.setSpeed(self.standardSpeed)

    def goStop(self):
        dcMotor.setSpeed(0) #Full stop

    def goCorrect(self):

    def sendVideo(self):

    def createObjects(self):





if __name__ == '__main__':
    #Main