# Import libraries
import webiopi
import smbus as smbus
import time

# Config I2C bus
bus = smbus.SMBus(1)

# This is the address we setup in the Arduino Program
address = 0x04

# Define functions
def writeNumber(val):
	bus.write_byte(address, val)
	print val

# Add macro
@webiopi.macro
def relay1off(0):
	writeNumber()

@webiopi.macro
def relay1on(1):
	writeNumber()

# Start the webiopi server
server = webiopi.Server(port=8000, login="dashboard", password="raspberry")

# Add server macro
server.addMacro(relay1off)
server.addMacro(relay1on)

# Run default loop
webiopi.runLoop()

# Cleanly stop server
server.stop()
