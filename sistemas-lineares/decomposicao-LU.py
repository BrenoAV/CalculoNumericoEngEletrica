import numpy as np

"""
Método direto: Decomposição LU

É necessário informar os vetores A e b depois do pivoteamento.

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""

A = np.array([[3, 2, 4], [1, 1, 2], [4, 3, -2]], dtype= np.float) # vetor n x n
b = np.array([1, 2, 3]) # vetor coluna
tam = len(A)

U = A.copy()
L = np.identity(tam, dtype= np.float)

for i in range(0, tam):
    for k in range(i + 1, tam):
        Mik = U[k][i]/U[i][i] # multiplicador da linha
        L[k][i] = Mik # adicionar os valores dos multiplicadores em L
        U[k, :] = U[k, :] - Mik*U[i, :] # Lk <-- Lk - Mik*Pivô

# RESOLVER O SISTEMA DADO POR:
# Ax = b
# L*U*x = b, logo A = L*U
# -> L*y = b
# -> U*x = y

y = np.array([0]*tam, dtype= np.float)
y[0] = b[0]/L[0][0] # primeiro elemento, ou seja, o y0

for n in range(1, tam):
    y[n] = ( (b[n] - sum(L[n][:n+1]*y[:n+1]) ) / L[n][n] ) # L*y = b

x = np.array([0] * tam, dtype= np.float)
x[tam - 1] = y[tam - 1]/U[tam - 1][tam - 1] # primeiro elemento, ou seja, o Xn

for n in range(tam - 2, -1, -1):
    x[n] = ( y[n] - sum(U[n][n+1:]*x[n+1:]) ) / U[n][n]  # U*x = y

# EXIBE O RESULTADO NA TELA
i = 1
for variable in x:
    print(f'x{i} = {variable:.4f}')
    i += 1
