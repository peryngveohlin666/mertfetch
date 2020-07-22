import platform
from datetime import datetime
import psutil
from termcolor import colored
from pyfiglet import figlet_format


print(
    colored(figlet_format('MERTFETCH'), 'green') +
    colored(platform.node(), 'red') + "\n" +
    "----------------------" + "\n" +
      colored("System: ", 'green' ) + platform.platform() + " " + platform.system() +
      colored("\nPython version: ", 'green'), platform.python_version() +
      colored("\nCPU count: ", 'green') + str(psutil.cpu_count(logical=False)) +
      colored("\nCPU freq: ", 'green') + str(psutil.cpu_freq()[2]) +
      colored("\nRam: ", 'green') + (str(psutil.virtual_memory()[0]/1024))[:2] + "GB" +
      colored("\nUptime: ", 'green') + str(datetime.now() - datetime.fromtimestamp(psutil.boot_time()))
)

