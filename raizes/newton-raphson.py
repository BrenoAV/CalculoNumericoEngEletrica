"""
Método iterativo: Newton-Rapshon

É necessário informar a função e sua derivada no campo das definições das funções
e escolher um valor próximo da raiz, pode ser utilizando novamente uma ferramenta 
gráfica com o matplolib

Para trocar os valores exibidos das casas decimais é necessário alterar o .4f para
.nf, onde n é o número de casas decimais.

Autor: brenoAV
"""


# Insira os valores das constantes

x = 0.75 # Valor inicial do método (obs: ele tem que está no intervalo pré definido)
E = 1e-2 # Critério de parada sendo a aproximação de f(x) de zero
max_i = 30 # Máximo de interações possíveis
i = 0 # Número de interações

def funcao(x):
    "Função que se deseja obter a raíz"
    return x**3 - 9*x + 5

def derivada(x):
    """Derivada da função que se deseja obter a raíz"""
    return 3*x**2 - 9


print(f'{"Interação":^9} {"x":^10} {"f(x)":^10} {"f1(x)":^10}') #f1(x) é a derivada
while True:
    i += 1
    print(f'{i:^9} {x:^10.4f} {funcao(x):^10.4f} {derivada(x):^10.4f}')
    
    if abs(funcao(x)) < E or i == max_i:
        break

    x = x - funcao(x)/derivada(x)
    
    
print(f'\nLogo, o valor de x é {x:.4f}.')
