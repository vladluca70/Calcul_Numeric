import math
import numpy as np
import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()
frame = tk.Frame(root, bd=2, relief="solid", padx=70, pady=100)
frame.pack(padx=20, pady=20)


def P_x_horner(valoare, coeficienti):
    grad=len(coeficienti)
    Px=coeficienti[0]
    for pozitie in range(1,grad):
        Px=Px*valoare+coeficienti[pozitie]
    return Px


def afisare_polinom(coeficienti):
    termenii = []
    n = len(coeficienti) - 1
    for i, coef in enumerate(coeficienti):
        putere = n - i
        if coef == 0:
            continue
        semn = " + " if coef > 0 and termenii else ""
        coef_str = "" if abs(coef) == 1 and putere != 0 else str(abs(coef))
        if putere > 1:
            termen = f"{coef_str}x^{putere}"
        elif putere == 1:
            termen = f"{coef_str}x"
        else:
            termen = f"{coef_str}"
        termenii.append(f"{semn}{'-' if coef < 0 else ''}{termen}")
    return "".join(termenii) or "0"


#begin_initializare
valori_x=[]
valori_y=[]
numar_de_puncte=int(input("numarul de puncte"))
gradul_polinomului=int(input("grad polinom"))

for i in range(numar_de_puncte):
    x=int(input())
    valori_x.append(x)

for i in range(numar_de_puncte):
    y=int(input())
    valori_y.append(y)
#end_initializare

#begin_calculare_sume
nr_de_sume_S=gradul_polinomului*2+1
nr_de_sume_T=gradul_polinomului+1
sume_S=[]
sume_T=[]
sume_S.append(len(valori_x))

for i in range(1,nr_de_sume_S):
    suma=0
    for j in valori_x:
        suma=suma+math.pow(j,i)
    sume_S.append(int(suma))

for i in range(nr_de_sume_T):
    suma=0
    for j in range(len(valori_y)):
        suma=suma+math.pow(valori_x[j],i)*valori_y[j]
    sume_T.append(int(suma))
#end_calculare_sume pentru sistem

#determinare solutie
nl=gradul_polinomului+1
sublists = [sume_S[i:i + nl] for i in range(len(sume_S) - nl + 1)]
A=np.array(sublists)
B=np.array(sume_T)
sol=np.linalg.solve(A,B)
sol[np.abs(sol) < 1e-10] = 0
sol = np.round(sol, 2).tolist()
#end determinare solutie
print(sol)
print(afisare_polinom(sol))



label = tk.Label(frame, text=f"Raspuns {sol}")
label.pack()
root.mainloop()

def afiseaza_grafic(coeficienti):
    def f(x):
        return sum(c * x**i for i, c in enumerate(coeficienti))

    x = np.linspace(-10, 10, 400)

    y = f(x)

    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Grafic')
    plt.grid(True)
    plt.show()
afiseaza_grafic(sol)
