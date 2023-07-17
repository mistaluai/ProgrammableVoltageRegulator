import RPi.GPIO as GPIO
from time import sleep
import sys

readerPin = 11
getPin = 13
GPIO.setmode(GPIO.BOARD)
GPIO.setup(getPin,GPIO.OUT)
GPIO.setup(readerPin, GPIO.IN)
GPIO.setwarnings(False)

GPIO.output(getPin,1)
sleep(0.1)
GPIO.output(getPin,0)
outputVoltage = [0,0,0,0,0]

for i in range(0,5):
	GPIO.output(getPin,1)
	sleep(0.1)
	GPIO.output(getPin,0)
	print(GPIO.input(readerPin))
	outputVoltage[i] = GPIO.input(readerPin)




