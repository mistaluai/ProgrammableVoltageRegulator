import RPi.GPIO as GPIO
from time import sleep
import sys

## get values from command line
pwmPin = int(sys.argv[1])
f = int(sys.argv[2])
duty_cycle = int(sys.argv[3])
stop = int(sys.argv[4])

#set gpio modes
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setwarnings(False)

#start pwm
pwm = GPIO.PWM(pwmPin,f)
pwm.start(duty_cycle);

sleep(0.1)

if stop == 1:
	pwm.stop()

input()
