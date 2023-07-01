import serial
import time

# Configure the serial port
port = 'COM9'  # Replace with the appropriate serial port for your system
baudrate = 115200  # Set the baud rate to match your ESP8266 configuration
# some AT commands would take a while (connecting to network, listing avaialable networks)
timeout = 15

# Diagnostic WiFi Credentials
ssid = 'SSID'
password = 'password'


# Open the serial port
ser = serial.Serial(port, baudrate, timeout=timeout)

# Wait for the serial port to be ready
time.sleep(2)

# Send an AT command and wait for the response


def send_at_command(command):
    ser.write(command.encode() + b'\r\n')
    # Read until "OK\r\n" is recieved
    response = ser.read_until(b'OK\r\n')
    return response.decode()


# Basic AT Functionality
print(send_at_command('AT'))  # AT Functionality
print(send_at_command('AT+GMR'))  # Firware Version
print(send_at_command('AT+CWMODE?'))  # Current Mode
print(send_at_command('AT+CWMODE=3'))  # Turn into dual mode
print(send_at_command('AT+CWLAP'))  # detection of WiFi Networks

# Next Section should be done only when connecting to network and pinging is to be checked
# Connect to a WiFi network
print(send_at_command('AT+CWJAP="{}","{}"'.format(ssid, password)))
print(send_at_command('AT+CWJAP?'))
print(send_at_command('AT+CIFSR'))
print(send_at_command('AT+PING="8.8.8.8"'))

# Close the serial port
ser.close()
# GFVA
