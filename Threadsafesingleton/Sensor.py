#http://python-3-patterns-idioms-test.readthedocs.io/en/latest/Singleton.html
class Sensor:
    class __Sensor:
        def __init__(self):
            self.val = None
        def __str__(self):
            return `self` + self.val
    instance = None
    def __new__(cls): # __new__ always a classmethod
        if not Sensor.instance:
            Sensor.instance = Sensor.__Sensor()
        return Sensor.instance
    # def __getattr__(self, name):
    #     return getattr(self.instance, name)
    # def __setattr__(self, name):
    #     return setattr(self.instance, name)
