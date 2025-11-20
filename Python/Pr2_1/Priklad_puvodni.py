import numpy as np
import matplotlib.pyplot as plt
from OptiMetodyNula import *
from OptiMetodyJedna import *
###
# Zadani
###

x0 = 0
 

def myfun(x):
    return (0.01*x**4-0.5*x**2-x+10)

def funApro(x,a,xL,xP):
    return a[0]+a[1]*(x-xL)+a[2]*(x-xL)*(x-xP)

##
# Hledani interval unimodalni funkce
##
a,b = Swann(myfun,x0)

# Metoda puleni intervalu
xOptiPI,delta = PuleniInt(myfun,a,b)

# Metoda zlateho rezu
xOptiZR,delta = ZlatyRez(myfun,a,b)

# Metoda kvadraticke aproximace
xOver,aK = KvadApro(myfun, a,(a+b)/2, b)

# Powellova metoda
xOptiPM = PowellMetoda(myfun,(a+b)/2)

# Metoda bisekce
xOptiBi = Bisekce(myfun, a, b)[0]

# Metoda secny
xOptiSe = Secant(myfun, a, b)[0]

# Metoda secny
xOptiSe = NewtonRapson(myfun, (a+b)/2)