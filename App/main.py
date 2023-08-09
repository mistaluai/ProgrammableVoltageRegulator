import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import busio
import digitalio
import board
from time import sleep
import RPi.GPIO as GPIO
import sys
import subprocess
# import matplotlib.pyplot as plt
from multiprocessing import Process
import threading
# ui and gtk
import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

UI_FILE = "UI.xml"


# global variables

# # analog variables
# inputVoltage = 0
# outputVoltage = 0
# shuntVoltage = 0
# current = 0
# resistance = 0

# # constants
# shunt_resistance = 10
# inputVoltage_factor = 109 / 20
# outputVoltage_factor = 52 / 7


class UI:
    desiredVoltage = 0
    resistance = 0
    CycleIncrease = 0
    CycleDecrease = 0

    def __init__(self):
        self.builder = Gtk.Builder()
        self.builder.add_from_file(UI_FILE)
        self.builder.connect_signals(self)

        self.window = self.builder.get_object("window")
        self.window_label = self.builder.get_object("Controller")
        self.window.show_all()

    def ibutton_clicked(self, increase):
        self.step = self.builder.get_object("step")
        self.CycleIncrease = float(self.step.get_text())

    def dbutton_clicked(self, decrease):
        self.step = self.builder.get_object("step")
        self.CycleIncrease = -1 * float(self.step.get_text())

    def button_clicked(self, Apply):
        self.Entry = self.builder.get_object("Entry")
        self.Vout = float(self.Entry.get_text())
        self.Resistance = self.builder.get_object("resistance")
        self.resistance = float(self.Resistance.get_text())
        if (self.Vout / self.resistance) > 0.1:
            self.warninglabel = self.builder.get_object("warning")
            self.warninglabel.set_label("Couldn't apply voltage, current will exceed 100mA")
        else:
            self.desiredVoltage = self.Vout

    def get_voltageDesired_button_value(self, v_desired):
        self.Entry = self.builder.get_object("Entry")
        desiredVoltage = float(self.Entry.get_text())

    def windows_destroy(self, window):
        Gtk.main_quit()

    def main(self):
        Gtk.main_iteration()


