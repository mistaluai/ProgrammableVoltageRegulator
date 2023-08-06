import RPi.GPIO as GPIO
from time import sleep
import sys

## get values from command line
pwmPin = int(sys.argv[1])
f = int(sys.argv[2])
duty_cycle = float(sys.argv[3])


GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)
GPIO.setup(pwmPin,GPIO.OUT)
GPIO.setwarnings(False)
#start pwm
pwm = GPIO.PWM(pwmPin,f)
pwm.start(duty_cycle);
print(str(f) + " " + str(duty_cycle))
input()
