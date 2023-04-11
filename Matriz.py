import numpy as np

Vitor_matriz = np.array([[3, 4, 1], [3, 1, 2]])

soma = 0
for i in range(Vitor_matriz.shape[0]): 
    for j in range(Vitor_matriz.shape[1]): 
        soma += Vitor_matriz[i][j]

print("A soma de todos os elementos da matriz é:", soma)