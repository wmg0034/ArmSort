import time
from servo import Servo
from machine import Pin


S0 = Servo(Pin(0)) #S0 takes values in (0, 180). 90 is forward.
S2 = Servo(Pin(2)) #S2 takes values in (0, 180). 90 is up, 0 is forward.
S4 = Servo(Pin(4)) #S4 takes values in (0, 180). 0 is forward, 90 is up, 180 is backward.
S6 = Servo(Pin(6)) #S6 takes values in (0, 180). 45 is parallel to the table.
S8 = Servo(Pin(8)) #S10 takes values in (0, 100). 0 is fully open, 100 is almost closed.

servos = [S0, S2, S4, S6, S8]
rest = [90, 90, 0, 45, 60]
rest_state = dict(zip(servos, rest))

reach = [90,180,120,45,60]
reach_state = dict(zip(servos, reach))

current_state = rest_state.copy()

def angle2state(angle_code : str):
    angle_list = angle_code.split('-')
    angle_list = [int(a) for a in angle_list]
    state = dict(zip(servos, angle_list))
    return state

def state2angle(state : dict):
    angle_code = ''
    for s in servos:
        angle_code += str(state[s])
        angle_code += '-'
    angle_code = angle_code[:-1]
    return angle_code

def update_state(target_state : dict):
    for i in range(20):
        for s in reversed(servos):
            current_state[s] += (target_state[s] - current_state[s])/20
            s.write(current_state[s])
            time.sleep(.01)
        
#for debugging purposes
def slow_write(s, p):
    for i in range(20):
        current_state[s] += (p - current_state[s])/20
        s.write(current_state[s])
        time.sleep(.05)
