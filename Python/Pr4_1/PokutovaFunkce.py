import numpy as np
import scipy.optimize as spo

L = 1500
F =5000
P = 20000
sigmaD = 100
wD = 8
rho = 2.7*10**-9
g = 9810
E = 70000

def m(x):
    return x[0]*x[1]*L*rho

def g3(x):
    return (sigmaD-(F/2-L/2*rho*g*x[0]*x[1])*L/2/(1/6*x[0]*x[1]**2))/sigmaD

def g4(x):
   return (wD - (((F*L**3)/(48*E*1/12*x[0]*x[1]**3))+((5*rho*g*L**4)/((384*E*1/12*x[1]**2)))))/wD

def g5(x):
    return ((np.pi**2*E*x[0]**3*x[1]/12)/(L**2)- P)/P    
def g6(x):
    return ((np.pi**2*E*x[0]*x[1]**3/12)/(L**2)- P)/P  

def Pfun(x,R):
    gT1 = R*(np.min((x[0]-10,0)))**2
    gT2 = R*(np.min((x[1]-10,0)))**2  
    gT3 = R*(np.min((g3(x),0)))**2
    gT4 = R*(np.min((g4(x),0)))**2
    gT5 = R*(np.min((g5(x),0)))**2
    gT6 = R*(np.min((g6(x),0)))**2
    return m(x)+gT1+gT2+gT3+gT4+gT5+gT6
err = 1
tol=10**-3
x0 =np.array([100,100])
R=10000
solution = spo.minimize(Pfun, x0,args=(R))

xN=solution.x
print(xN)
print(solution.success)
print(m(xN)*1000)

    
    
    
    
    
    
