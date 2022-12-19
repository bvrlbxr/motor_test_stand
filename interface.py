import time, datetime, json, os
from tkinter import Tk
from tkinter.ttk import Combobox,Frame,Label,Entry,Button,Style
from connector import CurrentMaster
from graphic import CreatePlot


class Interface:

	def __init__(self,master):

		self.app_style = Style()
		self.app_style.theme_use("clam")
		# self.app_style.configure("TButton",background="#f7a34f")
		# self.app_style.configure("TFrame",background="#ffbf80")
		# create connect obj
		self.device_obj = CurrentMaster()
		# create frame
		self.frame = Frame(root)
		self.frame.grid()

		# common labels

		# error label
		self.error_label = Label(self.frame,text="")
		self.error_label.grid(row=0, column=0)

		# parametr label
		self.par_label = Label(self.frame,text="Параметры теста",font="Arial 10")
		self.par_label.grid(row=0, column=0)

		## cur values label
		self.par_label = Label(self.frame, text="Телеметрия",font="Arial 10")
		self.par_label.grid(row=0, column=1)
		# ==============

		# column 0
		# create input fields
		# # input 1
		self.input1_label = Label(self.frame,text="Напряжение, В")
		self.input1_label.grid(row=1, column=0)
		self.input1 = Entry(self.frame)
		self.input1.grid(row=2, column=0)

		# # input 2
		self.input2_label = Label(self.frame,text="Сила тока, А")
		self.input2_label.grid(row=3, column=0)
		self.input2 = Entry(self.frame)
		self.input2.grid(row=4, column=0)

		# # input 3
		self.input3_label = Label(self.frame,text="Скорость вращения, об/мин.")
		self.input3_label.grid(row=5, column=0)
		self.input3 = Entry(self.frame)
		self.input3.grid(row=6, column=0)

		# # input 4
		self.input4_label = Label(self.frame,text="Название/номер теста")
		self.input4_label.grid(row=7, column=0)
		self.input4 = Entry(self.frame)
		self.input4.grid(row=8, column=0)

		# create buttons
		# save test
		self.button1 = Button(self.frame, text="Сохранить тест", command=self.save_test_parameters)
		self.button1.grid(row=9, column=0)

		# # input 5
		self.input5_label = Label(self.frame,text="Название/номер тензодатчика")
		self.input5_label.grid(row=10, column=0)
		self.input5 = Entry(self.frame)
		self.input5.grid(row=11, column=0)

		# # input 6
		self.input6_label = Label(self.frame,text="Коэффициент тензодатчика")
		self.input6_label.grid(row=12, column=0)
		self.input6 = Entry(self.frame)
		self.input6.grid(row=13, column=0)

		# save tenzo
		self.button2 = Button(self.frame, text="Сохранить тензодатчик", command=self.save_tenzo_parameters)
		self.button2.grid(row=14, column=0)

		# column 1
		# current values ==================
		# # input 7
		self.input7_label = Label(self.frame,text="Напряжение, В")
		self.input7_label.grid(row=1, column=1)
		self.input7 = Entry(self.frame)
		self.input7.grid(row=2, column=1)

		# # input 8
		self.input8_label = Label(self.frame,text="Сила тока, А")
		self.input8_label.grid(row=3, column=1)
		self.input8 = Entry(self.frame)
		self.input8.grid(row=4, column=1)

		# # input 9
		self.input9_label = Label(self.frame,text="Скорость вращения, об/мин.")
		self.input9_label.grid(row=5, column=1)
		self.input9 = Entry(self.frame)
		self.input9.grid(row=6, column=1)

		# # input 10
		self.input10_label = Label(self.frame,text="Показания тензо")
		self.input10_label.grid(row=7, column=1)
		self.input10 = Entry(self.frame)
		self.input10.grid(row=8, column=1)

		# # input 11
		self.input11_label = Label(self.frame,text="Температура")
		self.input11_label.grid(row=9, column=1)
		self.input11 = Entry(self.frame)
		self.input11.grid(row=10, column=1)

		# start test
		self.button5 = Button(self.frame, text="Начать тест", command=self.start_test_req)
		self.button5.grid(row=12, column=1)

		#  ========== ==== column 2
		# create buttons ===================
		self.button3 = Button(self.frame, text="Загрузить выбранный тест", command=self.load_selected_config)
		self.button3.grid(row=2, column=4)

		# create combo existing tests
		self.par_label = Label(self.frame,text="Выбрать сохраненный тест",font="Arial 10")
		self.par_label.grid(row=0, column=4)
		self.combo_test_configs = Combobox(self.frame)
		self.combo_test_configs.grid(row=1, column=4)

		# create combo existing tenzo
		self.tenzo_label = Label(self.frame,text="Выбрать сохраненный тензодатчик")
		self.tenzo_label.grid(row=3, column=4)
		self.combo_tenzo_configs = Combobox(self.frame)
		self.combo_tenzo_configs.grid(row=4, column=4)

		# select tenzo
		self.button4 = Button(self.frame, text="Загрузить выбранный тензодатчик", command=self.load_selected_tenzo)
		self.button4.grid(row=5, column=4)

		# graphics

		# create combo existing tenzo
		self.plot_label = Label(self.frame,text="Выбрать данные для графика")
		self.plot_label.grid(row=9, column=4)
		self.combo_plot_configs = Combobox(self.frame)
		self.combo_plot_configs.grid(row=10, column=4)

		self.button6 = Button(self.frame, text="Построить график", command=self.print_graphics)
		self.button6.grid(row=11, column=4)

		# ===================================
		# init existing configs
		self.load_test_configs()
		self.load_tenzo_configs()
		self.load_data_plots()

	def print_graphics(self):
		"""
		test start
		"""
		file_name = self.combo_plot_configs.get()
		fig = CreatePlot(f"./graphic_data/{file_name}.csv", "png")
		fig.create_plot()
		fig.show_plot()

	def load_test_configs(self):
		"""
		load existing configs
		"""
		test_config = []
		for i in os.listdir("./test_configs"):
			if i.endswith(".json"):
				test_config.append(i.split(".")[0])
		self.combo_test_configs["values"] = test_config

	def load_data_plots(self):
		data_plots = []
		for i in os.listdir("./graphic_data"):
			if i.endswith(".csv"):
				data_plots.append(i.split(".")[0])
		self.combo_plot_configs["values"] = data_plots

	def save_test_parameters(self):
		"""
		save test params
		"""
		file_name = self.input4.get()

		if self.input1.get() and self.input2.get() and self.input3.get() and file_name:
			settings = {"voltage": float(self.input1.get()),
						"current": float(self.input2.get()),
						"RPM": int(self.input3.get())}

			with open(f'./test_configs/{file_name}.json', 'w') as outfile:
				json.dump(settings, outfile, indent=4)
			# saving parameters....
			time.sleep(0.5)
			# updating combobox
			self.load_test_configs()
		else:
			print("ошибка сохранения: введите напряжение,ток, скорость и название теста")

	def save_tenzo_parameters(self):
		"""
		save tenzo params
		"""
		settings = {"tenzo_coeff": float(self.input6.get())}

		file_name = self.input5.get()

		with open(f'./tenzo/{file_name}.json', 'w') as outfile:
			json.dump(settings, outfile, indent=4)
		# saving parameters....
		time.sleep(0.5)
		# updating combobox
		self.load_tenzo_configs()

	def load_selected_tenzo(self):
		try:
			file_name = self.combo_tenzo_configs.get()
			with open(f"./tenzo/{file_name}.json", "r") as f:
				config = json.load(f)

			self.clear_input(self.input6)
			self.input6.insert(0,config.get("tenzo_coeff"))  # tenzo

			self.clear_input(self.input5)  # clear input
			self.input5.insert(0,file_name)
		except:
			print("cannot load tenzo config")

	def load_tenzo_configs(self):
		"""
		load existing configs
		"""
		tenzo_configs = []
		for i in os.listdir("./tenzo"):
			if i.endswith(".json"):
				tenzo_configs.append(i.split(".")[0])
		self.combo_tenzo_configs["values"] = tenzo_configs


	def load_selected_config(self):
		try:
			file_name = self.combo_test_configs.get()
			with open(f"./test_configs/{file_name}.json", "r") as f:
				config = json.load(f)
			# self.input1.insert(0, "")  # clear input
			self.clear_input(self.input1)
			self.input1.insert(0,config.get("voltage"))  # напряжение

			self.clear_input(self.input2)  # clear input
			self.input2.insert(0,config.get("current"))  # сила тока

			self.clear_input(self.input3)  # clear input
			self.input3.insert(0, config.get("RPM"))  # скорость вращения

			self.clear_input(self.input4)  # clear input
			self.input4.insert(0,file_name)
		except:
			print("cannot load test config")

	def start_test_req(self):

		if self.input4.get():
			data_file_name = f"""{self.input4.get()}_{datetime.datetime.now().strftime("%d%M%Y_%H%m%S")}"""
			self.device_obj.start_test_req(data_file_name)  # transmit file name to Connector obj
		else:
			print("error введите название теста или выберите из существующих перед стартом")

	def clear_input(self,entry_obj):
		entry_obj.delete(0,len(entry_obj.get()))

root = Tk()
my_interface = Interface(root)
