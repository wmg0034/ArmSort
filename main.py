import select
import sys
import time
import machine

from servo_controller import *

# Set up the poll object
poll_obj = select.poll()
poll_obj.register(sys.stdin, select.POLLIN)

while True:
    # Read the data from stdin (read data coming from PC)
    angle_code = sys.stdin.readline().strip()
    state = angle2state(angle_code)
    update_state(state)