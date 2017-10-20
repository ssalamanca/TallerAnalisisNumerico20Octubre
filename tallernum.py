import sympy as sy
import scipy.integrate as integrate
import math

def integrar(a,b):
    x2= lambda x: math.sqrt(x)*math.sin(x)
    print (integrate.quad(x2,0,4))
    
def f(x):
    return math.sqrt(x)*math.sin(x)

def trapecios(a,b,m):
    h = (b -a) / m
    s = 0
    for i in range(1,m):
        s = s + f(a + i * h)
        r = h / 2 *(f(a)+2*s+f(b))
    return r

a=0
b=2
m=[10,100,1000]
for i in range(0,2):
    r=trapecios(a,b,m[i])
    z=integrar(a,b)
    """t = ((-((b-a)/m[i])**2)/12)(b-a)**3"""
    e=z-r
    print('%18.15s %18.15s %18.15s'%(r,z,e))


