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
def relayOff_1():
	writeNumber(0)

@webiopi.macro
def relayOn_1():
	writeNumber(1)

@webiopi.macro
def relayOff_2():
	writeNumber(2)

@webiopi.macro
def relayOn_2():
	writeNumber(3)

@webiopi.macro
def relayOff_3():
	writeNumber(4)

@webiopi.macro
def relayOn_3():
	writeNumber(5)

@webiopi.macro
def relayOff_4():
	writeNumber(6)

@webiopi.macro
def relayOn_4():
	writeNumber(7)

# Start the webiopi server
server = webiopi.Server(port=8000)

# Add server macro
server.addMacro(relayOff_1)
server.addMacro(relayOn_1)
server.addMacro(relayOff_2)
server.addMacro(relayOn_2)
server.addMacro(relayOff_3)
server.addMacro(relayOn_3)
server.addMacro(relayOff_4)
server.addMacro(relayOn_4)

# Run default loop
webiopi.runLoop()

# Cleanly stop server
server.stop()
