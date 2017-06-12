from dcMotor import dcMotor

from servoMotor import servoMotor
from sonicSensor import sonicSensor
motor = dcMotor()
servo = servoMotor()
sensor = sonicSensor()
motor.setSpeed(14.4)
while True:
	if sensor.isNearObject():
		motor.setZero()
	else:
		motor.setSpeed(14.4)
