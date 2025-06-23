# Desafios da aula 14

# 57. Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores M e F. Caso esteja errado, peça a digitação novamente

sexo = str(input("Qual o seu sexo? [M/F] ")).strip().upper()[0] # o [0] faz pegar só a primeira letra, se a pessoa escrever Masculino, leva o M em consideração e aceita
while sexo not in "MmFf":
    sexo = str(input("Dados inválidos, informe novamente: ")).strip().upper()[0]
print("Sexo {} registrado.".format(sexo))

# 58. Melhore o desafio 028. Só que agora o jogador vai adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
import time
pc = random.randint(0, 10)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 10. Tente adivinhar...")
print("-=-" * 20)
time.sleep(2)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Qual o seu palpite? "))
    palpites += 1
    if jogador == pc:
        acertou = True
    else:
        if jogador < pc:
            print("Mais... Tente mais uma vez. ")
        elif jogador > pc:
            print("Menos... Tente mais uma vez. ")
print("Acertou com {} tentativas. Parabéns!! ".format(palpites))

# 59. Crie um programa que leia dois valores e mostre um menu na tela:
    # [1] somar
    # [2] multiplicar
    # [3] maior
    # [4] novos números
    # [5] sair do programa
        # Seu propgrama deve realizar a operação solicitada em cada caso
n1 = int(input("Primeiro valor: "))
n2 = int(input("Segundo Valor: "))
escolha = 0
while escolha != 5:
    escolha = int(input("""
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair do programa 
O que deseja fazer? """))
    if escolha == 1:
        print(n1 + n2)
    elif escolha == 2:
        print(n1 * n2)
    elif escolha == 3:
            if n1 > n2:
                maior = n1
            else:
                maior = n2
            print("Entre {} e {}, o maior valor  é {}".format(n1, n2, maior))
    elif escolha == 4:
        print("Informe os números novamente: ")
        n1 = int(input("Primeiro valor: "))
        n2 = int(input("Segundo Valor: "))
    elif escolha == 5:
        print("Finalizando...")
    else:
        print("Opção inválida. Tente novamente" )
print("Fim do programa!")
          
# 60. Faça um programa que leia um número qaulquer e mostre seu fatorial.
    # ex 5! = 5x4x3x2x1= 120
from math import factorial
n = int(input("Digite um número para calcular seu fatorial: "))
fatorial = factorial(n)
print("O fatorial de {} é {} ".format(n, fatorial))

n = int(input("Digite um número para calcular seu fatorial: "))
c = n
f = 1
print("Calculando {}! = ".format(n))
while c > 0:
    print("{}".format(c), end= " ")
    print("x" if c > 1 else " = ", end= " ")
    f *= c
    c -= 1
print("{}".format(f))
# dá pra fazer com for, já que conhecemos os limites
                       
# 61. Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while
primeiro = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razão da PA? "))
termo = primeiro
cont = 1
while cont <= 10:
    print("{} -> ".format(termo), end= " ")
    termo += razao
    cont += 1
print("FIM")