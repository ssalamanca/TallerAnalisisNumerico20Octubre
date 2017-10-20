import math
def f(x):
    return math.log1p(x)

x0=1.8
h=[0.1,0.01,0.001,0.0001,0.00001]
for i in range(0,5):
    res = (f(x0+h[i])-f(x0))/h[i]-((-1/x0**2)/2)*h[i]
    print(res)
