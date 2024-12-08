import os
import sys
from time import sleep

from .defs import Table


def animate_guard(table:Table, frame_rate:float=0.5):
    cl_cmd = 'cls' if os.name == 'nt' else 'clear'
    for step in table.iterate_update():
        os.system(cl_cmd)
        table.display()
        sleep(1/frame_rate)
    os.system(cl_cmd)
    table.display()
    sleep(1/frame_rate)
