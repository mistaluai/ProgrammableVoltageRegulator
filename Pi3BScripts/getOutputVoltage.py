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
sleep(0.05)
GPIO.output(getPin,0)

outputVoltage = []
index = 0;
while GPIO.input(endListenerPin)!=1:
	outputVoltage.append(GPIO.input(readerPin))
	#print(GPIO.input(readerPin))
	index += 1;
	sleep(0.05)
print(outputVoltage)
weight = len(outputVoltage);
dec = 0;
for i in outputVoltage:
	dec += i * 2**weight
	weight -= 1;
dec/=100;
print(dec)



