import numpy as np
import matplotlib.pyplot as plt


class CreatePlot:

    def __init__(self, data_path, file_type):
        self.file_type = file_type
        self.data_path = data_path
        self.data = np.genfromtxt(self.data_path, delimiter=',', skip_header=1,
                             names=['Time_ms', 'dshot', 'Voltage_V', 'Current_A', 'RPM', 'Thrust_g'])
        self.fig = plt.figure()

    def create_plot(self):
        ax1 = self.fig.add_subplot(311)
        self.fig.subplots_adjust(right=0.75)
        ax2 = ax1.twinx()
        ax3 = ax1.twinx()
        ax3.spines["right"].set_position(("axes", 1.2))

        ax3.plot(self.data['Time_ms'], self.data['dshot'], color='y', label='dshot')
        ax3.set_xlabel('Time_ms')
        ax3.set_ylabel('dshot')
        ax3.set_ylim([0, 2100])

        ax2.plot(self.data['Time_ms'], self.data['Thrust_g']/(self.data['Voltage_V']*self.data['Current_A']/10), color='r', label='g/W')
        ax2.set_ylabel('g/W')
        ax2.set_ylim([0, 5])
        ax2.legend()

        ax1.plot(self.data['Time_ms'], self.data['Thrust_g'], color='b', label='Thrust (g)')
        ax1.set_ylabel('Thrust (g)')
        ax1.set_ylim([0, 1500])
        ax1.legend()


        ax1 = self.fig.add_subplot(312)
        self.fig.subplots_adjust(right=0.75)
        ax2 = ax1.twinx()
        ax3 = ax1.twinx()
        ax3.spines["right"].set_position(("axes", 1.2))

        ax3.plot(self.data['Time_ms'], self.data['dshot'], color='y', label='dshot')
        ax3.set_xlabel('Time_ms')
        ax3.set_ylabel('dshot')
        ax3.set_ylim([0, 2100])

        ax2.plot(self.data['Time_ms'], self.data['Voltage_V'], color='r', label='Voltage (V)')
        ax2.set_ylabel('Voltage (V)')
        ax2.set_ylim([15.5, 26])
        ax2.legend()

        ax1.plot(self.data['Time_ms'], self.data['Current_A']/10, color='b', label='Current (A)')
        ax1.set_ylabel('Current (A)')
        ax1.set_ylim([0, 50])
        ax1.legend()


        ax1 = self.fig.add_subplot(313)
        self.fig.subplots_adjust(right=0.75)
        ax2 = ax1.twinx()
        ax3 = ax1.twinx()
        ax3.spines["right"].set_position(("axes", 1.2))

        ax3.plot(self.data['Time_ms'], self.data['dshot'], color='y', label='dshot')
        ax3.set_xlabel('Time_ms')
        ax3.set_ylabel('dshot')
        ax3.set_ylim([0, 2100])

        ax1.plot(self.data['Time_ms'], self.data['RPM'], color='r', label='RPM')
        ax1.set_ylabel('RPM')
        ax1.set_ylim([0, 30000])
        ax1.legend()

        ax2.plot(self.data['Time_ms'], self.data['RPM']/self.data['Voltage_V'], color='b', label='KV')
        ax2.set_ylabel('KV')
        ax2.set_ylim([0, 2600])
        ax2.legend()

    def show_plot(self):
        self.fig.show()

    def save_plot(self):
        self.fig.savefig(f"./graphics/plot.{self.file_type}")
