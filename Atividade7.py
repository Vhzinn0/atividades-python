import numpy as np

vitormatriz = np.array([[3, 4, 1], [3, 1, 2]])

soma = 0
for i in range(vitormatriz.shape[0]): 
    for j in range(vitormatriz.shape[1]): 
        soma += vitormatriz[i][j]

print("A soma de todos os elementos da matriz é:", soma)