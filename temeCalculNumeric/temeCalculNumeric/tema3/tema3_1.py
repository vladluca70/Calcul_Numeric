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

A=[]
diagonala_matrice=[0]*n
for _ in range(n):
    A.append([0]*n)

for linie in elemente:
    A[linie[1]][linie[2]]=linie[0]
    if linie[1]==linie[2]:
        diagonala_matrice[linie[1]]=linie[0]

ok=1
for i in range(n):
    if diagonala_matrice[i]==0:
        ok=0
if ok==0:
    print("element diagonala matrice egal cu 0")
    exit()
else:
    print("elemente diagonala matrice nenule")


x=[0]*n
#for k in range(n):
for i in range(n):
    suma=0
    for j in range(n):
        if i!=j and A[i][j]!=0:
            suma =suma+ A[i][j]*x[j]
    x[i]=(b[i]-suma)/diagonala_matrice[i]

print(x)

label = tk.Label(frame, text=f"aproximare vector x {x}")
label.pack()

root.mainloop()
