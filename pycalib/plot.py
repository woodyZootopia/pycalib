import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def plotCamera(ax, R, t, c, scale):
    ps_c = np.array(([0,0,0], [1,1,3], [1,-1,3], [-1,-1,3], [-1,1,3]))
    ps_w = np.zeros((ps_c.shape))

    for i_p in range(ps_c.shape[0]):
        ps_w[i_p] = R.dot(scale*ps_c[i_p]) + t

    L01 = np.array([ps_w[0], ps_w[1]])
    L02 = np.array([ps_w[0], ps_w[2]])
    L03 = np.array([ps_w[0], ps_w[3]])
    L04 = np.array([ps_w[0], ps_w[4]])
    L1234 = np.array([ps_w[1], ps_w[2], ps_w[3], ps_w[4], ps_w[1]])
    
    ax.plot(L01[:,0], L01[:,1], L01[:,2], "-", color=c)
    ax.plot(L02[:,0], L02[:,1], L02[:,2], "-", color=c)
    ax.plot(L03[:,0], L03[:,1], L03[:,2], "-", color=c)
    ax.plot(L04[:,0], L04[:,1], L04[:,2], "-", color=c)
    ax.plot(L1234[:,0], L1234[:,1], L1234[:,2], "-", color=c)
