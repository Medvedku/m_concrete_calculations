import numpy as np
import pandas as pd
from functions import diff_2

d_y = pd.read_csv('d_y.csv')
if str(d_y.keys()[0]) == r'Unnamed: 0':
    d_y.pop(d_y.keys()[0])

keys = list(d_y.keys())

# for i in range(len(keys)-1):
#     xs = np.array(d_y[keys[0]])

dels = diff_2(y=np.array(d_y[keys[1]]), x=np.array(d_y[keys[0]]))[1]

frame = []

for i in range(len(keys)):
    if i ==0:
        frame.append(list(d_y[keys[i]]))
    else:
        frame.append(diff_2(y=list(d_y[keys[i]]), del_g=dels, g_l=True)[0])

frame = np.array(frame)
frame = np.transpose(frame)
df = pd.DataFrame(frame, columns=keys)
df.to_csv("fi.csv")
