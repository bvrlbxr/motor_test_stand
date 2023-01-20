import socket
import serial
import json
import csv
import time
import os
# import threading


class CurrentMaster:

	def __init__(self):
		self.config = self.get_config()
		self.connected = False
		self.data_file = None
		self.test_run = False
		self.test_start = False
		self.current_master = None

	def get_config(self):
		config = None
		try:
			with open("./connector_config.json","r") as f:
				config = json.load(f)
		except:
			print("cannot load config")

		return config

	def configure_socket(self):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		for i in range(self.config["connect_attemps"]):
			if not self.connected:
				print(f"Connecting attemp {1+i}")
				try:
					sock.connect((self.config["host"], self.config["socket_port"]))
				except Exception as e:
					print(e)
					time.sleep(0.5)
			else:
				print("Successfully connected")
				break
		return sock if self.connected else print("Cannot connect!")

	def configure_serial(self):
		for i in range(self.config["connect_attemps"]):
			print(f"Connecting attemp {1+i}")
			if not self.connected:
				try:
					ser = serial.Serial(
						port=self.config["port"],
						baudrate=self.config["baudrate"],
						bytesize=self.config["bytesize"],
						parity=self.config.get("parity"),
						stopbits=self.config["stopbits"]
					)
				except Exception as e:
					print(e)
					time.sleep(0.5)
			else:
				print("Successfully connected")
				break

		return ser if self.connected else print("Cannot connect!")

	def configure_current_master(self):

		if self.config["type"] == "serial":
			cur_master = self.configure_serial()
		elif self.config["type"] == "socket":
			cur_master = self.configure_socket()
		else:
			cur_master = None
			print("Wrong connection type")
		return cur_master



	def start_test_req(self,data_file_name):

		if not self.test_start:
			headers = ["Time (ms)","dshot","Voltage (V)","Current (A)","RPM,Thrust (g)"]
			print(data_file_name, "коннектор")

			with open(f'./graphic_data/{data_file_name}.csv', 'w', newline='') as csvfile:
				telemetry_data = csv.writer(csvfile, delimiter=',', quotechar=' ', quoting=csv.QUOTE_MINIMAL)
				telemetry_data.writerow(headers)
				for i in range(100):  # test
					telemetry_data.writerow([9686, 1547, 16.83, 24.2, 31157, 1])
			self.test_start = True
			self.test_run = True
			print("start_test_ok")
		else:
			print("коннектор: тест уже начался")
		return self.config["device_adress"]

	def get_data(self):
		pass

	def stop_test_cmd(self):
		pass

	def calibrate_tenzo(self):
		pass

