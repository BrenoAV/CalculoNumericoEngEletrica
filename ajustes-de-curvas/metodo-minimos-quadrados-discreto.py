import numpy as np
import matplotlib.pyplot as plt

"""
Método Mínimos Quadrados: Regressão linear

É necessário informar os valores de x e y que precisam ter a mesma dimensão.

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""
# Constantes
x = np.array([0, 10, 20, 30, 40, 50, 70, 80, 90])
y = np.array([0, 10, 19, 31, 39, 52, 65, 69, 70])


n = len(x) # retorna o número de amostras
sx = np.sum(x) # ∑x
sy = np.sum(y) # ∑y
sx2 = np.sum(x.copy()**2) # ∑x²
sy2 = np.sum(y.copy()**2) # ∑y²
sxy = np.sum(x.copy()*y.copy()) # ∑xy

# y = a0 + a1*x
a1 = (n*sxy - sx*sy)/(n*sx2 - sx**2) 
a0 = sy/n - a1*(sx/n)

# calculando o coeficiente de correlação

r = (n*sxy - sx*sy)/(np.sqrt(n*sx2 - sx**2) * np.sqrt(n*sy2 - sy**2))

# Exibição dos resultados

print(f'sx = {sx}')
print(f'sy = {sy}')
print(f'sx2 = {sx2}')
print(f'sy2 = {sy2}')
print(f'sxy = {sxy}')
print(f'a1 = {a1:.4f}')
print(f'a0 = {a0:.4f}')
print(f'r = {r:.4f}')

# Calculando o valor quando x = 60 utilizando a reta, obtemos que
print(f'y(60) = {a0:.4f} + {a1:.4f}*x = {a0 + a1*60:.4f}')

# Plotando os pontos e a reta da regressão linear

xr = np.linspace(x[0], x[-1], 500) # pega o primeiro termo e o último da amostra
yr = a0 + a1*xr
plt.plot(x, y, 'ro')
plt.plot(xr, yr)
plt.grid()
plt.show()
