import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go
import psutil
import matplotlib.ticker as ticker
from scipy.interpolate import interp1d

f_pebs='./out/out.txt'

# PEBS
is_init = 0
init_t = 0
time_duration=0
with open(f_pebs) as fp:
    line = fp.readline()
    for line in fp:
        line = line.split()

        # 3 : time
        # 14 : physical address

        #print(line)
        if(line[2][0] == '['):
            tempt = line[3].split('.')
        elif(line[3][0] == '['):
            tempt = line[4].split('.')
        else:
            tempt = line[5].split('.')

        cur_time = int(tempt[0])

        if(is_init is 0):
            init_t = cur_time
            is_init = 1
        if(cur_time < init_t):
            init_t = cur_time
        if(cur_time-init_t+1 > time_duration):
            time_duration = cur_time - init_t + 1

#print(time_duration)
FT=4
ROW=512*FT
DIV=142606336/FT

data_pebs = np.zeros((ROW, time_duration+1), dtype=np.int64)

# PEBS
with open(f_pebs) as fp:
    line = fp.readline()

    for line in fp:
        line = line.split()

        if(line[2][0] == '['):
            tempt = line[3].split('.')
            tempa = line[14].split(',')
            paddr = int(tempa[0], 16)
        elif(line[3][0] == '['):
            tempt = line[4].split('.')
            tempa = line[15].split(',')
            paddr = int(tempa[0], 16)
        else:
            tempt = line[5].split('.')
            tempa = line[16].split(',')
            paddr = int(tempa[0], 16)

        cur_time = int(tempt[0])

        # 14 : LDA
        if((paddr == 0)):
            continue
        if((paddr > 73014444032)):
            continue

        pa_idx = int(paddr/DIV)
        if(data_pebs[pa_idx, cur_time - init_t +1] < 10):
            data_pebs[pa_idx, cur_time - init_t +1] += 1


filename = './out/np'
np.save(filename, data_pebs)
print('Heatmap np gen compeleted')
