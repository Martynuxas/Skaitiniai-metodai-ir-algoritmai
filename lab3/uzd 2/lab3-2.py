import numpy as np
from numpy import sin, cos, arccos, pi
import matplotlib.pyplot as plt
import pandas as pd

plt.style.use('ggplot')

# daugianario formulė
def ciobysevo_daugianaris(x, i): return cos(arccos(x) * i)

# duota cb interpoliavimo intervalo formulė
# pr - pradžią, b - pabaiga, n - mazgų skaičius FORMULĖ
def ciobysevo_intervalas(n, pr, pb): return (2 * n) / (pb - pr) - (pb + pr) / (pb - pr)


def interpoliuoti_ciobyseva(x, y):
    int_ciobysevo = ciobysevo_intervalas(x, 0, 11)

    cb_daugianaris = ciobysevo_daugianaris(int_ciobysevo, x.T)
    koffs = np.linalg.solve(cb_daugianaris, y)

    x_n = np.linspace(0, 11, 100).reshape(-1, 1) # nuo 0 iki 11 į 100 taškų 2d stulpelis
    cb_i_int = ciobysevo_intervalas(x_n, 0, 11)

    cb_daugianaris = ciobysevo_daugianaris(cb_i_int, x.T) # x.T transponuoja, eilutes į stulepius ir atvr
    y_n = cb_daugianaris.dot(koffs) # dauginamos matricos

    plt.title('Austrijos temperatūra 2014')
    plt.plot(x, y, 'D',label='Esami')
    plt.plot(x_n, y_n, 'g-', label='Interpoliuoti')
    plt.legend()
    plt.xticks(np.arange(12), np.arange(1, 13))
    plt.show()

n = 12  # 12 mėnesių
data = pd.read_csv('austria_temperatures_2014.csv')
x = data.index.to_numpy().reshape(-1, 1)  # index'ai į 2d dimensija stulpelis
y = data.iloc[:, 0].to_numpy().reshape(-1, 1)  # temperatūros į 2d dimensija stulpelis
del data

interpoliuoti_ciobyseva(x, y)