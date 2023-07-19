from machine import ADC, Pin
import utime

desiredVoltage_adc = ADC(Pin(28)) #should be coupled with 100nF or 1uF on the ADC input to ground.
voltageChangePin = Pin(19,Pin.IN)
desiredVoltage =0; #value of the desired voltage
#####
def getDesiredVoltage(): #calculates desired voltage based on signal received from the host
    dv_reading = desiredVoltage_adc.read_u16() #the reading after the adc
    print("dv_reading: " + str(dv_reading))
    if dv_reading >= 8276:
        desiredVoltage = 18* dv_reading/57594;
        print("desired voltage: " + str(desiredVoltage))
    else: print("can't provide voltage less than 2.5v")
#####

getterPin = Pin(22, Pin.IN)
outputVoltagePin = Pin(21, Pin.OUT)
enderPin = Pin(20, Pin.OUT)
outputVoltage = 750;

def sendOutputVoltage():
    print("output voltage stream start")
    index = 0;
    #algorithm to make output voltage in binary
    outputVoltageDigital = list(map(int, bin(int(outputVoltage))[2:]))
    while index<len(outputVoltageDigital):
        if getterPin.value() == 1:
            outputVoltagePin.value(outputVoltageDigital[index])
            print(outputVoltagePin.value())
            index = index +1;       
    enderPin.value(1)
    print("output voltage stream end")
    utime.sleep(0.1)
    enderPin.value(0)



while True:
    if voltageChangePin.value()==1:
        getDesiredVoltage()
    if getterPin.value() == 1:
        sendOutputVoltage()
    utime.sleep(0.1)


