import serial
import serial.tools.list_ports
import sys

from flask import Flask
from flask_socketio import SocketIO

app = Flask(__name__)
app.config['SECRET_KEY'] = 'test'
socketio = SocketIO(app)

def handle_message(message):
	print("recieved " + message)
	send_message(message)

def send_message(mes):
	ports = list(serial.tools.list_ports.comports())
	arduino = ''
	for x in ports:
		if "USB2.0-Serial" in x[1]:
			arduino = x[0]
			break
	if arduino != "":
		ser = serial.Serial()
		ser.baudrate = 9600
		ser.port = arduino
		ser.stopbits = 1
		ser.databits = 8
		ser.open()
		ser.write(str(mes).encode('utf-8'))
		ser.close()

if __name__ == "__main__":
@socketio.on('message')
	socketio.run(app)