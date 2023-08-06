import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import busio
import digitalio
import board
from time import sleep
import RPi.GPIO as GPIO
import sys


#global variables
desiredVoltage = 0
#analog variables
inputVoltage=0
outputVoltage=0
shuntVoltage = 0
current = 0
resistance =0
#constants
shunt_resistance = 10
inputVoltage_factor = 109/20
outputVoltage_factor = 27/7
#pid variables
Kp=0
Ki=0
Kd=0


class Embedded:
	def __init__(self):
		#Analog To Digital
		#create the spi bus
		spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
		print("SPI Bus created")
		# create the cs (chip select)
		cs = digitalio.DigitalInOut(board.D5)
		# create the mcp object
		mcp = MCP.MCP3008(spi, cs)
		print("MCP Object created")
		#channels definition
		CH_inputVoltage = AnalogIn(mcp, MCP.P1, MCP.P0)
		CH_outputVoltage = AnalogIn(mcp, MCP.P3, MCP.P2)
		CH_shuntVoltage = AnalogIn(mcp, MCP.P4, MCP.P5)
		print("Diffrential Channels Defined")
		#pwm initialization
		GPIO.setup(23,GPIO.OUT)
		GPIO.setwarnings(False)
		print("PWM Pins initialised")


	
	def getInputVoltage():
		inputVoltage = inputVoltage_factor * CH_inputVoltage.voltage()


	def getOutputVoltage():
		outputVoltage = outputVoltage_factor * CH_outputVoltage.voltage() - CH_shuntVoltage.voltage();

	def getCurrent():
		shuntVoltage = CH_shuntVoltage.voltage()
		current = shuntVoltage*100;

	def getResistance():
		if current != 0:
			resistance = outputVoltage/current
		else: resistance = 0

	def debugAnalogInput():
		print("about to call something")
		getInputVoltage()
		getOutputVoltage()
		getCurrent()
		getResistance()
		print("Input Voltage (V): " + str(inputVoltage) + "\nOutput Voltage (V): " + str(outputVoltage) + "\nShunt Voltage (V): " + str(shuntVoltage) + "\nTotal Current (mA): " + str(current) + "\nTotal Resistance (Ω): " + str(resistance))
	
	def pwmSignal(duty_cycle, frequency):
		pwm = GPIO.PWM(23,frequency)
		pwm.start(duty_cycle)

if __name__ == "__main__":
	embeddedObject = Embedded()
	f = int(input("enter f"))
	dc = int(input("enter dc"))
	embeddedObject.pwmSignal(5,20)
	while True:
		embeddedObject.debugAnalogInput()
		sleep(0.1)