class Embedded:
    timestep = 0.01
    _100ohm = dict({2.5: 17, 3: 22, 3.5: 26, 4: 31, 4.5: 37, 5: 44, 5.5: 50})
    _330ohm = dict(
        {2.5: 5, 3: 6, 3.5: 4, 4: 8, 4.5: 9, 5: 10.2, 5.5: 11.9, 6: 13.3, 6.5: 14.7, 7: 17, 7.5: 19, 8: 20.5, 8.5: 23,
         9: 26, 9.5: 29, 10: 31, 10.5: 35, 11: 39, 11.5: 42, 12: 45})
    _560ohm = dict(
        {2.5: 2.6, 3: 3.1, 3.5: 4, 4: 4.6, 4.5: 5.3, 5: 5.9, 5.5: 7, 6: 7.5, 6.5: 8.3, 7: 9.6, 7.5: 9.6, 8: 11.2,
         8.5: 12.2, 9: 13.4, 9.5: 14.7, 10: 17, 10.5: 19.5, 11: 20.8, 11.5: 23, 12: 24})

    # # analog channels

    # CH_inputVoltage = None
    # CH_outputVoltage = None
    # CH_shuntVoltage = None
    # CH_pwmIN = None
    # # pid variables
    # Kp = 0
    # Ki = 0
    # Kd = 0
    # integrator = 0
    # maxIntegrator = 0
    # diffrentiator = 0
    # prevError = 0
    # prevMeasurment = 0
    # error = 0
    ui = None

    def __init__(self, ui):
        # # Analog To Digital
        # # create the spi bus
        # spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
        # print("SPI Bus created")
        # # create the cs (chip select)
        # cs = digitalio.DigitalInOut(board.D5)
        # # create the mcp object
        # mcp = MCP.MCP3008(spi, cs)
        # print("MCP Object created")
        # # channels definition
        # self.CH_inputVoltage = AnalogIn(mcp, MCP.P3, MCP.P2)
        # self.CH_outputVoltage = AnalogIn(mcp, MCP.P1, MCP.P0)
        # self.CH_shuntVoltage = AnalogIn(mcp, MCP.P4, MCP.P5)
        # self.CH_pwmIN = AnalogIn(mcp, MCP.P6)
        # print("Diffrential Channels Defined")
        # board
        GPIO.setmode(GPIO.BCM)
        self.ui = ui

    prevDesiredVoltage = 0

    def checkForDesiredVoltage(self, ui):  # meant to be executed in the loop
        if self.prevDesiredVoltage != ui.desiredVoltage:
            print("voltage changed")
        self.prevDesiredVoltage = ui.desiredVoltage

    # def PIDinit(self):
    #     self.integrator = 0
    #     self.diffrentiator = 0
    #     self.prevError = 0
    #     self.error = 0
    #     self.prevMeasurment = 0
    #     self.globalDutyCycle = (desiredVoltage / inputVoltage) * 100

    # def PIDupdate(self):
    #     self.pid = 0
    #     self.error = desiredVoltage - outputVoltage

    #     self.proportional = self.Kp * self.error
    #     self.integrator = self.integrator + self.error * self.timestep
    #     self.diffrentiator = (self.error - self.prevError) / self.timestep

    #     self.globalDutyCycle += self.pid
    #     if self.globalDutyCycle > 100:
    #         self.globalDutyCycle = 100
    #     elif self.globalDutyCycle < 0:
    #         self.globalDutyCycle = 0
    #     self.prevError = error
    #     self.prevMeasurment = outputVoltage

    # def getInputVoltage(self):
    #     inputVoltage = inputVoltage_factor * self.CH_inputVoltage.voltage

    # def getOutputVoltage(self):
    #     outputVoltage = outputVoltage_factor * self.CH_outputVoltage.voltage - self.CH_shuntVoltage.voltage;

    # def getCurrent(self):
    #     shuntVoltage = self.CH_shuntVoltage.voltage
    #     current = shuntVoltage * 100;

    # def getResistance(self):
    #     if current != 0:
    #         resistance = outputVoltage / current
    #     else:
    #         resistance = 0

    # def debugAnalogInput(self):
    #     print("about to call something")
    #     self.getInputVoltage()
    #     self.getOutputVoltage()
    #     self.getCurrent()
    #     self.getResistance()
    #     print("Input Voltage (V): " + str(inputVoltage) + "\nOutput Voltage (V): " + str(
    #         outputVoltage) + "\nShunt Voltage (V): " + str(shuntVoltage) + "\nTotal Current (mA): " + str(
    #         current) + "\nTotal Resistance (Ω): " + str(resistance))

    currentCycle = 0
    dutyCycle = 0
    currentFrequency = 0

    def setCycle(self, ui):
        if ui.resistance != 330 and ui.resistance != 560 and ui.resistance != 100:
            if ui.resistance > 100 and ui.resistance < 330:
                self.dutyCycle = self._100ohm[ui.desiredVoltage] if (ui.resistance < 215) else self._330ohm[ui.desiredVoltage]
            elif ui.resistance > 330 and ui.resistance < 560:
                self.dutyCycle = self._330ohm[ui.desiredVoltage] if (ui.resistance < 445) else self._560ohm[ui.desiredVoltage]
        elif ui.resistance == 100:
            self.dutyCycle = self._100ohm[ui.desiredVoltage]
        elif ui.resistance == 330:
            self.dutyCycle = self._330ohm[ui.desiredVoltage]
        elif ui.resistance == 560:
            self.dutyCycle = self._560ohm[ui.desiredVoltage]
        else:
            self.dutyCycle = 0

    def pwmSignal(self, duty_cycle, frequency):
        if self.currentFrequency != frequency or self.currentCycle != duty_cycle:
            self.disablePWM()
            self.enablePWM(duty_cycle, frequency)
            print("PWM changed")

    def disablePWM(self):
        try:
            subprocess.call(["pkill", "-f", "pwm.py"])
        except:
            pass

    def enablePWM(self, duty_cycle, frequency):
        pwmScript = subprocess.Popen(
            ["python", "/home/proj/Documents/embproj/Pi3BScripts/pwm.py", "13", str(frequency), str(duty_cycle)])
        self.currentCycle = duty_cycle
        self.currentFrequency = frequency
        print("pwm enabled")

    def embeddedMain(self):
        pass


if __name__ == "__main__":
    uiapp = UI()
    embeddedObject = Embedded(uiapp)
    print("embedded loop started")
    while True:
        uiapp.main()
        embeddedObject.checkForDesiredVoltage(uiapp)
        embeddedObject.setCycle(uiapp)
        embeddedObject.pwmSignal(embeddedObject.dutyCycle, 20)
        sleep(embeddedObject.timestep)
