#type: ignore

import serial
import math
import time

reach_angle_list = [90,180,120,45,60]
rest_angle_list = [90, 90, 0, 45, 60]
rest_angle_code = '90-90-0-45-60'

def xywh_to_angle_list(xywh : list):
    diff_x = -1 * (0.5 - xywh[0])
    test_angle_list = rest_angle_list.copy()
    test_angle_list[0] = int(90 + math.degrees( math.atan( diff_x / (xywh[1] + .4) ) ))
    # test_angle_list[1] = int(56.25 * (xywh[1] - 0.1))
    # test_angle_list[2] = int(60 * (xywh[1] - 0.1))
    #S2 -> 170, S4 -> 60 is like full reach
    #t2 = 
    # return [t0, t2, t4, t6, t8]
    return test_angle_list

#An angle_code is a string formatted as 't0-t2-t4-t6-t8' where ti is the angle for servo i.
def make_angle_code_from_angle_list(angles):
    angles = [str(a) for a in angles]
    angle_code = ('-').join(angles)
    return angle_code + '\r'

def update_angle_code(xywh):
    angle_list = xywh_to_angle_list(xywh)
    angle_code = make_angle_code_from_angle_list(angle_list)
    return time.time(), angle_code

def update_state(angle_code):

    ser = serial.Serial(
            port="COM3", 
            parity=serial.PARITY_EVEN, 
            stopbits=serial.STOPBITS_ONE, 
            timeout=None)

    ser.flush()
    ser.write(angle_code.encode())
    #mes = ser.read_until().strip()
    print('update state here')
    #print('update' + mes.decode())# + 'and object at: (%s, %s)' % (xywh[0], xywh[1]))
    #ser.close()

if __name__ == "__main__":
    main()