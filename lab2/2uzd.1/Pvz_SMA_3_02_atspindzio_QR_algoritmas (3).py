
import numpy as np
from PyFunkcijos import *

# textbox isvedimui
T=ScrollTextBox(100,20) # sukurti teksto isvedimo langa
T.insert(END,"# ********************* Gauso algoritmas  ****************************")


# -------------------iseities duomnenys:
A=np.matrix([[1 , 1,  1,  1],
             [1, -1, -1,  1],
             [2,  1, -1,  2],
             [3,  1,  2, -1]]).astype(np.float)        # koeficientu matrica
b=(np.matrix([2,0,9,7])).transpose().astype(np.float)   #laisvuju nariu vektorius-stulpelis
n=(np.shape(A))[0]   # lygciu skaicius nustatomas pagal ivesta matrica A
nb=(np.shape(b))[1]  # laisvuju nariu vektoriu skaicius nustatomas pagal ivesta matrica b

A1=np.hstack((A,b))  #isplestoji matrica

SpausdintiMatrica(A,T,'A');SpausdintiMatrica(b,T,'b');SpausdintiMatrica(n,T,'n');SpausdintiMatrica(nb,T,'nb');SpausdintiMatrica(A1,T,'A1');

# tiesioginis etapas(atspindziai):
for i in range (0,n-1):
    z=A1[i:n,i]
    zp=np.zeros(np.shape(z)); zp[0]=np.linalg.norm(z)
    SpausdintiMatrica(zp,T,'zp')
    omega=z-zp; omega=omega/np.linalg.norm(omega)
    Q=np.identity(n-i)-2*omega*omega.transpose()
    SpausdintiMatrica(Q,T,'Q')
    A1[i:n,:]=Q.dot(A1[i:n,:])
    SpausdintiMatrica(A1,T,'A1')
    # atgalinis etapas:
x=np.zeros(shape=(n,nb))
for i in range (n-1,-1,-1):    # range pradeda n-1 ir baigia 0 (trecias parametras yra zingsnis)
    x[i,:]=(A1[i,n:n+nb]-A1[i,i+1:n]*x[i+1:n,:])/A1[i,i]
    SpausdintiMatrica(x,T,"x")

T.insert(END,"sprendinys:");SpausdintiMatrica(x,T,'x');
T.insert(END,"------------ sprendinio patikrinimas ----------------");
liekana=A.dot(x)-b;SpausdintiMatrica(liekana,T,'liekana');
SpausdintiMatrica(np.linalg.norm(liekana)/ np.linalg.norm(x),T,"bendra santykine paklaida:")

str1=input("Baigti darba? Press Enter \n")
