
# coding: utf-8

# In[ ]:

import scipy.integrate as sci
import numpy as np
import matplotlib.pyplot as plt
get_ipython().magic('matplotlib inline')

y0 = [1,0]
t= np.linspace(0,10)
m = 1
g = 1
l = 1
paras = (m,g,l)

def f(y,t,*args):
    #second value passed is the velocity
    d1 = y[1]
    #acc is defined by: -gsin(theta) / l based on derived formula
    d2 = ( (-1) * args[1] * np.sin(y[0]) ) / args[2]
    return [d1,d2]
theta = sci.odeint(f,y0,t,args = paras)
plt.plot(t, theta[:,0])

