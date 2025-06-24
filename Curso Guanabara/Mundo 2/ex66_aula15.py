# Desafios da Aula 15

# 66. Crie um programa que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar 999, que é a condição de parada.
    # No final, mostre quantos números foram digitados e qual a soma entre eles (desconsiderando a flag)
n = cont = s = 0
while True:
    n = int(input("Digite um valor: "))
    if n == 999:
        break
    cont += 1
    s += n
print(f"Foram digitados {cont} números e a soma entre eles foi de {s}")

# 67. Faça um programa que faça a tabuada de vários números, um de cada vez. O programa será interrompido quando o número pedido for negativo
n = c = 0
while True:
    n = int(input("Digiter um número para ver sua tabuada: "))
    if n < 0:
        break
    for c in range(1, 11):
        tab = n * c
        print(f" {n} x {c:2} = {tab}")
print("FIM")
    
# 68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.
from random import randint
v = 0
while True:
    jogador = int(input("Diga um valor: "))
    pc = randint(0, 11)
    total = jogador + pc
    tipo = " "
    while tipo not in "PpIi": 
        tipo = str(input("Par ou ímpar? ")).strip().upper()[0]
    print(f"Você jogou {jogador} e a máquina {pc}, dando {total}")
    print("Deu par" if total % 2 == 0 else "Deu impar")
    if tipo == "P":
        if total % 2 == 0:
            print("Você venceu!!")
            v += 1
        else:
            print("Você perdeu!")
            break
    if tipo == "I":
        if total % 2 == 0:
            print("Você perdeu!")
            break
        else:
            print("Vocêw venceu!!")
            v += 1
print(f"Fim de jogo. Você venceu {v} vezes")

# 69. Crie um programa que leia a idade e o sexo de várias pessoas. A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, mostre:
    # a) quantas pessoas tem mais de 18 anos
    # b) quantos homens foram cadastrados 
    # c) quantas mulheres tem menos de 20 anos
tot18 = toth = totm20 = 0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo: ")).strip().upper()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        toth += 1
    if sexo == "F" and idade < 20:
        totm20 += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? ")).strip().upper()[0]
    if resp == "N":
        break
print(f"Há {tot18} pessoas com mais de 18 anos, {toth} homens cadastrados e {totm20} mulheres com menos de 20 anos")

# 70. Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar. No final, mostre:
    # a) qual é o total gasto nha compra 
    # b) quantos produtos custam mais de R$1000 
    # c) qual é o nome do produto mais barato
total = totm = menor = cont = 0
while True:
    produto = str(input("Produto: "))
    preco = float(input("Preço: R$"))
    cont += 1
    total += preco
    if preco > 1000:
        totm += 1
    if cont == 1:
        menor = preco
    else:
        if preco < menor:
            menor = preco
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar [S/N] ")).strip().upper()[0]
    if resp == "N":
        break
print(f"O total gasto na compra foi R${total:.2f}")
print(f"{totm} produto(s) custam mais de R$1000 ")
print(f"O produto mais barato é {menor} ")

# 71. Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao usuário qual o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues.
    # OBS: considere que o caixa possui cédulas de R$50, R$20, R$10 e R$1.
valor = int(input("Quanto deseja sacar? R$"))
total = valor
ced = 50
totced = 0
while True:
    if total >= ced:
        total -= ced
        totced += 1
    else:
        if totced > 0:
            print(f"{totced} cédulas de R${ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totced = 0
        if total == 0:
            break
