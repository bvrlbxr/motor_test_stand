from connector import CurrentMaster
import socket, time

class Simulator(CurrentMaster):

	def __init__(self):
		super().__init__()
		self.config["port"] = "COM2"  # change port

	def stop_test_cmd(self):
		pass

	def calibrate_tenzo(self):
		pass

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

sim = Simulator()
sim.configure_current_master()