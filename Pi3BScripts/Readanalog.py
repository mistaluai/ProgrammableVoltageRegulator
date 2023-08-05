import adafruit_mcp3xxx.mcp3008 as MCP
from adafruit_mcp3xxx.analog_in import AnalogIn
import busio
import digitalio
import board
from time import sleep

# create the spi bus
spi = busio.SPI(clock=board.SCK, MISO=board.MISO, MOSI=board.MOSI)
# create the cs (chip select)
cs = digitalio.DigitalInOut(board.D5)

# create the mcp object
mcp = MCP.MCP3008(spi, cs)

# create an analog input channel on pin 0
chan = AnalogIn(mcp, MCP.P0, MCP.P1)

while True:
	print('Voltage Across the resistor: ' + str(chan.voltage) + 'V')
	print('Current in the circuit: ' + str((chan.voltage*100)) + 'mA')
	print('Circuit Resistance' + str(4.6/((chan.voltage*100))) + 'kΩ')
	sleep(0.05)