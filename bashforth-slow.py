import matplotlib.pyplot as plt
import numpy as np

import math

dt = .01
iterations = 1790

class Pendulum:
    def __init__(self):
        self.vel = [0,-.03]
        self.theta = [15,14.99]
        self.t = [0,.01]
k = 3.5

def cal_accel(theta):
    accel = -(k**2)*math.sin(math.radians(theta))
    #print( "Acceleration: " + str(accel))
    return accel

def bashforthadams(style, pend):
    if style == "vel":
        pend.vel.append(pend.vel[-1] + 1.5*dt*cal_accel(pend.theta[-1]) - 0.5*dt*cal_accel(pend.theta[-2]))
        #pend.vel.append(pend.vel[-1] - dt*cal_accel(pend.theta[-1]))
    if style == "pos":
        pend.theta.append(pend.theta[-2] + 1.5*dt*pend.vel[-2] - 0.5*dt*pend.vel[-3])
        #pend.theta.append(pend.theta[-1] + dt*pend.vel[-1])
        
def run_oscillator(pend):    
    for i in range (iterations):
        #ok = input("Vel: " + str(pend.curr_vel) + "\nPos: " + str(pend.curr_pos))
        bashforthadams("vel", pend)
        bashforthadams("pos", pend)
        pend.t.append(pend.t[-1]+dt)
       
pend = Pendulum()
run_oscillator(pend)

plt.plot(pend.t, pend.theta)
plt.xlabel('t')
plt.ylabel('theta')
plt.show()
