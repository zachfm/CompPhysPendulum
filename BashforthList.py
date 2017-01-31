
import math

dt = .01

class Pendulum:
    def __init__(self):
        self.vel = []
        self.theta = []
        self.accel = []

k = 3.5

def cal_accel(theta):
    accel = (-1)*k*k*math.sin(math.radians(theta))
    print( "Acceleration: " + str(accel))
    return accel

def bashforthadams(style, pend):
    if style == "pos":
        pend.theta.append(  pend.theta[-1] + (3*dt*pend.vel[-1]/2) \
                             - dt*pend.vel[-2]/2)
    if style == "vel":
        pend.vel.append(pend.vel[-1] + 3*dt*cal_accel(pend.theta[-1])/2 \
                             - dt*cal_accel(pend.theta[-1])/2

def run_oscillator(pend):    
    for i in range (100):
        #ok = input("Vel: " + str(pend.curr_vel) + "\nPos: " + str(pend.curr_pos))
        bashforthadams("pos", pend)
        bashforthadams("vel", pend)
def main():
    pend = Pendulum()
    run_oscillator(pend)

def solve_analytical_small():
    timestep = .25
    pend_small = Pendulum()
    t = 0
    for i in range(100):
            pend.theta.append(pend.theta[0]*math.cos(k*t))
            pend.vel.append((-1)*k*pend.vel[0]*math.sin(k*t))
            t += timestep
    return pend_small

plt.plot(pend.theta, pend.vel)
plt.xlabel('theta')
plt.ylabel('vel')
plt.show()