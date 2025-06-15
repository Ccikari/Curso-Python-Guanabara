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
n = int(input("Digite um número: "))
if n == 0 or n % 2 == 0:
    print("O número {} é par!".format(n))
else:
    print("O número {} é ímpar!".format(n))
# eo prof fez assim:
n = int(input("Me diga um número qualquer: "))
resultado = n % 2
if resultado == 0:
    print("O número {} é par!".format(n))
else:
    print("O número {} é ímpar!".format(n))

# 31. Desenvolva um programa que pergunte a distância de uma viagem em Km.
    # calcule o preço da passagem, cobrando R$0,50/Km para viagens até 200KM e R$0,45/Km para viagens mais longas
viagem = float(input("Qual a distância (em Km) da viagem? "))
p1 = viagem * 0.50
p2 = viagem * 0.45
if viagem <= 200:
    print("A passagem custa R${:.2f}".format(p1))
else:
    print("A passagem custa R${:.2f}".format(p2))

# 32. Faça um programa que leia um ano qualquer e mostre se ele é BISSEXTO
ano = int(input("Digite o ano: "))
if ano % 400 == 0: 
    print("O ano {} é bissexto".format(ano))
elif ano % 100 == 0:
    print("O ano {} não é bissexto".format(ano))
elif ano % 4 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))
# o prof fez assim: 
import datetime
ano = int(input("Que ano quer analisar? Coloque 0 para analisar o ano atual "))
if ano == 0:
    ano == datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print("O ano {} é bissexto".format(ano))
else:
    print("O ano {} não é bissexto".format(ano))