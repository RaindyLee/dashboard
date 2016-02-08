# dashboard

A Personal Project on Improving the Smart Home

**By Raindy Lee**

Allows the user to use a Raspberry Pi, Arduino and various modules to control their home from the comfort of their phone, computer, and any other device.

Uses HTML/CSS and Python 3, in conjunction with [WebIOPi](http://webiopi.trouch.com)

[See the making of this Personal Project](dashboardjournal.wordpress.com)

### Installation
1. Plugging in all cables
  - Connection
  - Power
  - Any other cables for the relay
2. User Interface Setup
  - On and Off buttons for simplicity
3. Relay Setup
  - Unscrew cable holder
  - Insert cable
  - Screw back cable holder, ensuring a strong connection
4. That's it!

### SSH and Connections
- Raspberry Pi
  - Use `SSH` and log in to `pi@192.168.1.183`
  - `pi@raspberrypi ~ $` should appear which indicates that you are connected to the Raspberry Pi
  - There are many commands you can execute in the Unix language
  - The OS is Raspbian, which is based off of Debian Linux
- Arduino
  - Download `Arduino IDE` from [the Arduino website](www.arduino.cc)
  - Download the file from this GitHub called `Dashboard_relay.ino` and open it in the Arduino IDE
  - Plug in a USB cable with a USB type B (printer cable) from the computer which has the Arduino IDE to the Arduino
  - Press Upload, and the LEDs on the Arduino should blink

### Troubleshooting
**Always check for loose cables and connections!**

1. Reupload the code on the Arduino
2. Check to see if the Raspberry Pi is connected to the Internet by seeing if the WiFi adapter (small black plug in the USB port) is blinking
  - If not connected, plug out the power cable and reconnect it, which should force restart the Pi
  - Make sure the WiFi modem is turned on and connected to the Internet
3. If none of these apply, contact at the below contact addresses

### Extentions
Since this product uses a Raspberry Pi and an Arduino, there are many different possibilities with this. Just search `projects with a Raspberry Pi` or `projects with an Arduino` and there should be plenty!

This product uses I2C as a connection between the Pi and the Arduino, which can be extended to have more Arduinos or even changed to a Radio Frequency transmission! In addition to that, the code for the website (in HTML and CSS), script (in Python) and also the code for the Arduino can be customised to your will and made to perform many different tasks.

Included is also a breadboard so that you can prototype and use many different other modules such as a [DHT11](https://www.adafruit.com/product/386) sensor to monitor temperature and humidity, and perform tasks accordingly. 

### Recommended 3rd Party Application
- [Weaved](https://www.weaved.com/raspberry-pi-remote-connection/)
  - Allows access from another Internet modem (not confined to local address)
  - This gives access to the Dashboard from afar, even from another country
  - Needs user login
- [Tasker](http://tasker.wikidot.com) and plugins
  - This is an app from an Android phone that allows tasks to be executed when an event is detected
  - For example, when someone uses Google Now and says "Turn the lights on", it sends a command (`HTTP Post`) to the website that then executes the task (`WebIOPi macro`)
  - Paid app and different plugins also need payment
- [Node.js](https://nodejs.org/en/)
  - For more technology-savvy people, this allows the code to be changed from Python to JavaScript, which may be useful depending on the situation
  - This also includes a plugin to communicate over I2C, SPI, and Serial Bus.

  
##### Contacts
Email: raindybl@gmail.com

Email: raindy.lee@sph.ac.id
