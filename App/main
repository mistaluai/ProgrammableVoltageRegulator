import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import busio
import digitalio
import board
from time import sleep
import RPi.GPIO as GPIO
import sys
import subprocess
import matplotlib.pyplot as plt
#ui and gtk
import gi
gi.require_version("Gtk", "3.0")
from gi.repository import Gtk
UI_FILE="UI.xml"

# global variables
desiredVoltage = 0
# analog variables
inputVoltage = 0
outputVoltage = 0
shuntVoltage = 0
current = 0
resistance = 0
# pid variables
Kp = 0
Ki = 0
Kd = 0
# constants
shunt_resistance = 10
inputVoltage_factor = 109 / 20
outputVoltage_factor = 52/7

class UI:
    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)
        
        self.window = self.builder.get_object("window")
        self.window_label = self.builder.get_object("Controller")
        self.updateOutputVoltage(20)
        self.window.show_all()
        
    def button_clicked(self,Apply):
        self.Entry = self.builder.get_object("Entry")
        self.Vout = float(self.Entry.get_text())
        print (self.Vout)
        
        
        
        
        self.Current=self.builder.get_object("Current")
        self.Current.set_text(str(1))
        
        self.power_consumption=self.builder.get_object("power_consumption")
        self.power_consumption.set_text(str(3))

    def updateOutputVoltage(self, outputVoltage):
        self.Vout1=self.builder.get_object("V_out")
        self.Vout1.set_text(str(outputVoltage) + "v")
        
    def windows_destroy(self,window):
        Gtk.main_quit()
            
    def main(self):
        Gtk.main()


class Embedded:
    # analog channels
    CH_inputVoltage = None
    CH_outputVoltage = None
    CH_shuntVoltage = None
    CH_pwmIN = None

    def __init__(self):
        # Analog To Digital
        # create the spi bus
        spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        print("SPI Bus created")
        # create the cs (chip select)
        cs = digitalio.DigitalInOut(board.D5)
        # create the mcp object
        mcp = MCP.MCP3008(spi, cs)
        print("MCP Object created")
        # channels definition
        self.CH_inputVoltage = AnalogIn(mcp, MCP.P3, MCP.P2)
        self.CH_outputVoltage = AnalogIn(mcp, MCP.P1, MCP.P0)
        self.CH_shuntVoltage = AnalogIn(mcp, MCP.P4, MCP.P5)
        self.CH_pwmIN = AnalogIn(mcp, MCP.P6)
        print("Diffrential Channels Defined")
        # board
        GPIO.setmode(GPIO.BCM)

    def getInputVoltage(self):
        inputVoltage = inputVoltage_factor * self.CH_inputVoltage.voltage

    def getOutputVoltage(self):
        outputVoltage = outputVoltage_factor * self.CH_outputVoltage.voltage - self.CH_shuntVoltage.voltage;

    def getCurrent(self):
        shuntVoltage = self.CH_shuntVoltage.voltage
        current = shuntVoltage * 100;

    def getResistance(self):
        if current != 0:
            resistance = outputVoltage / current
        else:
            resistance = 0

    def debugAnalogInput(self):
        print("about to call something")
        self.getInputVoltage()
        self.getOutputVoltage()
        self.getCurrent()
        self.getResistance()
        print("Input Voltage (V): " + str(inputVoltage) + "\nOutput Voltage (V): " + str(
            outputVoltage) + "\nShunt Voltage (V): " + str(shuntVoltage) + "\nTotal Current (mA): " + str(
            current) + "\nTotal Resistance (Ω): " + str(resistance))

    currentCycle = 0
    currentFrequency = 0;

    def pwmSignal(self, duty_cycle, frequency):
        if self.currentFrequency != frequency or self.currentCycle != duty_cycle:
            self.disablePWM()
            self.enablePWM(duty_cycle, frequency)
            print("changes done")

    def disablePWM(self):
        try:
            subprocess.call(["pkill", "-f", "pwm.py"])
        except:
            pass

    def enablePWM(self, duty_cycle, frequency):
        pwmScript = subprocess.Popen(
            ["python", "/home/proj/Documents/embproj/Pi3BScripts/pwm.py", "23", str(frequency), str(duty_cycle)])
        self.currentCycle = duty_cycle
        self.currentFrequency = frequency
        print("pwm enabled")


if __name__ == "__main__":
    embeddedObject = Embedded()
    f = int(input("enter f "))
    dc = int(input("enter dc "))
   
    values = []
    for i in range(100):
        embeddedObject.pwmSignal(dc, f)
        value = embeddedObject.CH_pwmIN.voltage
        values.append(value)
        embeddedObject.debugAnalogInput()
        sleep(0.01)
    plt.plot(values)
    plt.show()


