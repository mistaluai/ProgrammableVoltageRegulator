import RPi.GPIO as GPIO
from time import sleep
import sys

readerPin = 11
isReadyForNextPin = 13

GPIO.setmode(GPIO.BOARD)
GPIO.setup(isReadyForNextPin,GPIO.OUT)
GPIO.setup(readerPin, GPIO.IN)
GPIO.setwarnings(False)

outputVoltage = [0,0,0,0,0]

for i in range(0,5):
	GPIO.output(isReadyForNextPin,0)
	outputVoltage[i] = GPIO.input(readerPin)
	print(GPIO.input(readerPin))
	GPIO.output(isReadyForNextPin,1)
	sleep(0.01)

GPIO.output(isReadyForNextPin,0)

