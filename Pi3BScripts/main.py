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
#pid variables
Kp=0
Ki=0
Kd=0
#constants
shunt_resistance = 10
inputVoltage_factor = 109/20
outputVoltage_factor = 27/7

class Embedded:
	#analog channels
	CH_inputVoltage = None
	CH_outputVoltage = None
	CH_shuntVoltage = None
	CH_pwmOUT = None
	CH_pwmIN = None
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
		self.CH_inputVoltage = AnalogIn(mcp, MCP.P1, MCP.P0)
		self.CH_outputVoltage = AnalogIn(mcp, MCP.P3, MCP.P2)
		self.CH_shuntVoltage = AnalogIn(mcp, MCP.P4, MCP.P5)
		print("Diffrential Channels Defined")
		#pwm initialization
		GPIO.setup(23,GPIO.OUT)
		GPIO.setwarnings(False)
		self.CH_pwmOUT = GPIO.PWM(23,20)
		self.CH_pwmOUT.start(0)
		print("PWM Pins initialised")


	
	def getInputVoltage(self):
		inputVoltage = inputVoltage_factor * self.CH_inputVoltage.voltage


	def getOutputVoltage(self):
		outputVoltage = outputVoltage_factor * self.CH_outputVoltage.voltage - self.CH_shuntVoltage.voltage;

	def getCurrent(self):
		shuntVoltage = self.CH_shuntVoltage.voltage
		current = shuntVoltage*100;

	def getResistance(self):
		if current != 0:
			resistance = outputVoltage/current
		else: resistance = 0

	def debugAnalogInput(self):
		print("about to call something")
		self.getInputVoltage()
		self.getOutputVoltage()
		self.getCurrent()
		self.getResistance()
		print("Input Voltage (V): " + str(inputVoltage) + "\nOutput Voltage (V): " + str(outputVoltage) + "\nShunt Voltage (V): " + str(shuntVoltage) + "\nTotal Current (mA): " + str(current) + "\nTotal Resistance (Ω): " + str(resistance))
	
	def pwmSignal(self, duty_cycle, frequency):
		self.CH_pwmOUT.ChangeFrequency(frequency)
		self.CH_pwmOUT.ChangeDutyCycle(duty_cycle)

if __name__ == "__main__":
	embeddedObject = Embedded()
	self.CH_pwmOUT.start(0)
	f = int(input("enter f"))
	dc = int(input("enter dc"))
	while True:
		embeddedObject.pwmSignal(dc,f)
		embeddedObject.debugAnalogInput()
		sleep(0.1)


