# import all classes
from classes.comProt import comProt
from classes.dcMotor import dcMotor
from classes.servoMotor import servoMotor

STANDARDSPEEDFORWARD = 14.1
STANDARDSPEEDBACKWARD = 9.3


# core class
class core():
    def __init__(self):
        # create objects
        self.comProt = comProt(5005)  # Give port number to object
        self.servoMotor = servoMotor(18)  # PWM pin for the servo is 18
        self.dcMotor = dcMotor(13)  # PWM pin for the engine is 13
        self.firstExecution = False

    def goForward(self):
        self.dcMotor.setSpeed(STANDARDSPEEDFORWARD)  # Call setSpeed

    def goBackward(self):
        self.dcMotor.setSpeed(STANDARDSPEEDBACKWARD)  # Call setSpeed

    def goStop(self):
        self.dcMotor.setZero()  # Call setZero

    def getInstruction(self):
        return self.comProt.getData()  # Call getData on ComProt

    def executeInstruction(self, instruction):
        if self.firstExecution is False:  # If no start signal is sent from the PC, dont do anything
            if instruction == "start":
                self.firstExecution = True
            else:
                print "Waiting for start signal!"
        else:
            if instruction != "stop":  # Else, if the instruction is not stop. Take instructions
                self.goForward()
                try:
                    data = float(instruction)  # Float conversion of data
                    if (data > 0):
                        self.servoMotor.turnRight(data)  # Data higher than 0 steer right
                    elif (data == 0):
                        self.servoMotor.zeroPosition()  # Data 0 zeroposition
                    elif (data < 0):
                        self.servoMotor.turnLeft(-(data))  # Data lower than 0 steer left
                    else:
                        pass
                except ValueError:  # Error catching.
                    pass
            else:
                self.goStop()  # If command is stop, stop and go into firstExecution loop
                self.firstExecution = False


if __name__ == '__main__':
    main = core()  # Call the core
    previousData = 0  # This prevents console spam
    while True:
        data = main.getInstruction()  # Get instruction
        if data is not None:  # If instruction is not null or previousData
            if data is not previousData:
                previousData = data
                print("Data is " + str(data))  # Print the data
            main.executeInstruction(data)  # Execute command if data is not none
