import sys
import os
import csv
import pandas as pd
import numpy as np

times = ["L", 0.2, 0.4, 0.7, 1., 1.2, 1.4, 1.7, 2., 2.2, 2.4, 2.7, 3., 3.2, 3.4, 3.7, 4., 4.2, 4.4, 4.7, 5., 5.2, 5.4, 5.7, 6., 6.2, 6.4, 6.7, 7., 35.8, 64.6, 79.72, 85.012, 90.304, 98.242, 110.15, 116.4, 122.65, 132.03, 136.95, 141.87, 146.8, 148.27, 149.74, 150.37, 151.]
times = [str(i) for i in times]


# path_ = r'E:\Ansys\Beton\results'
# path_ = r'D:\Ansys\Beton\Beton\results'

path_ = r'D:\Ansys\Beton\Beton\results\plastelina'

obsah = os.listdir()

el = len(times) - 1

frame = []
#Prvý riadok
f = open("d_y0.txt", "r")
data = f.readlines()
row_ = []
for i in data[1:]:
    row_.append(i.split()[0])
frame.append(row_)

for i in range(el):
    f = open("d_y{0}.txt".format(i), "r")
    data = f.readlines()
    row_ = []
    for i in data[1:]:
        row_.append(i.split()[-1])
    frame.append(row_)

frame = np.array(frame)
frame = np.transpose(frame)
df = pd.DataFrame(frame, columns = times)
df.to_csv("d_y.csv")

print(df)
