import sympy as sy
import scipy.integrate as integrate
import math

def integrar(a,b):
    x2= lambda x: math.sqrt(x)*math.sin(x)
    print (integrate.quad(x2,0,4))
    return (integrate.quad(x2,0,4))
    
def f(x):
    return math.sqrt(x)*math.sin(x)

def trapecios(a,b,m):
    h = (b -a) / m
    s = 0
    for i in range(1,m):
        s = s + f(a + i * h)
        print(s)
    r = h / 2 *(f(a)+2*s+f(b))
    return r

a=0
b=2
m=[10,100,1000]
for i in range(0,3):
    print(i)
    r=trapecios(a,b,m[i])
    z=integrar(a,b)
    #print(z[0])
    #print(z[1])
    res=z[1]-z[0]
    print(res)
    """t = ((-((b-a)/m[i])**2)/12)(b-a)**3"""
    e=res-r
    print('%18.15f %18.15f %18.15f'%(r,res,e))


