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

twoPower =0;
decimal = 0;



	


