import math
import random
import tkinter as tk

root = tk.Tk()
frame = tk.Frame(root, bd=2, relief="solid", padx=70, pady=100)
frame.pack(padx=20, pady=20)

def afisare_polinom(grad, coeficienti,type):
    polinom = ""

    for i in range(grad + 1):
        coeficient = coeficienti[i]
        if coeficient != 0:
            if polinom and coeficient > 0:
                polinom += "+"

            if coeficient == -1 and grad - i > 0:
                polinom += "-"
            elif coeficient != 1 or grad - i == 0:
                polinom += str(coeficient)

            if grad - i > 0:
                polinom += "x"
                if grad - i > 1:
                    polinom += "^" + str(grad - i)
    if type==1:
        print(polinom)
    else:
        return polinom

def derivate(coeficienti):
    grad = len(coeficienti) - 1
    prima_derivata = [coeficienti[i] * (grad - i) for i in range(grad)]
    grad_prim = len(prima_derivata) - 1
    a_doua_derivata = [prima_derivata[i] * (grad_prim - i) for i in range(grad_prim)]
    return prima_derivata, a_doua_derivata

def P_x(valoare,coeficienti):
    grad=len(coeficienti)-1
    Px=0
    for coeficient in coeficienti:
        Px=Px+coeficient*(math.pow(valoare,grad))
        grad=grad-1
    return Px

def P_x_horner(valoare, coeficienti):
    grad=len(coeficienti)
    Px=coeficienti[0]
    for pozitie in range(1,grad):
        Px=Px*valoare+coeficienti[pozitie]
    return Px


grad_polinom = int(input("Gradul polinomului: "))

coeficienti_polinom = []
coeficient_maxim = -float('inf')

for i in range(grad_polinom + 1):
    coeficient = float(input(f"Coeficient pentru x^{grad_polinom - i}: "))
    coeficienti_polinom.append(coeficient)
    if coeficient > coeficient_maxim:
        coeficient_maxim = coeficient

R = (coeficienti_polinom[0] + coeficient_maxim) / coeficienti_polinom[0]

first, second = derivate(coeficienti_polinom)
afisare_polinom(grad_polinom, coeficienti_polinom,1)
afisare_polinom(grad_polinom - 1, first,1)
afisare_polinom(grad_polinom - 2, second,1)

solutii=[]
epsilon=10e-15
k=1
kmax=2000
for selectii_pentru_x in range(100):
    x=random.uniform(-R,R)
    A=2*(math.pow(P_x(x,first),2)-(P_x(x,coeficienti_polinom)*P_x(x,second)))
    Delta=2*(P_x(x,coeficienti_polinom)*P_x(x,first))/A

    while abs(Delta)>=epsilon and k<kmax and abs(Delta)<=math.pow(10,8):
        A = 2 * (math.pow(P_x_horner(x, first), 2) - (P_x_horner(x, coeficienti_polinom) * P_x_horner(x, second)))
        if abs(A)<epsilon:
            A=epsilon*10
        Delta = 2 * (P_x_horner(x, coeficienti_polinom) * P_x_horner(x, first)) / A
        x=x-Delta
        k=k+1
    if abs(Delta)<epsilon:
        if x not in solutii:
            solutii.append(x)
print("solutii",solutii)

forFile=afisare_polinom(grad_polinom,coeficienti_polinom,2)

with open("rez.txt", "a") as file:
    file.write("Ecuatia: ")
    file.write(forFile)
    file.write("\nare solutiile: \n")
    file.write("\n".join(map(str, solutii)))
    file.write("\n")

#creare grafic functie

label = tk.Label(frame, text=f"Raspuns {solutii}")
label.pack()
root.mainloop()