"""
Método Intervalar: Bissecção

É necessário saber os intervalos onde existe somente uma raiz entre [a, b]. Você 
pode plotar esse gráfico usando matplotlib ou qualquer ferramenta para fixar os
intervalos usados no método.

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""

# Insira os valores das constantes
a = 0.5 # Valor de x à Esquerda
b = 1.0 # Valor de x à Direita
E = 1e-2 # Critério de parada sendo a aproximação de f(x) de zero
max_i = 30 # máximo de interações possíveis
i = 0 # número de interações


def funcao(x):
    "Função que se deseja obter a raíz em um intervalo"
    return x**3 - 9*x + 5 # mude a função para qualquer uma do seu interesse

print(f'{"Interação":^9} {"a":^10} {"b":^10} {"x":^10} {"f(x)":^10}')
while True:
    i += 1
    x = (a + b)/2 # retorna o valor da raiz refinada    
    print(f'{i:^9} {a:^10.4f} {b:^10.4f} {x:^10.4f} {funcao(x):^10.4f}')
    if funcao(x)*funcao(a) > 0:
        a = x
    else:
        b = x
    if abs(funcao(x)) < E  or i == max_i:
        break

print(f'\nLogo, o valor de x é {x:.4f}.')
