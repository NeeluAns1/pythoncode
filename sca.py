#network usage per process

from scapy.all import*
import psutil
from collections import defaultdict
import os
from threading import Thread
import pandas as pd

#get the all netwrok adapter/s MAC addresses

all_macs = {iface.mac for iface in ifaces.values()}
print(all_macs)

#A dictionary to map each connection to its corresponding process ID(PID)

connection2pid = {}

#A dictionary to map each process ID(PID) to total Upload (0) and Download (1) traffic

pid2traffic = defaultdict(lambda: [0,0])
print(pid2traffic)
# the global pandas dataframe that's used to track previous traffic stats

global_df = None

#global booleran for status of the program

is_program_running = True

def get_size(bytes): 
    """
    return size of bytes in a nuce format
    """
    for unit in ['','K','M','G','T','P']:    #binary mnemonics
        if bytes < 1024:
            return f"{bytes:.2f}{unit}B"
    bytes /= 1024



