from Sensor import Sensor


class CU:
    sensor1 = None

    def __init__(self):
        if (CU.sensor1 == None):
            self.__create()
        else:
            print "bestaat al"



    def __create(self):
        if(CU.sensor1 == None):
            CU.sensor1 = Sensor()

    def Checkvalue(self):
        print CU.sensor1

