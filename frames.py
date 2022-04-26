import uu
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d as plt3d
from matplotlib import cm
from functions import Force_1

# fig, ax = plt.subplots(subplot_kw={"projection": "3d"})

fig = plt.figure(figsize=(19, 19))
ax = plt.axes(projection='3d')


np.set_printoptions(3)

fi = pd.read_csv('fi.csv')
if str(fi.keys()[0]) == r'Unnamed: 0':
    fi.pop(fi.keys()[0])

d_y = pd.read_csv('d_y.csv')
if str(d_y.keys()[0]) == r'Unnamed: 0':
    d_y.pop(d_y.keys()[0])

eps = pd.read_csv('eps.csv')
if str(eps.keys()[0]) == r'Unnamed: 0':
    eps.pop(eps.keys()[0])

sig = pd.read_csv('sig.csv')
if str(sig.keys()[0]) == r'Unnamed: 0':
    sig.pop(sig.keys()[0])

yolo = pd.read_csv('yolo.csv')
if str(yolo.keys()[0]) == r'Unnamed: 0':
    yolo.pop(yolo.keys()[0])


def frame_plot(frame):
    fig, ax = plt.subplots()
    keys = list(frame.keys())
    xs = list(frame[keys[0]])
    for i in range(len(keys)-1):
        ys = list(frame[keys[i+1]])
        ax.plot(xs, ys, linewidth=0.3, label=str(keys[i+1]))

ax.set_ylabel("Lenght [m]")
ax.set_xlabel("Load [N]")
ax.set_zlabel("Deflection [m]")

# Remove gray panes and axis grid
ax.xaxis.pane.fill = False
ax.xaxis.pane.set_edgecolor('white')
ax.yaxis.pane.fill = False
ax.yaxis.pane.set_edgecolor('white')
ax.zaxis.pane.fill = False
ax.zaxis.pane.set_edgecolor('white')
ax.grid(False)
# Remove z-axis
ax.w_zaxis.line.set_lw(0.01)
ax.set_zticks([])


def create_frame_surface(frame):
    Y = list(frame[frame.keys()[0]])
    X_str = frame.keys()[1:]
    # X = [float(i) for i in X_str]
    X = [Force_1(float(i)) for i in X_str]
    X, Y = np.meshgrid(X, Y)
    Z = np.array(frame)

    Z = np.delete(Z, 0, axis=1)

    return X, Y, Z

print(fi.keys())

X, Y, Z = create_frame_surface(eps)

# ax.plot_surface(X, Y, -Z, cmap=cm.coolwarm, linewidth=0, antialiased=True, alpha=0.5)
ax.plot_wireframe(X, Y, -Z, color="k",
                           linewidth=0.5, antialiased=True, alpha=0.5)

ax.view_init(25, -30)
plt.tight_layout()
plt.show()
# yolo
