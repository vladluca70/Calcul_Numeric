with open("a.txt", "r", encoding="utf-8") as f:
    linii = [linie.strip() for linie in f if linie.strip()]
elemente = []
for linie in linii[1:]:
    valori = [val.strip() for val in linie.split(",")]
    valoare = float(valori[0])
    linie_idx = int(valori[1])
    coloana_idx = int(valori[2])
    elemente.append((valoare, linie_idx, coloana_idx))
n=int(linii[0])
matrice_A = [[] for _ in range(n)]

for linie in elemente:
    matrice_A[linie[1]].append((linie[0],linie[2]))

############

with open("b.txt", "r", encoding="utf-8") as f:
    linii = [linie.strip() for linie in f if linie.strip()]
elemente = []
for linie in linii[1:]:
    valori = [val.strip() for val in linie.split(",")]
    valoare = float(valori[0])
    linie_idx = int(valori[1])
    coloana_idx = int(valori[2])
    elemente.append((valoare, linie_idx, coloana_idx))

matrice_B = [[] for _ in range(n)]
for linie in elemente:
    matrice_B[linie[1]].append((linie[0],linie[2]))


def suma_matrici_rara(A, B):
    matrice_rara = []
    for i in range(len(A)):
        linie_rara = []

        index_A, index_B = 0, 0
        while index_A < len(A[i]) or index_B < len(B[i]):
            if index_A < len(A[i]) and (index_B >= len(B[i]) or A[i][index_A][1] < B[i][index_B][1]):
                linie_rara.append(A[i][index_A])
                index_A += 1
            elif index_B < len(B[i]) and (index_A >= len(A[i]) or B[i][index_B][1] < A[i][index_A][1]):
                linie_rara.append(B[i][index_B])
                index_B += 1
            else:
                valoare_suma = A[i][index_A][0] + B[i][index_B][0]
                linie_rara.append((valoare_suma, A[i][index_A][1]))
                index_A += 1
                index_B += 1

        matrice_rara.append(linie_rara)

    return matrice_rara

print(suma_matrici_rara(matrice_A,matrice_B))