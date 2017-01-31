import math

dt = float(input("Delta t pls: "))

class Pendulum:
    def __init__(self):
        self.curr_vel = -.1
        self.prev_vel = 0
        self.curr_pos = 89
        self.prev_pos = 90
 
k = 3.5

def cal_accel(theta):
    accel = (-1)*k*k*math.sin(math.radians(theta))
    print( "Acceleration: " + str(accel))
    return accel

def bashforthadams(style, pend):
    if style == "pos":
        prev = pend.curr_pos
        pend.curr_pos = pend.curr_pos + (3*dt*pend.curr_vel/2) \
                             - dt*pend.prev_vel/2
        pend.prev_pos = prev
    if style == "vel":
        prev = pend.curr_vel
        pend.curr_vel = pend.curr_vel + (3*dt*cal_accel(pend.curr_pos)/2) \
                             - dt*cal_accel(pend.curr_pos)/2
        pend.prev_vel = prev
    return pend

def run_oscillator():    
    pend = Pendulum()
    for i in range (10000000):
        #ok = input("Vel: " + str(pend.curr_vel) + "\nPos: " + str(pend.curr_pos))
        pend = bashforthadams("pos", pend)
        pend = bashforthadams("vel", pend)
	
        if i == 1000000:
            break


def main():
    run_oscillator()

main()
    
