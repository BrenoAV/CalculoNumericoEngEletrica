import numpy as np
import matplotlib.pyplot as plt


"""
Método Mínimos Quadrados: Regressão Polinomial

É necessário informar os valores de x e y que precisam ter a mesma dimensão.
E então escolher o grau do polinômio, lembrando que esse grau é menor do que
o número de dados.

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""

x = np.array([0, 10, 20, 30, 40, 50, 70, 80, 90])
y = np.array([0, 10, 19, 31, 39, 52, 65, 69, 70])

grau = int(input(f'Informe o grau que deseja o polinômio ( < {len(x)}): '))

n = len(x)
sx = np.array([0]*(2*grau + 1))
syx = np.array([0]*(grau+1))
# calculando os somatórios de x
for i in range(0, len(sx)): # calcula todos ∑x
    sx[i] = np.sum(x**i)

for i in range(0, len(syx)): # calcula todos ∑y
    syx[i] = np.sum((x**i)*y)

# Cálculando as médias
my = syx[0]/n # ∑y / n
mx = sx[1]/n # ∑x / n

# Calculando a matriz dos coeficientes de maneira geral

A = np.array([[0]*(grau + 1)]*(grau + 1))
inicio = 0
fim = grau + 1
for i in range(0, grau + 1):
    aux = inicio
    for j in range(0, grau+1):
        
        A[i][j] = sx[aux]
        aux += 1

    inicio += 1
    fim += 1

# Calculando a matriz B de maneira geral
B = np.array([0]*(grau+1))
for i in range(0, grau + 1):
    B[i] = syx[i]

a = np.linalg.solve(A, B)


# Cálculo de st
st = 0
for i in range(0, n):
    st += (y[i] - my)**2

# Cálculo de sr genérico
sr = 0
for i in range(0, n):
    y_pol = 0 
    for m in range(0, grau + 1):
        y_pol += a[m]*(x[i]**m)
    sr += (y[i] - y_pol) ** 2


r = (st - sr)/st

# Exibição dos resultados

print(f'Os coeficientes são (a0 + a1*x + a2*x^2 + ... + an*x^n)')
for i in range(0, len(a)):
    print(f'a{i} = {a[i]:.4f}')
print(f'r = {r}')


# Plotando os pontos e o polinômio da regressão

xp = np.linspace(x[0], x[-1], 500) # pega o primeiro termo e o último da amostra

yp = 0
for i in range(0, len(a)):
    yp += a[i]*xp**i

plt.plot(x, y, 'ro')
plt.plot(xp, yp)
plt.grid()
plt.show()
