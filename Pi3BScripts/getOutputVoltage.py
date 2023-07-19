import RPi.GPIO as GPIO
from time import sleep
import sys

readerPin = 11
getPin = 13
endListenerPin = 15
GPIO.setmode(GPIO.BOARD)
GPIO.setup(getPin,GPIO.OUT)
GPIO.setup(readerPin, GPIO.IN)
GPIO.setup(endListenerPin, GPIO.IN)
GPIO.setwarnings(False)

GPIO.output(getPin,1)
sleep(0.1)
GPIO.output(getPin,0)
outputVoltage = [0,0,0,0,0,0,0,0,0,0]
twoPower = 0;
decimal = 0;
while GPIO.input(endListenerPin)!=1:
	print(GPIO.input(readerPin))
	outputVoltage[twoPower] = GPIO.input(readerPin)
	decimal += 2**twoPower * GPIO.input(readerPin)
	twoPower += 1;
	GPIO.output(getPin,1)
	sleep(0.1)
	GPIO.output(getPin,0)

print(decimal)





