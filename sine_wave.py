import matplotlib.pyplot as plot
import numpy as m
f=input("enter the value")
fs=input("enter the value")
n=m.arange(0,10,0.25)
A=m.sin((2*m.pi*f*n)/fs)
plot.plot(n,A)
plot.title("sine wave")
plot.xlabel("---->time")
plot.ylabel("---->Amplitude")
plot.show( )
