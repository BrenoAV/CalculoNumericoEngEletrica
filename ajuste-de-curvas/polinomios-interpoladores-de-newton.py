import numpy as np


"""
Interpolação: Polinômios Interpoladores de Newton

É necessário informar os valores de x e y que precisam ter a mesma dimensão.
E então o valor que se dejesa obter da interporlação em x_.

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""

# CONSTANTES
x = np.array([20, 25, 35])
y = np.array([1.12, 1.06, 0.94])
x_ = 30 # valor que se deseja interporlar

n = len(x)
a = np.array([[0]*n]*n, dtype= np.float)

for i in range(0, n): # atribui a primeira coluna os valores de y
    a[i][0] = y[i]

for j in range(1, n): # calcula os valores dos coeficientes de diferença finita
    for i in range(0, n - j):
        a[i][j] = (a[i+1][j-1] - a[i][j-1])/(x[i+j] - x[i])

# Pn(x) = a0 + a1*(x - x0) + a2*(x - x0)*(x - x1) + ... + an*(x - x0)*(x - x1)*...*(x - x(n-1))

pn = 0
mult = 1
for i in range(0, n):
    pn += a[0][i]*mult
    mult *= (x_ - x[i])

print(f'O valor interpolado de f({x_}) = {pn:.4f}')
