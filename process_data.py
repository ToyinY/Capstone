#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 19:43:55 2020
@author: riley
"""
import pandas as pd
import numpy as np
from scipy import integrate
from scipy import signal
import matplotlib.pyplot as plt

CUTOFF = .1
WIDTH = 0.03

data = pd.read_csv('2_19_test.csv')
us = data.ultra_sonic - data.ultra_sonic[0]
us = us/200

intervals = {'marissa_row_low': np.arange(734, 835),
             'marissa_row_mid': np.arange(854, 955),
             'marissa_row_high': np.arange(979, 1080),
             'marissa_row_no_pause': np.arange(1104, 1205)}

fig = plt.figure() # generate plot as figure

for name, inter in intervals.items():
    z_acc = data.z[inter] - data.z[inter[0]]
    thresh = np.std(z_acc)
    z_acc = [0 if z_acc_ < thresh else z_acc_ for z_acc_ in z_acc]
    z_vel = integrate.cumtrapz(z_acc, x=data.time[inter], initial=0)
    z_pos = integrate.cumtrapz(z_vel, x=data.time[inter], initial=0)
    low_N, low_Wn = signal.buttord(CUTOFF, CUTOFF+WIDTH, 3, 40)
    lowpass = signal.butter(low_N, low_Wn, 'lowpass',output='sos')
    pos_low = signal.sosfilt(lowpass, us[inter])
    hi_N, hi_Wn = signal.buttord(CUTOFF+WIDTH, CUTOFF, 3, 40)
    highpass = signal.butter(hi_N, hi_Wn, 'highpass', output='sos')
    pos_high = signal.sosfilt(highpass, z_pos)
    pos_comp = pos_low + pos_high
    plt.plot(pos_comp)
    plt.title('Marissa rows')
    plt.xlabel('samples (2Hz)')
    plt.ylabel('displacement (m)')
    plt.legend(intervals.keys())

fig.savefig('workout.png') 
