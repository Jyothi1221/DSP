import matplotlib.pyplot as plot
import numpy as n
f1=5
f2=2
fs=20
x=n.arange(0,10,0.01)
a=n.sin((2*n.pi*f1*x)/fs)
plot.subplot(3,1,1)
plot.plot(x,a)
plot.title("sine 1")
plot.xlabel("---->time")
plot.ylabel("---->Amplitude")

b=n.sin((2*n.pi*f2*x)/fs)
plot.subplot(3,1,2)
plot.plot(x,b)
plot.title("sine 2")
plot.xlabel("---->time")
plot.ylabel("---->Amplitude")

c=a+b
plot.subplot(3,1,3)
plot.plot(x,c)
plot.title("sum of two waves")
plot.xlabel("---->time")
plot.ylabel("---->Amplitude")
plot.show( )
