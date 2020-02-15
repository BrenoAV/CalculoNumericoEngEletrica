import numpy as np
import matplotlib.pyplot as plt


"""
Integração Numérica: Método dos Trapézios

É necessário informar a função f e o algoritmo irá perguntar os limites de integração
além da quantidade de pontos que se deseja subdividir o intervalo.

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""


def f(x):
    return 1/x # informe a função que se deseja integrar

a = float(input('Qual o valor de a (limite inferior): '))
b = float(input('Qual o valor de b (limite superior): '))
n = int(input('Informe quantidade de intervalos: '))

h = (b-a)/n
x = np.array([0]*(n + 1), dtype= np.float)
y = np.array([0]*(n + 1), dtype= np.float)

# Preencher a tabela x e y
x[0] = a
y[0] = f(x[0])
x[-1] = b
y[-1] = f(x[-1])

for i in range(1, n):
    x[i] = a + i*h
    y[i] = f(x[i])

# At = h/2 * [y0 + 2*∑yi + yn]

At = y[0] + y[-1]
Syi = 0
for i in range(1, n):
    Syi += y[i]
At += 2*Syi
At *= h/2

# Exibição do resultado
print(f'O valor da integral de f de {a} até {b} para {n} divisões igualmente separadas é {At:.4f}')

xg = np.linspace(x[0], x[-1], 100) # x gráfico
yg = f(xg)
plt.figure(figsize=(10, 10)) # aumentar tamanho do gráfico
plt.plot(xg, yg, 'k')

# PLOTAR AS RETAS PARALELAS AO EIXO Y para formar um trapézio
for i in range(0, n+1):
    p1 = [x[i],y[i]]
    p2 = [x[i], 0]
    x_values = [p1[0], p2[0]]
    y_values = [p1[1], p2[1]]
    plt.plot(x_values, y_values, 'b', linestyle='dashed', linewidth= .5)

plt.plot(x, y, 'b', linestyle='dashed', linewidth= .5)
plt.grid()
plt.show()
