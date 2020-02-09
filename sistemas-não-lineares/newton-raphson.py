import numpy as np
from numpy.linalg import inv

"""
Método iterativo: Newton-Raphson

É necessário ajustar xo, F, J para cada situação, tendo cuidado no tamanho dos
vetores e da forma que eles devem está para que o algoritmo possa funcionar
corretamente.

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""

# CONSTANTES
xo = np.array([1, 1]) # aproximação inicial
max_i = 500 # máximo de iterações
E = 0.0001 # critério de parada


i = 0 # número de iterações
tam = len(xo) # número de variáveis no sistema
xabs = np.array([0]*tam, dtype= np.float) # valores absolutos de x usados para comparar o erro posteriormente
d = np.array([0]*tam, dtype= np.float) # erro

while True:
    i += 1

    F = np.array([xo[0]**2 + xo[1]**2 - 4, 2*xo[0] - xo[1]**2]) # Matriz da função F
    J = np.array([[2*xo[0], 2*xo[1]], [2, -2*xo[1]]]) # Matriz do Jacobiano
    
    dx = np.dot(inv(J), F)
    xn = xo - dx

    # Verificação da convergência
    for n in range(0, tam):
        d[n] = ( abs(xn[n]) - abs(xo[n]) )
        xabs[n] = abs(xn[n])

    if abs(max(d)/max(xabs)) < E or i == max_i:
        break
    
    xo = xn.copy()


# Exibição dos valores
cont = 1
print(f'O resultado convergiu com {i} iterações:')
for i in xn:
    print(f'x{cont} = {i:.4f}')
    cont += 1
