# Desafios da Aula 13

# 46. Faça um programa que mostre na tela uma contagem regressiva para o estouro de fogos de artifício, indo de 10 até 0, com pausa de 1 segundo entre eles.
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print("Feliz Ano Novo!!!!!")

# 47. Crie um programa que mostre na tela todos os número pares que estão no intervalo de 1 a 50
for c in range(2, 51, 2):
    print(c, end = " ") # end = deixa tudo na mesma linha
print("Acabou")

# 48. Faça um programa que calcule a soma entre todos os números ímpares que são múltiplos de três e que se encontram no intervalo de 1 até 500
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        cont = cont +1 # mesma coisa de cont += 1
        soma = soma + c # mesma coisa de soma += c
print("A soma dos {} valores é igual a {}".format(cont, soma))

# 49. Refaça o desafio 009, mostrando a tabuada de um número que o usuário escolher, só que utilizando um laço for
n = int(input("Digite um número: "))
for c in range(1, 11):
    t = n * c
    print("{} x {:2} = {}".format(n, c, t))

# 50. Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o
soma = 0
for c in range(1, 7):
    n = int(input("Digite o {}° valor: ".format(c)))
    if n % 2 == 0:
        soma += n
print("A soma dos valores pares é {}".format(soma))
        