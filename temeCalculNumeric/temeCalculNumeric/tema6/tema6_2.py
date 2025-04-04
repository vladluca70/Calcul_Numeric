import numpy as np
from sympy import pi, cos, sin, Eq, solve, symbols
import tkinter as tk
import matplotlib.pyplot as plt

root = tk.Tk()
frame = tk.Frame(root, bd=2, relief="solid", padx=70, pady=100)
frame.pack(padx=20, pady=20)

#begin initializare
nr_puncte = 5
valori_x = [0, pi/2, pi, 3*pi/2, 2*pi]
valori_y = [1, 0, -1, 0, 1]

T = []
m = (nr_puncte - 1) // 2

for i in range(nr_puncte):
    linie = [1]
    for j in range(1, m + 1):
        linie.append(cos(j * valori_x[i]))
        linie.append(sin(j * valori_x[i]))
    T.append(linie)

Y = valori_y

print("Matricea T:")
print(np.array(T))
print("Vectorul Y:")
print(Y)

def solve_linear_system(coefficients, constants):
    n = len(coefficients)
    variables = symbols(f'x1:{n + 1}')

    equations = [Eq(sum(coefficients[i][j] * variables[j] for j in range(n)), constants[i]) for i in range(n)]

    for x in equations:
        print(x)
    solution = solve(equations, variables)

    if len(solution) != len(constants):
        missing_vars = set(variables) - set(solution.keys())

        for var in missing_vars:
            solution[var] = 0  #

    return solution


def construire_polinom(solutii_sistem):
    n = len(solutii_sistem)
    polinom = str(solutii_sistem[0])
    m = (n - 1) // 2
    for k in range(1, m + 1):
        a_k = solutii_sistem[2 * k - 1]
        b_k = solutii_sistem[2 * k]
        polinom += f" + {a_k}*cos({k}*x) + {b_k}*sin({k}*x)"
    print("Polinomul:")
    print(polinom)


solution = solve_linear_system(T, Y)
solutii_sistem=[]
for x,y in solution.items():
    solutii_sistem.append(y)
construire_polinom(solutii_sistem)

label = tk.Label(frame, text=f"Raspuns {solutii_sistem}")
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
afiseaza_grafic(solutii_sistem)
