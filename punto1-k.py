# -*- coding: cp1252 -*-
import matplotlib.pyplot as plt
import numpy as np
import scipy.interpolate as sp
def D_ade(a,b,c):
    return (-(c)+(4*b)-(3*a))/2*0.01

def D_atr(a,b,c):
    return ((3*a)-(4*b)+(c))/2*0.01

# t es x
t =  [1.00,1.01,1.02,1.03,1.04]
# i es f(x)
i =  [3.1,3.12,3.14,3.18,3.24]

R=0.142
L=0.98

for x in range(0, 3):
    d = D_ade(i[x],i[x+1],i[x+2])
    v = (L*d)+(R*i[x])
    print(v)

for x in range(2, 4):
    d = D_atr(i[x],i[x-1],i[x-2])
    v = (L*d)+(R*i[x])
    print(v)

plt.plot(t,i)
plt.show()
print()




