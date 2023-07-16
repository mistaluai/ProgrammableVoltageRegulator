from machine import ADC, Pin
import utime

desiredVoltage_adc = ADC(Pin(28)) #should be coupled with 100nF or 1uF on the ADC input to ground.
desiredVoltage =0;
def getDesiredVoltage(): #calculates desired voltage based on signal received from the host
    dv_reading = desiredVoltage_adc.read_u16()
    print("dv_reading: " + str(dv_reading))
    if dv_reading >= 9102:
        desiredVoltage = 18* dv_reading/65535;
        print("desired voltage: " + str(desiredVoltage))
    else: print("can't provide voltage less than 2.5v")

while True:
    getDesiredVoltage()
    utime.sleep(1)
