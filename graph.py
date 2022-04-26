import sys
import os
import csv
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


fig, ax = plt.subplots()

times = [ 0.2, 0.4, 0.7, 1., 1.2, 1.4, 1.7, 2., 2.2, 2.4, 2.7, 3., 3.2, 3.4, 3.7, 4., 4.2, 4.4, 4.7, 5., 5.2, 5.4, 5.7, 6., 6.2, 6.4, 6.7, 7., 35.8, 64.6, 79.72, 85.012, 90.304, 98.242, 110.15, 116.4, 122.65, 132.03, 136.95, 141.87, 146.8, 148.27, 149.74, 150.37, 151.]

times = [str(i) for i in times]

el = len(times)
frame = []
#Prvý riadok
f = open("sig0.txt", "r")
data = f.readlines()
xs = []
for i in data[1:]:
    xs.append(float(i.split()[0]))

for i in range(el):
    f = open("sig{0}.txt".format(i), "r")
    data = f.readlines()
    ys = []
    for i in data[1:]:
        ys.append(float(i.split()[-1]))
    ax.plot(xs, ys, linewidth=.3)

plt.show()

def derivate(lst):
    pass
