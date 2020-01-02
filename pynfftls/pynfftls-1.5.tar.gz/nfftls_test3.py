from pynfftls import *
import numpy as np
import matplotlib.pyplot as plt
import math



# sinusoidal function 
nu0 = 0.1e-3
a0 = 1.

# sampling
dt=50.

# duration in days
duration = 100.

# over-sampling factor
over = 10

T = duration*86400.

# number of measurements
n = int(round(T/dt))

# time series
t = np.arange(n)*dt


hifac = 1.
sig = 1

y =a0*np.cos(2.*math.pi * nu0 * t)   

nf = n/2*over # number of positive frequencies

(f2,p2) = nfft(t,y,nf,over=over)


(f,p) = period(t,y,over,hifac)


p2 = np.abs(p2[0:nf])**2/np.var(y)/float(n)
f2 = f2[0:nf]

plt.figure(1)
plt.clf()
plt.plot((f-nu0)*1e6,p,'k')
plt.plot((f2-nu0)*1e6,p2,'r')
plt.axis(xmin=-1,xmax=1)

plt.figure(2)
plt.clf()
plt.plot(f*1e6,p,'k')
plt.plot(f2*1e6,p2,'r')


plt.show(block=False)

