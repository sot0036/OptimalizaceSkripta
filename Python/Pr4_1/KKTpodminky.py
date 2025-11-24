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
    return sigmaD-(F/2-L/2*rho*g*x[0]*x[1])*L/2/(1/6*x[0]*x[1]**2)

def g4(x):
   return wD - (((F*L**3)/(48*E*1/12*x[0]*x[1]**3))+((5*rho*g*L**4)/((384*E*1/12*x[1]**2))))

def g5(x):
    return (np.pi**2*E*x[0]**3*x[1]/12)/(L**2)- P    
def g6(x):
    return (np.pi**2*E*x[0]*x[1]**3/12)/(L**2)- P  

def Var8gradL(x):
    gradL1 =rho*L*x[1]+x[2]*((-1/24*rho*g*L**2*x[0]*x[1]**3)-((F/2-rho*g*x[0]*x[1]*L/2)*L/2*(1/6*x[1]**2)))/(1/6*x[0]*x[1]**3)**2
    gradL2 =rho*L*x[0]+x[2]*((-1/24*rho*g*L**2*x[0]**2*x[1]**2)-((F/2-rho*g*x[0]*x[1]*L/2)*L/2*(1/3*x[0]*x[1])))/(1/6*x[0]*x[1]**3)**2
    return np.array([gradL1,gradL2,g3(x)])

def Var4(x):
    return np.array([g3(x),g4(x)])

def Var6(x):
    return np.array([g3(x),g5(x)])

def Var7(x):
    return np.array([g3(x),g6(x)])    

def Var10(x):
    return np.array([g4(x),g5(x)])
   
def Var11(x):
    return np.array([g4(x),g6(x)])  

def Var12gradL(x):
    gradL1 =rho*L*x[1]-x[2]/E*((3*F*L**3)/(48/12*x[0]*2*x[1]**3))
    gradL2 =rho*L*x[0]-x[2]/E*((3*F*L**3)/(48/12*x[0]*x[1]**4)+(15*rho*g*L**4)/(384/12*x[1]**3))
    return np.array([gradL1,gradL2,g4(x)])

def Var13(x):
    return np.array([g5(x),g6(x)])

x0=np.zeros(2)+100

bound=((10,10),(100,100))

solutionVar4 = spo.least_squares(Var4,x0,bounds=bound,)
xVar4 = solutionVar4.x
g5Var4 = g5(xVar4)
g6Var4 = g6(xVar4)

solutionVar6 = spo.least_squares(Var6,x0,bounds=bound)
xVar6 = solutionVar6.x

g4Var6 = g4(xVar6)
g6Var6 = g6(xVar6)

solutionVar7 = spo.least_squares(Var7,x0,bounds=bound)
xVar7 = solutionVar7.x

g4Var7 = g4(xVar7)
g5Var7 = g5(xVar7)

x0V8 = np.zeros(3)+100

bound8=((10,10,0),(100,100,10**12))
solutionVar8 = spo.fsolve(Var8gradL,x0V8)
xVar8 = solutionVar8
g4Var8 = g4(xVar8)

solutionVar10 = spo.least_squares(Var10,x0,bounds=bound)
xVar10= solutionVar10.x

g3Var10=g3(xVar10)
g6Var10=g6(xVar10)
mVar10=m(xVar10)*1000

solutionVar11 = spo.least_squares(Var11,x0,bounds=bound)
xVar11= solutionVar11.x

g3Var11=g3(xVar11)
g5Var11=g5(xVar11)
mVar11=m(xVar11)*1000


bound12=((10,10,0),(100,100,10**12))
solutionVar12 = spo.fsolve(Var12gradL,x0V8)
xVar12 = solutionVar12
g3Var12 = g3(xVar12)
g5Var12 = g5(xVar12)
g6Var12 = g6(xVar12)


solutionVar13 = spo.least_squares(Var13,x0,bounds=bound)
xVar13= solutionVar13.x

g3Var13=g3(xVar13)
g4Var13=g4(xVar13)

