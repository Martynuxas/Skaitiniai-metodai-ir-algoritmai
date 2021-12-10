import numpy as np

def lygciuSistema(x): # grazina lygciu sistema
    return np.array([
        2 * x[0] + 2 * x[1] - 3 * x[2] - 32,
        x[0] * x[1] - 2 * x[3] - 12,
        -4 * x[1] ** 2 + x[1] * x[2] + 3 * x[2] ** 3 + 676,
        5 * x[0] - 6 * x[1] + x[2] + 3 * x[3] - 4
    ])

def tikslumas(x): # grazina tiksluma
    return (lygciuSistema(x) ** 2).sum()

def gradientas(x): # gradiento funkcija
    # 1e-14 norma, tikslumas/normos
    dx0 = (tikslumas([
        x[0] + 1e-14, x[1], x[2], x[3]
    ]) - tikslumas(x)) / 1e-14
    dx1 = (tikslumas(
        [x[0], x[1] + 1e-14, x[2], x[3]
         ]) - tikslumas(x)) / 1e-14
    dx2 = (tikslumas(
        [x[0], x[1], x[2] + 1e-14, x[3]
         ]) - tikslumas(x)) / 1e-14
    dx3 = (tikslumas(
        [x[0], x[1], x[2], x[3] + 1e-14]
    ) - tikslumas(x)) / 1e-14
    g = np.array([dx0, dx1, dx2, dx3])
    return g

# turi x'sai gautis = 5 2 -6 -1
def greiciausio_nusileidimo(): # metodas
    alpha = 1.1 # žingsnio dydis
    x = np.array([
        4.9, 1.9, -5.9, -0.9
    ])

    x_1 = 0
    g = gradientas(x)
    for i in range(1000000):
        buv_tikslumas = tikslumas(x)
        if buv_tikslumas < 1e-17: # jei tikslumas pasiektas - stabdom
            break

        x = x - alpha * g # nauja kryptis

        if buv_tikslumas < tikslumas(x):
            x = x + alpha * g # atgalinis žingsnis
            alpha *= 0.4 # sumažinam alpha
            g = gradientas(x) # perskaičiuoja gradienta
        else:
            x_1 += 1
            if x_1 > 10: # kas iteraciju žingsnių didinam zingsniu
                x_1 = 0
                alpha *= 10000


        print(f'Tikslumas: {tikslumas(x)} iteracijos: {i}')
    print()
    print(f'x = {x}')

greiciausio_nusileidimo()
