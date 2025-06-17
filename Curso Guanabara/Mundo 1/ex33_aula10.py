# Continuação dos Exercícios da Aula 10

# 33. Faça um programa que leia três números e mostre qual é maior e qual é menor
n1 = float(input("Digite o primeiro número: "))
n2 = float(input("Digite o segundo número: "))
n3 = float(input("Digite o terceiro número: "))
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print("O menor número é {}".format(menor))
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2: 
    maior = n3
print("O maior número é {}".format(maior))

# 34. Escreva um programa que pregunte o salário de um funcionário e calcule o valor do seu aumento.
    # para salários superiores a R$1.250,00, calcule um aumento de 10%
    # para os inferiores ou iguais, o aumento é de 15%
salario = float(input("Qual o seu salário? "))
if salario > 1250:
    print("O salário será de R${:.2f}".format((salario * 1.10)))
else:
    print("O salário será de R${:.2f}".format((salario * 1.15)))

# 35. Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo
    # em outra aula ele vai ensinar um complemento para essa questão
r1 = float(input("Digite o comprimento da primeira reta: "))
r2 = float(input("Digite o comprimento da segunda reta: "))
r3 = float(input("Digite o comprimento da terceira reta: "))
if r1 + r2 > r3 and r1 + r3 > r2 and r2 + r3 > r1:
    print("As retas podem formar um triângulo!")
else:
    print("As retas NÃO podem formar um triângulo!")