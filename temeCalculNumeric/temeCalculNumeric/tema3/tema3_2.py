import math
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, bd=2, relief="solid", padx=70, pady=100)
frame.pack(padx=20, pady=20)



with open("b_1.txt", "r", encoding="utf-8") as f:
    b = [float(linie.strip()) for linie in f if linie.strip()]
n=int(b[0])
b.pop(0)

with open("a_1.txt", "r", encoding="utf-8") as f:
    linii = [linie.strip() for linie in f if linie.strip()]
elemente = []
for linie in linii[1:]:
    valori = [val.strip() for val in linie.split(",")]
    valoare = float(valori[0])
    linie_idx = int(valori[1])
    coloana_idx = int(valori[2])
    elemente.append((valoare, linie_idx, coloana_idx))

epsilon=math.pow(10,-80)

matrice_A = [[] for _ in range(n)]
diagonala_matrice_A=[0]*n

for linie in elemente:
    if linie[1]==linie[2]:
        diagonala_matrice_A[linie[1]]=linie[0]
    if linie[1]!=linie[2]:
        matrice_A[linie[1]].append((linie[0],linie[2]))


x=[0]*n
for k in range(100):#10^&*4
    for i in range(n):
        suma=0
        linie_matrice=matrice_A[i]
        for elem in linie_matrice:
            suma=suma+elem[0]*x[elem[1]]
        x[i]=(b[i]-suma)/diagonala_matrice_A[i]


print(x)

#norma
rez_inmultire_A_si_x=[0]*n
contor=0
for linie in matrice_A:
    suma=0
    for i in linie:
        suma=suma+i[0]*x[i[1]]
    suma=suma+diagonala_matrice_A[contor]*x[contor]
    rez_inmultire_A_si_x[contor]=suma
    contor+=1
for i in range(len(rez_inmultire_A_si_x)):
    rez_inmultire_A_si_x[i]-=b[i]

sumaNorma=0
for i in rez_inmultire_A_si_x:
    sumaNorma=sumaNorma+i*i
print(math.sqrt((sumaNorma)))

label = tk.Label(frame, text=f"Norma {math.sqrt(sumaNorma)}")
label.pack()

root.mainloop()
