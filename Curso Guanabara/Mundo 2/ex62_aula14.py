# Continuação do Desafios da aula 14

# 62. Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais alguns termos. O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razão da PA? "))
termo = primeiro
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end= " ")
        termo += razao
        cont += 1
    print("PAUSA")
    mais = int(input("Quantos termos você quer a mais? "))
print("PA finalizada com {} termos mostrados. ".format(total))

# 63. Escreva um programa que leia um número n inteiro qualquer e mostre na tela os n primeiros elementos de uma Seqência de Fibonacci
    # ex: 0 -> 1 -> 1 -> 2 -> 3 -> 5 -> 8
print("-" * 30)
print("Sequência de Fibonacci")
print("-" * 30)
n = int(input("Quantos termos quer mostar? "))
t1 = 0
t2 = 1
print("~" * 30)
print("{} -> {}".format(t1, t2), end= " ")
cont = 3
while cont <= n:
    t3 = t2 + t1
    print("-> {} ".format(t3), end= " ")
    t1 = t2
    t2 = t3
    cont += 1
print("FIM")

# 64. Crie um progama que leia vários números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição da parada.
    # No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsidade o flag)
n1 = 0
cont = 0
soma = 0
while n1 != 999:
    n1 = int(input("Digite um valor [999 para parar]: ")) 
    cont = cont + 1
    soma = soma + n1
contfinal = cont - 1
somafinal = soma - 999
print("Após {} números digitados, a soma foi de {}".format(contfinal, somafinal))

# 65. Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a media entre todos os valores e qual foi o maior e o menor número lidos.
    # O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores
resp = "S"
soma = quant = media = marior = menor = 0
while resp in "Ss":
    num = int(input("Digite um número: "))
    soma += num
    quant += 1
    if quant == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    resp = str(input("Quer continuar? [S/N] ")).upper().strip()[0]
media = soma / quant
print("Você digitou {} números e a média foi {:.2f}".format(quant, media))
print("O maior valor foi {} e o menor {}".format(maior, menor))
