import math
import random
import numpy as np
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, bd=2, relief="solid", padx=70, pady=100)
frame.pack(padx=20, pady=20)

n = int(input("n: "))
epsilon = -200


A=[]
for i in range(n):
    linie=[]
    for j in range(n):
        x=random.uniform(0,10)
        linie.append(x)
    A.append(linie)

b = []
dU = []
for i in range(n):
    x = int(random.uniform(-100, 100))
    dU.append(x)
    x = int(random.uniform(-100, 100))
    b.append(x)

for i in range(n):
    if dU[i]<epsilon:
        print("eroare epsilon")
        exit()

L=[]
U=[]
for i in range(n):
    line=[]
    for j in range(n):
        line.append(0)
    L.append(line.copy())
    U.append(line.copy())

for i in range(n):
    L[i][i] = 1
for i in range(n):
    U[i][i] = dU[i]

for i in range(n):
    for j in range(i, n):
        suma1 = sum(L[i][k] * U[k][j] for k in range(i))
        U[i][j] = (A[i][j] - suma1)

    for j in range(i + 1, n):
        suma2 = sum(L[j][k] * U[k][i] for k in range(i))
        L[j][i] = (A[j][i] - suma2) / U[i][i]

print("\nL:")
for row in L:
    print(row)

print("\nU:")
for row in U:
    print(row)

# Calcul determinant: det(A) = det(L) * det(U)
detL = 1
detU = 1
for i in range(n):
    detU *= U[i][i]

detA = detU * detL
print("\nDeterminantul lui A este:", detA)

# Ax=b <==> LUx = b -> Ly = b și Ux = y
y = [0] * n
for i in range(n):
    suma = sum(L[i][j] * y[j] for j in range(i))
    y[i] = (b[i] - suma)

x = [0] * n
for i in range(n - 1, -1, -1):
    suma = sum(U[i][j] * x[j] for j in range(i + 1, n))
    x[i] = (y[i] - suma) / U[i][i]

print("\nVectorul y:", y)
print("Vectorul x:", x)

#norma euclidiana
#||t|| unde t=Ax-b si ||t|| se face radical din suma patratelor
rez_Ax=[]
for i in range(n):
    suma=0
    for j in range(n):
        suma=suma+A[i][j]*x[j]
    rez_Ax.append(suma)
for i in range(n):
    rez_Ax[i]=rez_Ax[i]-b[i]
norma=0
for i in range(n):
    norma=norma+rez_Ax[i]*rez_Ax[i]
norma=math.sqrt(norma)
print("norma=",norma)

def inversa_matrice(A):
    A = np.array(A)
    if A.shape[0] != A.shape[1]:
        return "matricea nu are inversa pt ca nu e patratica"

    try:
        A_inv = np.linalg.inv(A)
        return A_inv
    except np.linalg.LinAlgError:
        return "matricea nu e inversabila deoarece detA=0"

inversa_matrice_A=inversa_matrice(A)
print("inversa_matrice_A:", inversa_matrice_A)

solution_with_function=np.linalg.solve(A,b)
print("solutia x folosind functii din numpy este x=", solution_with_function)

x_lib=np.linalg.solve(inversa_matrice_A,b)
s = np.linalg.norm(solution_with_function - x_lib)
print("a doua norma")
print(math.sqrt(s))

#a treia norma
result=np.dot(inversa_matrice_A,b)
result=inversa_matrice_A-b
for x in result:
    print(x)
suma_patrate=np.sum(result**2)
print("a treia norma", np.sqrt(suma_patrate))

label = tk.Label(frame, text=f"Matricea L este {L}\n Matricea U este {U}\n Determinant A={detA}\n"
                             f"Inversa matricei este {inversa_matrice_A}\n Prima norma={norma}\n"
                             f"A doua norma este {math.sqrt(s)}\n A treia nortma este {np.sqrt(suma_patrate)}")
label.pack()

root.mainloop()
