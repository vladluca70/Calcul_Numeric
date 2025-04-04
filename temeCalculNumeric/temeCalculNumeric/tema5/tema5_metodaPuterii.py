import numpy as np
import sympy as sp

def transpusa_matrice(matrice):
    A=np.array(matrice)
    transpusa=np.transpose(A)
    rez=transpusa.tolist()
    return rez

def ATA(matrice):
    A=np.array(matrice)
    transpusa=transpusa_matrice(A)
    transpusa=np.array(transpusa)
    rez=np.matmul(transpusa,A)
    rez=rez.tolist()
    return rez

def AAT(matrice):
    A=np.array(matrice)
    transpusa=transpusa_matrice(A)
    transpusa=np.array(transpusa)
    rez=np.matmul(A,transpusa)
    rez=rez.tolist()
    return rez

def determinare_solutii_delta(matrice):
    delta = sp.symbols('delta')

    A = sp.Matrix(matrice)

    I = sp.eye(A.shape[0])

    determinant = (A - delta * I).det()

    solutii = sp.solve(determinant, delta)

    solutii_numarice = []
    for sol in solutii:
        real_part = sol.as_real_imag()[0].evalf()
        imag_part = sol.as_real_imag()[1].evalf()

        if abs(imag_part) < 1e-10:
            solutii_numarice.append(real_part)
        else:
            solutii_numarice.append(sol.evalf())

    print("Soluțiile numerice ale ecuației caracteristice sunt:", solutii_numarice)

A=[
    [3,4],
    [5,6]
]

determinare_solutii_delta(ATA(A))