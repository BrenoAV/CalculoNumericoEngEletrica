import numpy as np

"""
Método iterativo: Gauss-Jacobi

É necessário informar os vetores A e b, o distanciamento E para o critério de parada e o máximo
de iterações

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""
# CONSTANTES
A = np.array([[3, 1, 0, -1], [1, 3, 1, 1], [0, 1, 3, -1], [-1, 1, -1, 4]], dtype= np.float) # vetor n x n
b = np.array([10, 15, 10, 0]) # vetor coluna
E = 0.0001 # Critério de parada
max_i = 30 # máximo de iterações


tam = len(A)
xo = np.array([0]*tam, dtype= np.float) # X OLD (valores antigos de X)
xn = np.array([0]*tam, dtype= np.float) # X NEW (valores atuais de X)
xabs = np.array([0]*tam, dtype= np.float) # valores absolutos de x usados para comparar o erro posteriormente
d = np.array([0]*tam, dtype= np.float) # erro
i = 0 # número de iterações

# Valor inicial do chute
for n in range(0, tam):
    xo[n] = b[n]/A[n][n]

while True:
    i += 1 

    # Calculando os x
    for n in range(0, tam):
        soma = b[n]/A[n][n] 
        for j in range(0, tam):
            if n != j:
                soma -= ( 1/A[n][n] )*(A[n][j]*xo[j])
        xn[n] = soma

    # Verificação da convergência
    for n in range(0, tam):
        d[n] = ( abs(xn[n]) - abs(xo[n]) )
        xabs[n] = abs(xn[n])

    if abs(max(d)/max(xabs)) < E or i == max_i:
        break

    xo = xn.copy() # antigo igual ao novo

# Exibição dos valores
cont = 1
print(f'O resultado convergiu com {i} iterações:')
for i in xn:
    print(f'x{cont} = {i:.4f}')
    cont += 1
