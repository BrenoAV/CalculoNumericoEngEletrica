import numpy as np

"""
Método direto: Eliminação de Gauss

É necessário informar a MATRIZ AUMENTADA A|b onde A é uma matriz nxn e b uma matriz
coluna nx1. Logo, a matriz Ab é uma matriz n x (n+1).

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""
# Informe a matriz AUMENTANDA
Ab = np.array([[3, 2, 4, 1], [1, 1, 2, 2], [4, 3, -2, 3]], dtype=np.float)
tam = len(Ab)

# FASE DE ELIMINAÇÃO

for i in range(0, tam):
    for k in range(i + 1, tam):
        Mik = Ab[k][i]/Ab[i][i] # multiplicador da linha
        Ab[k, :] = Ab[k, :] - Mik*Ab[i, :] # Lk <-- Lk - Mik*Pivô

# FASE DE SUBSTITUIÇÃO 

A = []
b = []
for n in range(0, tam):
    A.append(Ab[n][0:tam]) 
    b.append(Ab[n][tam])

# transforma as matrizes em numpy arrays para realizar as contas posteriores
A = np.array(A) 
b = np.array(b)
x = [0] * tam
x[tam - 1] = b[tam - 1]/A[tam - 1][tam - 1] # primeiro elemento, ou seja, o Xn

for n in range(tam - 2, -1, -1):
    x[n] = ( (b[n] - sum(A[n][n+1:]*x[n+1:]) ) / A[n][n] )


# EXIBE O RESULTADO NA TELA
i = 1
for variable in x:
    print(f'x{i} = {variable:.4f}')
    i += 1
