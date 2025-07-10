import os
import sys 
import subprocess


class Agent():
	def __init__(self):
		self.so = sys.platform
		if self.so == 'linux':
			self.hostname = subprocess.check_output(['hostname'], text=True).strip()
			self.architecture = subprocess.check_output(["lscpu | grep 'Architecture:' | cut -d ':' -f2 | xargs"],shell=True, text=True).strip()
			self.model = subprocess.check_output(["lscpu | grep 'Model name:' | cut -d ':' -f2 | xargs"],shell=True, text=True).strip()
			self.ram = subprocess.check_output(["cat /proc/meminfo | head -n 3 | sed 's/  */ /g' "],shell=True, text=True).strip()
			self.up = subprocess.check_output(["uptime -p | cut -d ' ' -f 2-5"],shell=True, text=True).strip()
			self.port = subprocess.check_output(["ss -tuln"],shell=True, text=True).strip() 
			self.interfaces = subprocess.check_output(["ip a"],shell=True, text=True).strip() 
			self.processes = subprocess.check_output(["ps -eo pid,user,%cpu,%mem,comm --sort=-%cpu | head -n 6"],shell=True, text=True).strip() 
		else:
			print("Cannot recognize operating system.")
	def inform(self):
		details = (
		f'Computer info\n\n'
		f'Sistema operativo: {self.so}\n'
		f'Hostname: {self.hostname}\n'
		f'Architecture: {self.architecture}\n'
		f'Model: {self.model}\n\n'		
		f'System status\n\n'
		f'Uptime: {self.up}\n'
		f'{self.ram}\n\n'
		f'Processes\n'
		f'{self.processes}\n\n'
		f'Network\n\n'
		f'Interfaces\n'
		f'{self.interfaces}\n\n'
		f'Listening Ports \n{self.port}'
		)
		return details
		
	def __str__(self):
		return self.inform()
		
		
agente = Agent()

print(agente)
