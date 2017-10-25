from scipy import integrate as inte
import math
def f(x):
    return x*math.exp(x)

a=1
b=2
x1=(-(b-a)/2)*(1/math.sqrt(3))+(b+a)/2
x2=((b-a)/2)*(1/math.sqrt(3))+(b+a)/2
A=(1/2)*(f(x1)+f(x2))
real=(inte.quad(lambda x: x*math.exp(x) , 1, 2))[0]
er=real-A
print('%18s %18s %18s'%("cuad Gauss","real","error"))
print('%18s %18s %18s'%(A,real,er))


