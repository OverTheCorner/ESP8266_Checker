import serial
import time

# Configure the serial port
port = 'COM9'  # Replace with the appropriate serial port for your system
baudrate = 115200  # Set the baud rate to match your ESP8266 configuration
timeout = 7

# Open the serial port
ser = serial.Serial(port, baudrate, timeout=timeout)

# Wait for the serial port to be ready
time.sleep(2)

# Send an AT command and wait for the response


def send_at_command(command):
    ser.write(command.encode() + b'\r\n')
    # Change 'OK' to the expected response
    response = ser.read_until(b'OK\r\n')
    return response.decode()


print(send_at_command('AT'))  # AT Functionality
print(send_at_command('AT+GMR'))  # Firware Version
print(send_at_command('AT+CWMODE?'))  # Current Mode
print(send_at_command('AT+CWMODE=3'))  # Turn into dual mode
print(send_at_command('AT+CWLAP'))  # etection of WiFi Networks

# Close the serial port
ser.close()
