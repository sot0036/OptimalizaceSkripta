import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib import patheffects

###
#Zadani
###

L=1500 # mm
E= 70000 # MPa
rho = 2.7*10**-9 # t/m^3
F = 5000 # N
g = 9810 # mm/s^2

###
#Omezeni
###
x1min = 10 # mm
x2min = 10 # mm

w_D=8 #mm
sigmaD= 100 # MPa
P = 20000 # N
###
Nx1 = 101 # Pocet dilku x1
Nx2 = 101 # Pocet dilku x2

x1 = np.linspace(x1min,100,Nx1) #Rovnomerne rozdeleni x1 pomoci Nx1 dilku
x2 = np.linspace(x2min,100,Nx2) #Rovnomerne rozdeleni x1 pomoci Nx1 dilku

###
# Priprava matic pro hodnoty cilove funkce a omezujici funkce
###
m = np.zeros([Nx2,Nx1])
w_F = np.zeros([Nx2,Nx1])
F_c = np.zeros([Nx2,Nx1])
sigma = np.zeros([Nx2,Nx1])

###
# Vypocet jednotlivych kandidatu
###

for i in np.arange(0,Nx1):
    for j in np.arange(0,Nx2):
        S = x1[i]*x2[j]
        m[j,i] = rho*L*S
        q = rho*g*S
        Mo = (F/2+q*L/2)*L/2-q*L**2/2
        Jz = 1/12*x1[i]*x2[j]**3
        Jy = 1/12*x1[i]**3*x2[j]
        w_F[j,i] = (F*L**3)/(48*E*Jz) + (5*q*L**4)/(384*E*Jz)
        F_c[j,i] = np.pi**2*E*min([Jz,Jy])/L**2
        sigma[j,i] = Mo/Jz * x2[j]/2

###
# Vykresleni vysledku
###
x1v,x2v = np.meshgrid(x1,x2) # priprava mrizky navrhovych promennych 
fig, ax = plt.subplots(figsize=(6, 6)) # priprava ramecku obrazku

# Vykresleni cilove funkce a vypsani hladin
objective = ax.contour(x1v,x2v,m*1000, cmap=cm.winter)
ax.clabel(objective,objective.levels,manual=[(30,30),(50,50),(70,70),(80,80),(90,90),(100,100)])

# Vykresleni hladiny w_D
pw_f = ax.contour(x1v,x2v,w_F,[w_D], colors="m")
pw_f.set(path_effects=[patheffects.withTickedStroke(angle=135)])
ax.clabel(pw_f,pw_f.levels,fmt="$w_F\leq w_D$ ")

# Vykresleni hladiny P
pF_c= ax.contour(x1v,x2v,F_c,[P],colors='g')
pF_c.set(path_effects=[patheffects.withTickedStroke(angle=240)])
ax.clabel(pF_c,pF_c.levels,fmt="$F_c \geq P$",manual=[(50,30)])

# Vykresleni hladiny \sigma
pSigma = ax.contour(x1v,x2v,sigma,[sigmaD],colors='k')
pSigma.set(path_effects=[patheffects.withTickedStroke(angle=100)]) 
ax.clabel(pSigma,pSigma.levels,fmt="$\sigma \leq \sigma_D$",manual=[(60,40)])

# Priprava popisu obrazku
plt.title("Grafický výpočet hmotnosti nosníku (kg)")
plt.xlabel("$x_1$ (mm)")
plt.ylabel("$x_2$ (mm)")

#Ulozeni obrazku
plt.savefig("Pr12_bez.pdf") 