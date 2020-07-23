#!/usr/local/bin/python3

import platform
from datetime import datetime
import psutil
from termcolor import colored
from pyfiglet import figlet_format


print(
    colored(figlet_format('MERTFETCH'), 'green') +
    colored(platform.node(), 'red') + "\n" +
    len(platform.node())*"-" + "\n" +
      colored("System: ", 'green' ) + platform.platform() + " | " + platform.system() +
      colored("\nPython version: ", 'green'), platform.python_version() +
      colored("\nCPU count: ", 'green') + str(psutil.cpu_count(logical=False)) +
      colored("\nCPU freq (Max): ", 'green') + str(psutil.cpu_freq()[2]) + " |" + colored(" Current: ", 'yellow') + str(psutil.cpu_freq()[0]) +
      colored("\nRAM: ", 'green') + str(psutil.virtual_memory()[0]/1024**2)[:2] + "GB" + " |" + colored(" Used: ", 'yellow') + str(psutil.virtual_memory().percent * psutil.virtual_memory()[0] / 100 / 1024**3)[:4] +
      colored("\nUptime: ", 'green') + str(datetime.now() - datetime.fromtimestamp(psutil.boot_time()))
)

