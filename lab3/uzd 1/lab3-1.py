import numpy as np
from numpy import sin, cos, arccos, pi
import matplotlib.pyplot as plt
import sympy as sym

plt.style.use('ggplot')

# duota uzd funkcija
def funkcija(x): return cos(2 * x) / (sin(2 * x) + 1.5) - x / 5
# daugianario formulė
def ciobysevo_daugianaris(x, i): return cos(arccos(x) * i)
# daugianario funkcija formulė spausdinimui
def sym_ciobysevo_daugianaris(x, i): return sym.cos(sym.acos(x) * i)
# duota cb interpoliavimo intervalo formulė
def ciobysevo_intervalas(x, a, b): return (2 * x) / (b - a) - (b + a) / (b - a)
#cb mazgo transformacija
def ciobysevo_mazgas(i, pr, pb, n): # Paskirsto interpoliavimo taškus
    # i - iteracijos, pr - pradžia, pb - pabaiga, n - mazgų skaičius.
    return ((pb - pr) / 2) * cos(pi * (2 * i + 1) / (2 * n)) + ((pb + pr) / 2)

# spausdinimas
def spausdinti_ciobysevo(i, koffs):
    x = sym.Symbol('x')
    koffs = koffs.flatten()
    xc = ciobysevo_intervalas(x, -2, 3)
    for i in range(len(koffs)):
        A = sym_ciobysevo_daugianaris(xc, i)
        if i == 0:
            print(str(koffs[i]) + ' +')
        elif i == 1:
            print(str(koffs[i]) + ' * (' + str(A) + ') +')
        else:
            print(str(koffs[i]) + ' * ' + str(A) + ' +')

print('Pasirinkite taškų išdėstymo tipą:')
print('Tolygiai - tl')
print('Čiobyševo - cb')

n = 15 # interpoliavimo taškų skaičius
i = np.arange(n) # nuo 0 iki 14

if str(input("Pasirinkta: ")) == "tl":
    x = np.linspace(-2, 3, n).reshape(-1, 1); plot_name = 'Tolygiai pasiskirstę' # (-1, 1) 2d dimensija stulpelis nuo -2 iki 3 15 taškų į formule ideda nuo 0 iki 14
else:
    x = ciobysevo_mazgas(i, -2, 3, n).reshape(-1, 1); plot_name = ' Čiobyševo abscisė' # 2d

int_ciobysevo = ciobysevo_intervalas(x, -2, 3)
cb_daugianaris = ciobysevo_daugianaris(int_ciobysevo, i)
koffs = np.linalg.solve(cb_daugianaris, funkcija(x)) # išsprendžia lygčių sistema

x = np.linspace(-2, 3, 100).reshape(-1, 1) # padarom į 100 taškų nuo -2 iki 3

#spausdinti_ciobysevo(i, koffs)

cb_i_intervalas = ciobysevo_intervalas(x, -2, 3)
cb_i_daugianaris = ciobysevo_daugianaris(cb_i_intervalas, i)
int = np.dot(cb_i_daugianaris, koffs) # # dauginamos matricos

plt.plot(x, int, label='Interpoliuota')
plt.plot(x, funkcija(x), label='Esami')
plt.plot(x, funkcija(x)-int, label='Netektis')
plt.legend()
plt.title(plot_name)
plt.show()