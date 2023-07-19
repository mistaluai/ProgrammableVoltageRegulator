import RPi.GPIO as GPIO
from time import sleep
import sys

## get values from command line
pwmPin = 33
f = 1000
duty_cycle = int(sys.argv[1])
notifier_pin = 31

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