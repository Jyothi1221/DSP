import matplotlib.pyplot as plt
import numpy as m
f=input("enter the freq")
fs=input("enter sample freq")
n=m.arange(0,10,0.25)
A=m.sin((2*m.pi*f*n)/fs)
plt.title("sampled sine wave")
plt.xlabel("---->time")
plt.ylabel("---->Amplitude")
plt.stem(n,A)
plt.show( )
