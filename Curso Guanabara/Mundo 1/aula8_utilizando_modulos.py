# Aula 8 - Utilizando Módulos

# para incluir alguma coisa que não está incluso no python, usa o comando "import" e o nome do módulo/biblioteca
    # se quiser algo em específico do módulo/biblioteca, usar "from" antes, e depois "import" com a funcionalidade que quero escolher
        # o prof deu exemplos com bebida, comida e doce
            # import bebida - vai importar todas as bebidas disponíveis
            # from doce import pudim - do grupo de doces, vai importar só o pudim

# vamos importar a biblioteca math, que trás várias funções além dos operadores aritméticos, como:
    # ceil - arredondar pra cima
    # floor - arredondar pra baixo
    # trunc - truncar o número, eliminando da vírgula pra frente
    # pow - calcular potência
    # sqrt - calcular raíi
    # factorial - calcular fatorial

# Prática

import math # se quisesse uma funcionalidade em específico, usaria from math import sqrt
num = int(input("Digite um número: "))
raiz = math.sqrt(num) # isso só aparece por causa do import math anterior. Se tivesse importado apenas a funcionalidade, bastaria usar apenas sqrt(num)
print("A raiz de {} é igual a {}".format(num, raiz))
print(f"A raiz de {num} é igual a {raiz}") # uma outra forma que aprendi de fazer
print(f"A raiz de {num} é igual a {math.ceil(raiz)}") # arredondei o resultado para cima

# posso ver as bibliotecas disponíveis no python.org

import random
num = random.random()
print(num)

#se escrever import e usar control + espaço, surge uma infinidade de bibliotecas que posso colocar
    # a comunidade também cria módulos que não vão aparecer aqui
