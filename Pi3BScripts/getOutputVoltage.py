import RPi.GPIO as GPIO
from time import sleep
import sys

readerPin = 11
isReadyForNextPin = 13
isReceivingPin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(isReadyForNextPin,GPIO.OUT)
GPIO.setup(readerPin, GPIO.IN)
GPIO.setup(isReceivingPin, GPIO.IN)
GPIO.setwarnings(False)

outputVoltage = [0,0,0,0,0]

for i in range(0,5):
	while GPIO.input(readerPin) == 0:
		GPIO.output(isReadyForNextPin,1)

	if GPIO.input(readerPin) == 1:
		outputVoltage[i] = GPIO.input(readerPin)
		print(GPIO.input(readerPin))
		
	GPIO.output(isReadyForNextPin,0)
	sleep(0.01)

GPIO.output(isReadyForNextPin,0)

