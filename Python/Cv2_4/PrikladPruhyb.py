###
# Zadani
###
import numpy as np
import matplotlib.pyplot as plt

D = 30
E = 200000
a = 500
b = 300

q = 5
F = 1000

Ra = (q*(a**2/2+a*b)-F*b)/(a+b)
Rb = (q*(a**2/2)-F*a)/(a+b)

Jz = np.pi/64*D**4

C3 = 1/(E*Jz*(-a-b))*(Rb*(-b**2*a/2-b**3/6)+Ra*(a**3/6-a**3/2)-q*(a**4/24-a**4/6))
C1 = 1/(E*Jz)*(Rb*b**2/2+Ra*a**2/2-q*a**3/6)-C3


def pruhyb(x,Ra,Rb,q,C1,C3,a,b,E,Jz):
    w=np.empty(len(x))
    i=-1
    for xi in x:
        i+=1
        if xi < a:
            w[i] = -(Ra*xi**3/6-q*xi**4/24)/(E*Jz)+C1*xi
        else:
            w[i] = -(Rb*(a+b-xi)**3/6)/(E*Jz)+C3*(a+b-xi)
    return w

x = np.linspace(0,a+b,1000)

w = pruhyb(x,Ra,Rb,q,C1,C3,a,b,E,Jz)

plt.plot(x,w)