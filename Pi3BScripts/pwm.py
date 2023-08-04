import RPi.GPIO as GPIO
from time import sleep
import sys

## get values from command line
pwmPin = int(sys.argv[1])
f = int(sys.argv[2])
duty_cycle = float(sys.argv[3])
notifier_pin = int(sys.argv[4]) #zero for none
stop = int(sys.argv[5])

#set gpio modes
GPIO.setmode(GPIO.BOARD)
GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setup(notifier_pin,GPIO.OUT)
GPIO.setwarnings(False)

#start pwm
pwm = GPIO.PWM(pwmPin,f)
pwm.start(duty_cycle);

GPIO.output(notifier_pin,1)
sleep(0.1)
GPIO.output(notifier_pin,0)
if stop == 1:
	pwm.stop()

input()
