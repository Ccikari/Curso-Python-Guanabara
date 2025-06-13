# Aula 7 - Operadores Aritméticos

# Operadores Aritméticos em Python
    # Adição (+). Exemplo: 5 + 2 == 7. Sempre utiliza dois símbolos de igualdade
    # Subtração (-). Exemplo: 5 - 2 == 3.
    # Multiplicação (*). Exemplo: 5 * 2 == 10.
    # Divisão (/). Exemplo: 5 / 2 == 2.5.
    # Potência (**). Exemplo: 5 ** 2 == 25. 
    # Divisão Inteira (//). Exemplo: 5 // 2 == 2. Retorna o quociente da divisão sem o resto.
    # Módulo ou Resto da Divisão (%). Exemplo: 5 % 2 == 1. Retorna o resto da divisão. (2 + 2 == 4, para 5 resta 1).

# Ordem de Precedência dos Operadores Aritméticos. (Quem vem primeiro?)
    # 1. Parênteses ()
    # 2. Exponenciação (**)
    # 3. Multiplicação (*), Divisão (/), Divisão Inteira (//) e Módulo (%). Quem aparecer primeiro
    # 4. Adição (+) e Subtração (-). Quem aparecer primeiro
    # Deve-se conhecer a ordem, executar um programa e funcionar não siginifica que está correto.

# Exemplos de Operadores Aritméticos
    # 5 + 3 * 2 == 11. Pois 3 * 2 == 6, depois 5 + 6 == 11.
    # 3 * 5 + 4 ** 2 == 31. Pois 4 ** 2 == 16, depois 3 * 5 == 15, e por último 15 + 16 == 31.
    # 3 * (5 + 4) ** 2 == 243. Pois 5 + 4 == 9, depois 9 ** 2 == 81, e por último 3 * 81 == 243.

# Aleatoriedades
nome = input("Digite seu nome: ")
print("Prazer em te conhecer {}!".format(nome))
print("Prazer em te conhecer {:>20}!".format(nome)) # Alinha à direita
print("Prazer em te conhecer {:^10}!".format(nome)) # Alinha ao centro
print("Prazer em te conhecer {:<35}!".format(nome)) # Alinha à esquerda
print("Prazer em te conhecer {:=^20}!".format(nome)) # Alinha ao centro e preenche com '='

# Mais exemplos de uso de operadores aritméticos
n1 = int(input("Um valor: "))
n2 = int(input("Outro valor: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print("A soma é {}, o produto é {}, a divisão é {}, a divisão inteira é {}, a exponenciação é {}.".format(s, m, d, di, e))
print("A divisão é {:.3f}.".format(d))  # Exibe a divisão com três casas decimais
# É possível juntar os prints colocando , end= " ") no fim. Não é obrigatório as aspas serem vazias.
# Também dá para quebrar as linhas colocando \n no meio da função

# Exercícios

# 5. Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor

# 6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

# 7. Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.

# 8. Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.

# 9. Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.

# 10. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere U$1,00 = R$3,27)

# 11. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2>

# 12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.

# 13. Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
