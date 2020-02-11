import numpy as np


"""
Interpolação: Polinômios Interpoladores de Lagrange

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
L = np.array([0]*n, dtype= np.float)


for k in range(0, n):
    L_num = 1
    L_den = 1
    for j in range(0, n): # Produtório de L aplicado no ponto x_
        if j != k:
            L_num *= (x_ - x[j])
            L_den *= (x[k] - x[j])
    L[k] = L_num/L_den  

# Cálculo do polinômio interpolador
Pn = 0
for i in range(0, n):
    Pn += y[i]*L[i]

print(f'O valor interpolado de f({x_}) = {Pn:.4f}')
