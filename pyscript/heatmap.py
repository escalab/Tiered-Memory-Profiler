import sys
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from matplotlib.ticker import FormatStrFormatter
import seaborn as sns
import pandas as pd
import plotly.graph_objects as go
import psutil
from scipy.interpolate import interp1d
from matplotlib.ticker import (AutoMinorLocator, MultipleLocator)

FT=4
ROW=512*FT

# heatmap
def plot_heatmap(data1, h1):
    plt.clf()

    plt.imshow(data1[:, 1:], cmap='Blues', aspect='auto')
    cb1 = plt.colorbar()
    cb1.ax.tick_params(labelsize=5)

    yt = np.empty(18, dtype='object')
    yt[0] = '0x000000000'
    for x in range(18):
        if(x is 0):
            continue
        h_x = x*0x100000000
        yt[x] = str(hex(h_x))
    plt.yticks(range(ROW)[::30*FT], yt, fontsize=6)
    plt.ylabel("Physical Address")
    plt.xlabel("Time (sec)")
    plt.tight_layout()
    plt.savefig('./out/heatmap.pdf', dpi=300)

f_pebs='./out/np.npy'
data_pebs = np.load(f_pebs)

plot_heatmap(data_pebs, 'PEBS')
