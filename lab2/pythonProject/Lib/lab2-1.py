import matplotlib.pyplot as plt
import numpy as np
from PyFunkcijos import *

def gradientas(x): # gradiento funkcija
    dx0 = (tikslumas([x[0] + 1e-13, x[1]]) - tikslumas(x)) / 1e-13
    dx1 = (tikslumas([x[0], x[1] + 1e-13]) - tikslumas(x)) / 1e-13
    return np.array([dx0, dx1])

def tikslumas(x): # grazina tiksluma
    return (lygciuSistema(x) ** 2).sum()

def greiciausio_nusileidimo(funkcija): # metodas
    alpha = 0.01 # žingsnio dydis
    x = np.array([0, 3.5])
    g = gradientas(x)
    for i in range(180):
        buv_tikslumas = tikslumas(x) # išsisaugom buvusį tikslumą
        x = x - alpha * g # nauja kryptis

        if tikslumas(x) > buv_tikslumas: # tikrinam ar naujas tikslenis
            x = x + alpha * g  # atgalinis žingsnis
            g = gradientas(x)  # perskaičiuoja gradienta
            x = x - alpha * g  # nauja kryptis

        print(f'iteracijos: {i} tikslumas: {tikslumas(x)}')

        if tikslumas(x) < 1e-25: break # tinkamas tikslumas - stabdom

    print(f'Funkcijos reiksme: {funkcija(x)}')
    print(f'x = {x}')

def lygciuSistema(x):  # grazina reiksmiu stulpeli
    return np.array([
        [0.1 * x[0] ** 3 - 0.3 * x[0] * (x[1] ** 2)],
        [x[0] ** 2 + x[1] ** 2 + 5 * np.cos(x[0]) - 16]
    ])

greiciausio_nusileidimo(lygciuSistema)

# ----------------------------------
fig1 = plt.figure(1, figsize=plt.figaspect(0.5))
fig2 = plt.figure(2, figsize=plt.figaspect(0.5))
fig3 = plt.figure(3, figsize=plt.figaspect(0.5))
fig4 = plt.figure(4, figsize=plt.figaspect(0.5))
ax1 = fig1.add_subplot(projection='3d')
ax1.set_xlabel('x')
ax1.set_ylabel('y')
ax1.set_ylabel('z')
ax2 = fig2.add_subplot(projection='3d')
ax2.set_xlabel('x')
ax2.set_ylabel('y')
ax2.set_ylabel('z')

ax3 = fig3.add_subplot(projection='3d')
ax3.set_xlabel('x')
ax3.set_ylabel('y')
ax3.set_ylabel('z')

ax4 = fig4.add_subplot(projection='3d')
ax4.set_xlabel('x')
ax4.set_ylabel('y')
ax4.set_ylabel('z')

xx = np.linspace(-15, 15, 400)
yy = np.linspace(-15, 15, 400)
X, Y = np.meshgrid(xx, yy)
Z = Pavirsius(X, Y, lygciuSistema)

surf1 = ax1.plot_surface(X, Y, Z[:, :, 0], color='red', alpha=0.4)

surf1 = ax3.plot_surface(X, Y, Z[:, :, 0], color='red', alpha=0.4)

surf2 = ax1.plot_surface(X, Y, Z[:, :, 1], color='green', alpha=0.4)

surf2 = ax4.plot_surface(X, Y, Z[:, :, 1], color='green', alpha=0.4)


CS11 = ax1.contour(X, Y, Z[:, :, 0], [0], colors='g')
CS12 = ax1.contour(X, Y, Z[:, :, 1], [0], colors='r')
CS1 = ax2.contour(X, Y, Z[:, :, 0], [0], colors='g')
CS2 = ax2.contour(X, Y, Z[:, :, 1], [0], colors='r')

XX = np.linspace(-15, -15, 2)
YY = XX
XX, YY = np.meshgrid(XX, YY)
ZZ = XX * 0
zeroplane = ax2.plot_surface(XX, YY, ZZ, color='gray', alpha=0.4, linewidth=0, antialiased=True)

plt.show()