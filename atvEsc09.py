import numpy as np

vetor1 = np.empty(10, dtype="int32")
vetor2 = np.empty(10, dtype="int32")
vetor3 = np.empty(20, dtype="int32")

for i in range(10):
    vetor1[i] = int(input("Digite o valor do primeiro vetor: "))

for i in range(10):
    vetor2[i] = int(input("Digite o valor do segundo vetor: "))

indiceVetor1 = 0
indiceVetor2 = 0

#
for i in range(20):
    if i % 2 == 0:
        vetor3[i] = vetor1[indiceVetor1]
        indiceVetor1 += 1
    else:
        vetor3[i] = vetor2[indiceVetor2]
        indiceVetor2 += 1

print(vetor3)
