import numpy as np
import matplotlib.pyplot as plt


def taskai(n):
    taskai = []
    kiekis = n
    for _ in range(kiekis):
        x = np.random.randint(-10, 10)
        y = np.random.randint(-10, 10)
        taskai.append((x, y))
    return np.array(taskai)

def papildomi_taskai(n):
    ptaskai = []
    kiekis = n
    for i in range(kiekis):
        rx = np.random.randint(-10, 10)
        ry = np.random.randint(-10, 10)
        ptaskai.append((rx, ry))
    return np.array(ptaskai)

taskai = taskai(6)
x = taskai[:, 0]
y = taskai[:, 1]
ptaskai = papildomi_taskai(6)
rx = ptaskai[:, 0]
ry = ptaskai[:, 1]

def skaiciuoti_vid_ilgi(rx, ry, x ,y):
    suma = 0
    n = len(rx+x) # viso tasku suma
    for i in range(n):
        for j in range(i + 1, n):
            suma += np.sqrt((rx[j]+x[j] - rx[i]+x[i]) ** 2 + (ry[j]+y[j] - ry[i]+y[i]) ** 2) # atstumo tarp tasku formule
    kampu_kiekis = n * (n - 1) / 2 # kampu kiekis
    vidutinis_ilgis = suma / kampu_kiekis # vidutinis atstumas
    return vidutinis_ilgis, suma


def tikslumas(rx, ry, vidutinis, s, x, y):
    suma = 0
    n = len(rx)
    _, ilgis = skaiciuoti_vid_ilgi(rx, ry, x, y)
    for i in range(n):
        for j in range(i + 1, n):
            atst = ((rx[j] - rx[i]) ** 2 + (ry[j] - ry[i]) ** 2) ** 0.5
            suma += (atst - vidutinis) ** 2
    return suma + abs(ilgis - s)


def gradientas(rx, ry, vidutinis, s, x ,y):
    g = []
    t = 1e-12
    f0 = tikslumas(rx, ry, vidutinis, s, x ,y)
    for i in range(len(rx)):
        xx = np.array(rx, copy=True)
        yy = np.array(ry, copy=True)
        xx[i] += t
        yy[i] += t
        dx = (tikslumas(xx, ry, vidutinis, s, x, y) - f0) / t
        dy = (tikslumas(rx, yy, vidutinis, s, x, y) - f0) / t
        g.append((dx, dy))
    g = np.array(g).T
    return g / np.linalg.norm(g)


def nusileidimo_gradientas(rx, ry, s, x, y):
    iteracijos = 0
    eTikslumas = 1e10
    log = []
    vidutinis_ilgis, _ = skaiciuoti_vid_ilgi(rx, ry, x, y)
    print(f'{vidutinis_ilgis}')

    alpha = 0.2 # žingsnio dydis
    while eTikslumas > 1e-6:
        iteracijos += 1
        buv_tikslumas = tikslumas(rx, ry, vidutinis_ilgis, s, x, y) # išsisaugom tikslumą

        grad = gradientas(rx, ry, vidutinis_ilgis, s, x, y) # apsiskaičiuoja gradienta

        log.append((iteracijos, buv_tikslumas))
        rx = rx - alpha * grad[0] # nauja kryptis
        ry = ry - alpha * grad[1] # nauja kryptis

        esam_tikslumas = tikslumas(rx, ry, vidutinis_ilgis, s, x , y) # apskaičiuoja dabartinį tikslumą po krypties keitimo
        eTikslumas = np.abs(esam_tikslumas - buv_tikslumas) / (np.abs(buv_tikslumas) + np.abs(esam_tikslumas))
        if eTikslumas < 1e-6:
            atvaizduoti_taskus(rx, ry, x, y)
            rodyti_tiksluma(np.array(log))
            break # stabdom pasiekus tinkama tiksluma
        if esam_tikslumas > buv_tikslumas:
            rx = rx + alpha * grad[0] # atgalinis žingsnis
            ry = ry + alpha * grad[1] # atgalinis žingsnis
            alpha /= 2
    print(f'{iteracijos}')


def atvaizduoti_taskus(rx, ry, x, y):
    plt.axis((-15, 15, -15, 15))
    rn = len(rx)
    n = len(x)
    #  padedami taskai
    for i in range(rn):
        plt.plot(rx[i], ry[i], 'ro')
        plt.text(rx[i], ry[i], f'({rx[i]:.2f}, {ry[i]:.2f})', size='large')
    for i in range(n):
        plt.plot(x[i], y[i], 'ro')
        plt.text(x[i], y[i], f'({x[i]:.2f}, {y[i]:.2f})', size='small')
    #  linijos
    for i in range(rn):
        for j in range(i+1, rn):
            plt.plot((rx[i], rx[j]), (ry[i], ry[j]), 'g-', linewidth=3)
    for i in range(n):
        for j in range(i+1, n):
            plt.plot((x[i], x[j]), (y[i], y[j]), 'g-', linewidth=0.5)
    plt.show()


def rodyti_tiksluma(log):
    plt.plot(log[:, 0], log[:, 1])
    plt.xlabel('iteracijos')
    plt.ylabel('tikslumas')
    plt.show()


atvaizduoti_taskus(rx, ry, x, y)
S = 1
nusileidimo_gradientas(rx, ry, S, x, y)