###
#Knihovna pro reseni metody optimalizace nulteho radu
###
import numpy as np


def Swann(fun,x0,Delta=0.1):  
    x = np.empty([20])
    x[0] = x0
    f0 = fun(x0)
    fL= fun(x0-Delta)
    fP=fun(x0+Delta)
    f= np.empty([20])
    f[0] = f0
    if fL > f0 > fP:
        for i in np.arange(20):
            x[i+1] = x[i] + 2**i * Delta
            f[i+1]= fun(x[i+1])
            if f[i+1]>f[i]:
                a=x[i-1]
                b=x[i+1]
                break
        
    elif fL < f0 < fP:
        for i in np.arange(20):
            x[i+1] = x[i] - 2**i * Delta
            f[i+1]= fun(x[i+1])
            if f[i+1]>f[i]:
                a=x[i+1]
                b=x[i-1]
                break       
    elif fL > f0 < fP:
        a = x0-Delta
        b = x0+Delta
    
    try: a,b
    except NameError: a,b = None
    if b == None and a == None:
        print("Nenašlo se rešení v okolí $x_0$")
    else:
        return a,b

def PuleniInt(fun,a,b,tol=0.01,flag=1):
    delta = 1
    i = 0 
    while delta > tol:
        L = (b-a)
        xL = a+1/4*L
        xM = (a+b)/2
        xP = b-1/4*L
        
        fL = fun(xL)
        fM = fun(xM)
        fP = fun(xP)
        
        if fL < fM:
            b = xM
        elif fP < fM:
            a = xM
        else:
            a = xL
            b = xP
        
        delta = (b-a)/2
        i+=1
        
    xStar = (b+a)/2
    if flag == 1: print (f"Optimum pomocí metody půlení intervalu se nachází {xStar:0.5f} +/- {delta:0.5f}.\nPro vypočet bylo nutné {i} iterací.\n")
    return xStar,delta

def ZlatyRez(fun,a,b,tol=0.01,flag=1):
    delta = 1
    phi = (-1+5**(1/2))/2
    i = 0
    while delta > tol:
        xL = b-(b-a)*phi
        xP = a+(b-a)*phi
        
        fL = fun(xL)
        fP = fun(xP)
        
        if fL < fP:
            b = xP
        else:
            a = xL
        delta = (b-a)/2
        i +=1    
    xStar = (b+a)/2
    if flag == 1: print (f"Optimum pomocí metody půlení intervalu se nachází {xStar:0.5f} +/- {delta:0.5f}.\nPro vypočet bylo nutné {i} iterací.\n")        
    return xStar, delta

def KvadApro(fun,x1,x2,x3,flag=1): ## 

    f1 = fun(x1)
    f2 = fun(x2)
    f3 = fun(x3)
    
    a0 = f1
    a1 = (f2-f1)/(x2-x1)
    a2 = 1/(x3-x2)*((f3-f1)/(x3-x1) - (f2-f1)/(x2-x1))
    
    a = np.array([a0,a1,a2])
    xOver = (x1+x2)/2-a1/(2*a2)
    
    if flag == 1: print (f"Odhad optima funkce je {xOver:0.5f}.\n")        
    
    return xOver, a

def PowellMetoda(fun,x1,Delta=0.1,tol=0.01,flag=1):
    ErrF = 1
    ErrX = 1
    i=0
    while ErrF > tol and ErrX > tol:
        
        x2 = x1 + Delta 
        f1 = fun(x1)
        f2 = fun(x2)
        
        if f1 > f2:
            x3 = x1+2*Delta
            flagx3 = 0
        else:
            x3=x1-Delta
            flagx3 = 1
        f3 = fun(x3) 
        Fmin = np.min([f1,f2,f3])
        Xmin = x1 if Fmin==f1 else x2 if Fmin==f2 else x3
        
        xOver = KvadApro(fun,x1,x2,x3,flag=0)[0]
        
        if flagx3 == 0:
            print ("xOver je extrapolovane") if xOver > x3 else None
        elif flagx3 == 1:           
            print ("xOver je extrapolovane") if xOver < x3 else None
            
        
        ErrF = np.abs(Fmin - fun(xOver))
        ErrX = np.abs(Xmin - xOver)
        x1=xOver
        i+=1
    if flag == 1: print (f"Odhad optima funkce je {xOver:0.5f}.\nPro aproximaci bylo nutné {i} iterací.\n")
    return xOver


if __name__ == "__main__":
    print("TestKnihovny")