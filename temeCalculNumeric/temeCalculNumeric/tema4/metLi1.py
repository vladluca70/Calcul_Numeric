import copy
import math
import tkinter as tk
import numpy as np
root = tk.Tk()
frame = tk.Frame(root, bd=2, relief="solid", padx=70, pady=100)
frame.pack(padx=20, pady=20)



def transpusa_matrice(matrice):
    n = len(matrice)
    transpusa = [[matrice[j][i] for j in range(n)] for i in range(n)]
    return transpusa

def A_1(matrice):
    n=len(matrice)
    maxx=-9999999999999
    for linie in matrice:
        suma=0
        for element in linie:
            suma=suma+element
        if suma>maxx:
            maxx=suma
    return maxx

def A_inf(matrice):
    n=len(matrice)
    maxx=-9999999999999
    for i in range(n):
        suma=0
        for j in range(n):
            suma=suma+matrice[j][i]
        if suma > maxx:
            maxx = suma
    return maxx

def matrice1_minus_matrice2(A,B):
    A=np.array(A)
    B=np.array(B)
    difference=A-B
    differenceList=difference.tolist()
    return differenceList

def norma_euclidiana(matrice):
    n=len(matrice)
    suma=0
    for linie in matrice:
        for element in linie:
            suma=suma+(element*element)
    suma=math.sqrt(suma)
    return suma

def metodaLi1(A,V0):
    A=np.array(A)
    V0=np.array(V0)

    n=len(V0)
    I=np.eye(n)*3 #matricea identitate

    #3I_n-A*V_k
    AV_k=np.matmul(A,V0)
    diferenta1=I-AV_k
    #end

    #AV_k*diferenta
    produs1=np.matmul(A,V0)
    produs2=np.matmul(produs1,diferenta1)
    #end

    #3I-AV_k*diferenta
    diferenta2=I-produs2
    #end

    #rez final
    rez=np.matmul(V0,diferenta2)
    #end

    rez=rez.tolist()
    return rez


A = [
    [4,7,6,8],
    [2, 6,6,2],
    [8,9,4,1],
    [4,6,2,3]
]

#determinare V0
n=len(A)
A1_Ainf=1/(A_1(A)*A_inf(A))
V0=transpusa_matrice(A)
for i in range(len(V0)):
    for j in range(len(V0[i])):
        V0[i][j] *= A1_Ainf
#end determinare V0


#begin Li1
epsilon=1e-15
V1=copy.deepcopy(V0)
k=0
kmax=1000
DeltaV=norma_euclidiana(matrice1_minus_matrice2(V1,V0))

while DeltaV>=epsilon and k<=kmax and DeltaV<=math.pow(10,10):
    V0=copy.deepcopy(V1)
    V1=metodaLi1(A,V0)
    DeltaV=norma_euclidiana(matrice1_minus_matrice2(V1,V0))
    k=k+1

if DeltaV<epsilon:
    print("V1 este aproximarea cautata a solutiei")
    mesaj="V1 este aproximarea cautata a solutiei"
else:
    print("divergenta")
    mesaj="divergenta"
print(V1)
#end Li1

def norma_finala(matrice1,matrice2):
    n=len(matrice1)
    matrice_1=np.array(matrice1)
    matrice_2=np.array(matrice2)
    I=np.eye(n)
    rez=np.matmul(matrice_1,matrice_2)
    rez=rez-I
    rez=rez.tolist()
    final=A_1(rez)
    return final
print(norma_finala(A,V1))



label = tk.Label(frame, text=f"Raspuns {mesaj}")
label.pack()

root.mainloop()
