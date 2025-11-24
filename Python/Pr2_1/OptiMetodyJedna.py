###
# Knihovna pro reseni metody optimalizace nulteho radu
###
import numpy as np
def cdiff(fun,x,h=10**-5):    
    return (fun(x+h)-fun(x-h))/(2*h)

def cdiff2(fun,x,h=10**-5):
    return (fun(x+2*h)-2*fun(x)+fun(x-2*h))/(4*h**2)

def Bisekce(fun,a,b,tol=0.01,flag=1):
    dfM = 1
    i=0
    while np.abs(dfM) > tol:
        i +=1
        xM = (b+a)/2
        dfM = cdiff(fun,xM)
        if np.abs(dfM) < tol:
            break
        if dfM <0:
            a = xM
        else:
            b = xM
    delta = (b-a)/2
    if flag == 1: print (f"Optimum pomocí metody sečny se nachází {xM:0.5f} +/- {delta:0.5f}.\nPro vypočet bylo nutné {i} iterací.\n")
    

    return xM,delta

def Secant(fun,a,b,tol=0.01,flag=1):
    dfs = 1
    i=0
    while np.abs(dfs) > tol:
        i +=1
        dfa = cdiff(fun,a)
        dfb = cdiff(fun,b)
        xs = b - (dfb*(b-a))/(dfb-dfa)
        dfs = cdiff(fun,xs)
        if np.abs(dfs) < tol:
            break
        if dfa*dfs >0:
            a = xs
        else:
            b = xs
        
    delta = (b-a)/2 
    if flag == 1: print (f"Optimum pomocí metody sečny se nachází {xs:0.5f} +/- {delta:0.5f}.\nPro vypočet bylo nutné {i} iterací.\n")

    return xs,delta

def NewtonRaphson(fun,xk,tol=0.01,flag=1):
    err = 1
    i=0
    while err > tol:
        i+=1
        x0=xk
        xk=x0-cdiff(fun, x0)/cdiff2(fun, x0)
        err =np.abs(cdiff(fun, x0))   

    if flag == 1: print (f"Optimum pomocí metody NewtonRapson se nachází {xk:0.5f}.\nPro vypočet bylo nutné {i} iterací.\n")
    
    return xk