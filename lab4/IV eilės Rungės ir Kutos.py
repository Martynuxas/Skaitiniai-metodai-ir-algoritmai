import matplotlib.pyplot as plt
import numpy as np
import math
from scipy.integrate import odeint


def RungėsKutos():

    t = t0
    TA = TA1
    T = T1

    print("Pradine kuno temperatura:", T)
    print("Pradine aplinkos temperatura:", TA)

    temperatura = []
    laikas = []
    aplinkosTemperatura = []

    while t != tmax:
        if t == ts and TA != TA2: # kaip aplinkos temperatūra kinta
            print("Pradeda kisti aplinkos temperatura")
            while TA != TA2: # kol nepasiekė max temp
                TA = TA1 + ((TA2-TA1)/2)*(1-np.cos(((math.pi)/20)*(t-ts))) # TA(t) dėsnis
                if TA == TA2:
                    print("pasiekta aplinkos temperatura!", T, TA, t)
                    TA = TA2
                k = -0.01 - 0.16*((T-273)/100) - 0.04*((T-273)/100)**2 # k(T) dėsnis
                #pirmas etapas
                dt1 = k * (T - TA)
                T11 = T + z/2 * dt1
                #antras etapas(atgalinis)
                dt2 = k * (T11 - TA)
                T2 = T + z/2 * dt2
                #trecias etapas(vidurinis taškas)
                dt3 = k * (T2 - TA)
                T3 = T + z * dt3
                #ketvirtas etapas(simpsono)
                dt4 = k * (T3 - TA)
                T = T + z/6 * (dt1 + 2 * dt2 + 2 * dt3 + dt4)
                print("esamos temperaturos:",T, TA)
                t += z
                if T == TA:
                    print("Temperaturos susivienodino1:", T, TA)
                temperatura.append(T)
                laikas.append(t)
                aplinkosTemperatura.append(TA)
        else: # kol nekinta aplinkos temperatŪra
            k = -0.01 - 0.16*((T-273)/100) - 0.04*((T-273)/100)**2 # k(T) dėsnis
            #pirmas etapas
            dt1 = k * (T - TA)
            T11 = T + z/2 * dt1
            #antras etapas(atgalinis)
            dt2 = k * (T11 - TA)
            T2 = T + z/2 * dt2
            #trecias etapas(vidurinis taškas)
            dt3 = k * (T2 - TA)
            T3 = T + z * dt3
            #ketvirtas etapas(simpsono)
            dt4 = k * (T3 - TA)
            T = T + z/6 * (dt1 + 2 * dt2 + 2 * dt3 + dt4)
            print("esamos temperaturos:",T, TA)
            t += z
            if T == TA:
                print("Temperaturos susivienodino3:", T, TA)
            temperatura.append(T)
            laikas.append(t)
            aplinkosTemperatura.append(TA)

    def model(T, t):

        global reachedModel
        TA = TA1 if not reachedModel else TA2
        if t > ts:
            if not reachedModel:
                TA = TA1 + ((TA2 - TA1) / 2) * (1 - np.cos(((math.pi) / 20) * (t - ts)))
                if TA>TA2:
                    TA=TA2
                    reachedModel = True
        k = -0.01 - 0.16 * ((T - 273) / 100) - 0.04 * ((T - 273) / 100) ** 2
        dt = k * (T - TA)
        return dt

    x = np.arange(0, tmax, 1)
    plt.plot(laikas, temperatura, label = "kūno temperatūra")
    plt.plot(laikas, aplinkosTemperatura, label = "aplinkos temperatura")
    plt.plot(x, odeint(model, T, x), 'g', label="odeint")
    plt.title("Runges ir Kutos")
    plt.xlabel('Laikas')
    plt.ylabel('Temperatura')
    plt.grid()
    plt.legend()
    plt.show()
            
            

        




if __name__ == '__main__':
    reachedModel = False
    t0 = 0 #pradinis laikas
    z = 0.5 #zingsnis
    #z = 1  # zingsnis
    #z = 2  # zingsnis
    #z = 5  # zingsnis
    T1 = 400 #pradine kuno temp
    #T1 = 270 #pradine kuno temp antras variantas
    TA1 = 320 #aplinkos temp 1
    TA2 = 460 #aplinkos temp 2
    tmax = 80 #galutinis laikas
    ts = 30 #kada pradeda kisti aplinkos temp


    RungėsKutos()

