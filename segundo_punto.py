from math import*
import matplotlib.pyplot as plt
def f(x):return x*exp(x)
r=5.436563656918091
h=0.1
listH= []
listY=[]
for i in range(15):
    d=(f(1+h)-f(1))/h
    listH.append(h)
    listY.append(e)
    e=abs(r-d)
    print('%18.15f %18.15f %18.15f %18.15f'%(h,r,d,e))
    h=h/10
"""
for i in range(15):
    print (listH[i])
    print(listY[i])
"""
plt.plot(listH,listY)
plt.plot(listH, listY, 'k:', linewidth = 2)
plt.show()

