import socket
import serial
import json
import csv
import time
# import threading


class CurrentMaster:

	def __init__(self):
		self.config = self.get_config()
		self.connected = False
		self.current_master = self.configure_current_master()
		self.data_file = None
		self.test_run = False
		self.test_start = False

	def get_config(self):

		try:
			with open("./connector_config.json","r") as f:
				config = json.load(f)
		except:
			print("cannot load config")

		return config

	def configure_current_master(self):
		test = True
		if not test:
			try:
				if self.config["type"] == "socket":
					sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

					for i in self.config["connect_attemps"]:
						if not self.connected:
							sock.connect((self.config["host"], self.config["port"]))
						else:
							print("Successfully connected")
							break

					return sock if self.connected else print("Cannot connect!")

				elif self.config["type"] == "serial":
					ser = serial.Serial(
						port=self.config["port"],
						baudrate=self.config["baudrate"],
						bytesize=self.config["bytesize"],
						parity=(serial.PARITY_NONE),
						# parity=self.config.get("parity", serial.PARITY_NONE),
						stopbits=self.config["stopbits"]
					)
					return ser
				else:
					raise ValueError("Invalid connection type")
			except:
				print("error")

	def start_test_req(self,data_file_name):

		if not self.test_start:
			headers = ["Time (ms)","dshot","Voltage (V)","Current (A)","RPM,Thrust (g)"]
			print(data_file_name, "коннектор")
			self.test_start = True
			self.test_run = True
			with open(f'./graphic_data/{data_file_name}.csv', 'w', newline='') as csvfile:
				telemetry_data = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
				telemetry_data.writerow(headers)
				for i in range(100): # test
					telemetry_data.writerow([9686, 1547, 16.83, 24.2, 31157, 1])
			print("start_test_ok")
		else:
			print("коннектор: тест уже начался")
		return self.config["device_adress"]

	def get_data(self):
		pass

	def calibrate_tenzo(self):
		pass

