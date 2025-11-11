
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import cm
plt.rcParams["svg.fonttype"] = ('none')
plt.rcParams['font.family']='CMU Serif'
# Zadani
L1 = 120 #mm
L2 = 80 #mm
k1 = 10 #N/mm
k2 = 100 #N/mm
F = 10 #N

Nx1=100+1 #Pocet dilku pro vykresleni x1
Nx2=100+1 #Pocet dilku pro vykresleni x2
x1 = np.linspace(0,5,Nx1) #Rovnomerne rozdeleni x1 pomoci Nx1 dilku
x2 = np.linspace(15,20,Nx2) #Rovnomerne rozdeleni x2 pomoci Nx2 dilku

x1v,x2v = np.meshgrid(x1,x2) #Priprava mrizky pro vypocet

# Celkova potencialni energie systemu
Energie=1/2*k1*(np.sqrt((L1+x1v)**2+(x2v)**2)-L1)**2+\
1/2*k2*(np.sqrt((L2-x1v)**2+(x2v)**2)-L2)**2-\
F*x2v

minimum = np.min(Energie) # maximum na rozsahu mrizky
maximum = np.max(Energie) # minimum na rozsahu mrizky

# Hledani indexu minima potencialni energie
ind = np.unravel_index(np.argmin(Energie, axis=None), Energie.shape)

# Nastaveni urovne barevne mapy
levels1= np.linspace(minimum,minimum+60-1,5)
levels2= np.linspace(minimum+60,maximum,50)
levels=np.concat((levels1,levels2))
# Vypsani vysledku x1 a x2
print(f"Navrhova promena x1 = {x1[ind[1]]:0.2f}")
print(f"Navrhova promena x2 = {x2[ind[0]]:0.2f}")

# Vykresleni vysledku jako 3D plocha
fig, ax = plt.subplots(subplot_kw={"projection": "3d"})
surface = ax.plot_surface(x1v,x2v,Energie/maximum,cmap=cm.jet)
ax.grid(False)
ax.set_zticks([])
plt.ylabel("$x_{2}$",fontsize=12)
plt.xlabel("$x_{1}$",fontsize=12)
plt.savefig("Priklad1_1_3D_final.pdf")
# Vykresleni vysledku jako 2D konturova plocha
plt.figure(2)
plt.contour(x1v,x2v,Energie,levels, cmap=cm.jet)
plt.ylabel("$x_{2}$",fontsize=12)
plt.xlabel("$x_{1}$",fontsize=12)
# Vykresleni optima x*
plt.plot(x1[ind[1]],x2[ind[0]],'r*')
offset = 50
bbox = dict(boxstyle="round", fc="0.8")
arrowprops = dict(arrowstyle="->",connectionstyle="angle,angleA=0,angleB=90,rad=10")
plt.annotate(f'Optimum [{x1[ind[1]]:0.2f}; {x2[ind[0]]:0.2f}]', (x1[ind[1]],x2[ind[0]]), xytext=(0.5*offset, -offset), textcoords='offset points',bbox=bbox,arrowprops=arrowprops,fontsize=12)

plt.savefig("Priklad1_1_2D_final.pdf")