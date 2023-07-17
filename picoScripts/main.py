from machine import ADC, Pin
import utime

desiredVoltage_adc = ADC(Pin(28)) #should be coupled with 100nF or 1uF on the ADC input to ground.
desiredVoltage =0; #value of the desired voltage
#####
def getDesiredVoltage(): #calculates desired voltage based on signal received from the host
    dv_reading = desiredVoltage_adc.read_u16() #the reading after the adc
    print("dv_reading: " + str(dv_reading))
    if dv_reading >= 9102:
        desiredVoltage = 18* dv_reading/65535;
        print("desired voltage: " + str(desiredVoltage))
    else: print("can't provide voltage less than 2.5v")
#####

isReadyForNext = Pin(22, Pin.IN)
outputVoltagePin = Pin(21, Pin.OUT)
isSendingPin = Pin(20,Pin.OUT)
outputVoltage = 0;

def sendOutputVoltage():
    outputVoltageDigital = [0,0,0,0,0]
    #algorithm to make output voltage in binary
    outputVoltageDigital = [1,0,0,1,0]
    for i in outputVoltageDigital:
        
       if isReadyForNext.value()==1:
        isSendingPin.value(1)

    outputVoltagePin.value(i) #feeds bit to the pin
    print(i)
    isSendingPin.value(0)
    utime.sleep(0.01)



while True:
    getDesiredVoltage()
    sendOutputVoltage()
    utime.sleep(1)
