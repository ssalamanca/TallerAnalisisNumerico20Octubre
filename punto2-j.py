from scipy import integrate as inte
import math
def g(x):
    return x*math.exp(x)

a=1
b=a+1/4
AF=0
for j in range(0,4):
  x1=(-(b-a)/2)*(1/math.sqrt(3))+(b+a)/2
  x2=((b-a)/2)*(1/math.sqrt(3))+(b+a)/2
  A1 = ((b-a)/2)*(g(x1)+g(x2))
  AF = AF+A1
  a=a+1/4
  b=b+1/4
  
real=(inte.quad(lambda x: x*math.exp(x) , 1, 2))[0]
er = real-AF
print('%18s %18s %18s'%("cuad Gauss","real","error"))
print('%18s %18s %18s'%(AF,real,er))
