# Continuação dos desafios da aula 13

# 51. Desenvolva um programa que leia o primeiro termo e a razão de uma PA (Progressão Aritmética). No final, mostre os 10 primeiros termos dessa progressão
termo = int(input("Qual o primeiro termo? "))
razao = int(input("Qual a razão da PA? "))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print("{}".format(c), end= "->")
print("Esses foram os dez primeiros termos da PA")
    
# 52. Faça um programa que leia um número inteiro e diga se ele é ou não um número primo
n = int(input("Número inteiro: ")) 
for c in range(2, n): # essa solução deve ter erros lógicos
    if n == 0 or n ==1:
        print("Não é um número primo")
        break
    elif n == 2 or n == 3:
        print("É um número primo")
        break
    elif n % c == 0:
        print("Não é um número primo")
        break
    else:
        print("É um número primo")
        break

# Resolução do professor:
num = int(input("Número inteiro: "))
total = 0
for c in range(1, num + 1):
    if num % c == 0:
        print("\033[33m", end=" ")
        total += 1
    else:
        print("\033[31m", end=" ")
    print("{} ".format(c), end=" ")
print("\n\033[mO número {} foi divisível {}x".format(num, total))
if total == 2:
    print("E por isso, ele é PRIMO")
else:
    print("E por isso, ele é NÃO É PRIMO")

# 53. Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços
    # Ex: Apos a sopa; a sacada da casa; a torre da derrota; o lobo ama o bolo; anotaram a data da maratona
frase = str(input("Frase: ")).strip().upper()
palavras = frase.split()
junto = " ".join(palavras)
inverso = " "
for letra in range(len(junto) - 1, -1, -1): # dá pra fazer sem for, usando pal = f3[::-1]
    inverso += junto[letra]
print("O inverso de {} é {}".format(junto, inverso))
if inverso == junto: 
    print("É um palíndromo")
else:
    print("Não é um palíndromo") # por algum motivo não dá certo e não consigo descobrir o pq

#54. Crie um programa que leia o ano de nascimento de sete pessoas. No final, mostre quantas ainda não atingiram a maioridade e quantas já são maiores
    # maioridade: 21 anos
from datetime import date
atual = date.today().year
totmaior = 0
totmenor = 0
for pessoa in range(1, 8):
    nasc = int(input("Em que ano a {} pessoa nasceu? ".format(pessoa)))
    idade = atual - nasc
    if idade >= 21:
        totmaior += 1
    else: 
        totmenor += 1
print("São {} pessoas maiores de idade".format(totmaior))
print("São {} pessoas menores de idade".format(totmenor))

# 55. Faça um programa que leia o peso de cinco pessoa. No final, mostre qual foi o maior e o menor peso lidos
maior = 0
menor = 0
for p in range(1, 6):
    peso = float(input("O peso da {} pessoa: ".format(p)))
    if p == 1:
        maior = p
        menor = p
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print("O maior peso foi {}Kg".format(maior))
print("O menor peso foi {}Kg".format(menor))

# 56. Desenvolva um programa que leia nome, idade e sexo de quatro pessoas. No final do programa, mostre:
    # A média de idade do grupo 
    # Qual é o nome do homem mais velho 
    # Quantas mulheres têm menos de 20 anos
somaidade = 0
mediaidade = 0
maioridadehomem = 0
nomevelho = " "
totmulher20 = 0
for pessoas in range(1, 5):
    print("----- {} PESSOA -----".format(pessoas))
    nome = str(input("Nome: ")).strip()
    idade = int(input("Idade: "))
    sexo = str(input("Sexo [M/F]: ")).strip()
    somaidade += idade
    if pessoas == 1 and sexo in "Mm":
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Mm" and idade > maioridadehomem:
        maioridadehomem = idade
        nomevelho = nome
    if sexo in "Ff" and idade < 20:
        totmulher20 += 1
mediaidade = somaidade / 4
print("A média de idade do grupo é de {} anos".format(mediaidade))
print("O homem mais velho tem {} anos e se chama {}".format(maioridadehomem, nomevelho))
print("São {} mulheres com menos de 20 anos".format(totmulher20))
