# Exercícios da aula 10

# 28. Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5,
    # peça para o usuário tentar descobrir qual foi o número escolhido pelo computador
    # o programa deverá escrever na tela se o usuário venceu ou perdeu
import random
import time
n = random.randint(0, 5)
print("-=-" * 20)
print("Vou pensar em um número entre 0 e 5. Tente adivinhar...")
print("-=-" * 20)
time.sleep(2) # faz ele esperar, dando a impressão de estar pensando
num = int(input("Em que número eu pensei? "))
if num == n:
    print("Parabéns! Você conseguiu me vencer!")
else:
    print("Ganhei! Pensei no número {}, não no {}".format(n, num))

# 29. Escreva um programa que leia a velocidade de um carro
    # se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado
    # a multa vai custar R$7,00 por cada Km acima do limite
v = float(input("Qual a velocidade do carro? "))
if v > 80:
    multa = (v - 80) * 7
    print("Multado em R${}".format(multa))
else:
    print("Dirija com segurança!")

# 30. Crie um programa que leia um número inteiro qualquer e mostre se ele é PAR ou ÍMPAR

# 31. Desenvolva um programa que pergunte a distância de uma viagem em Km.
    # calcule o preço da passagem, cobrando R$0,50/Km para viagens até 200KM e R$0,45/Km para viagens mais longas

# 32. Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO

# 33. Faça um programa que leia três números e mostre qual é maior e qual é menor

# 34. Escreva um programa que pregunte o salário de um funcionário e calcule o valor do seu aumento.
    # para salários superiores a R#1.250,00, calcule um aumento de 10%
    # para os inferiores ou iguais, o aumento é de 15%

# 35. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
    # em outra aula ele vai ensinar um complemento para essa questão