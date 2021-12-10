
import numpy as np
from PyFunkcijos import *


A=np.matrix([[1, 2, 1, 0],
            [2, 5, 0, 4],
            [14, -8, 4, 1],
            [4, 10, 0, 8]]).astype(np.float)        # koeficientu matrica
b=(np.matrix([-4, 3, 7, 2])).transpose().astype(np.float)   #laisvuju nariu vektorius-stulpelis
n=(np.shape(A))[0]   # lygciu skaicius nustatomas pagal ivesta matrica A
nb=(np.shape(b))[1]  # laisvuju nariu vektoriu skaicius nustatomas pagal ivesta matrica b

A1=np.hstack((A,b))  #isplestoji matrica


print(f'{A}\n') # A matrica
print(f'{b} {n}') # laisvuju nariu vektorius-stulpelis ir lygciu skaicius
print(f'{nb}') # laisvuju nariu vektoriu skaicius
print(f'{A1}') # isplestoji


# etapas(atspindziai):
Q=np.identity(n)
for i in range (0,n-1):
    z=A1[i:n,i]
    zp=np.zeros(np.shape(z)); zp[0]=np.linalg.norm(z)
    print(f'{zp}')
    omega=z-zp; omega=omega/np.linalg.norm(omega)
    Qi=np.identity(n-i)-2*omega*omega.transpose()
    print(f'{Q}')
    A1[i:n,:]=Qi.dot(A1[i:n,:])
    print(f'{A1}')

    # atgalinis etapas:
x=np.zeros(shape=(n,nb))
for i in range (n-1,-1,-1):    # range pradeda n-1 ir baigia 0 (trecias parametras yra zingsnis)
    x[i,:]=(A1[i,n:n+nb]-A1[i,i+1:n]*x[i+1:n,:])/A1[i,i]
    print(f'{x}')

print(f'sprendinys:')
print(f'{x}')
print(f'liekana:')
liekana=A.dot(x)-b;print(f'{liekana}')
print(f'bendra santykine paklaida:')
print(f'{np.linalg.norm(liekana)/ np.linalg.norm(x)}')

