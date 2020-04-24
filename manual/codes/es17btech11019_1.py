import numpy as np
from scipy import signal
import matplotlib.pyplot as plt
from matplotlib.pyplot import *

s1= signal.ZerosPolesGain([],[-1,-1,-1],[100])
w,H=signal.freqresp(s1)
plt.figure()
plt.plot(H.real,H.imag,"b")
plt.plot(H.real,-H.imag,"r")
plt.show()