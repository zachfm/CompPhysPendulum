import matplotlib.pyplot as plt
import numpy as np

import math

dt = .01

class Pendulum:
    def __init__(self):
        self.vel = []
        self.theta = []
        self.accel = []

"""
class Pendulum:
    def __init__(self):
        self.curr_vel = -.1
        self.prev_vel = 0
        self.curr_pos = 89
        self.prev_pos = 90
"""

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

pend = Pendulum()
run_oscillator(pend)

plt.plot(pend.theta, pend.vel)
plt.xlabel('t')
plt.ylabel('y(t)')
plt.show()
