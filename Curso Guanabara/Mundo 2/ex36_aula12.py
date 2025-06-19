# Desafios da Aula 12

# 36. Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. 
    # O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar
        # Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.
casa = float(input("Qual o valor da casa? R$"))
salario = float(input("Qual o salário do comprador? R$"))
anos = int(input("Quantos anos de financiamento? "))
prest = casa / (anos * 12)
if prest > salario * 0.3:
    print("Com prestação de R${:.2f} para um salário de r${:.2f}, o empréstimo foi negado".format(prest, salario))
else:
    print("Com prestação de R${:.2f} para um salário de r${:.2f}, o empréstimo foi autorizado".format(prest, salario))

# 37. Escreva um programa que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
    # 1 para binário
    # 2 para octal 
    # 3 para hexadecimal
num = int(input("Digite um número inteiro: "))
print (""" Escolha uma das bases para conversão:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL """)
opção = int(input("Sua opção: "))
if opção == 1:
    print(" {} convertido para BINÁRIO é igual a {}".format(num, bin(num)[2:])) # o [2:] é pq o python, ao calcular, coloca 0b, 0o ou 0h na frente, escrevendo isso para começar do dígito 2 (0, 1, 2)
elif opção == 2:
     print(" {} convertido para OCTAL é igual a {}".format(num, oct(num)[2:]))
elif opção == 3:
     print(" {} convertido para HEXADECIMAL é igual a {}".format(num, hex(num)[2:]))
else:
    print("Opção inválida. Tente novamente.")


# 38. Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
    # "O primeiro valor é maior"
    # "O segundo valor é maior"
    # "Não existe valor maior, os dois são iguais"
n1 = int(input("Primeiro número: "))
n2 = int(input("Segundo número: "))
if n1 > n2:
    print("O primeiro valor é maior")
elif n2 > n1:
    print("O segundo valor é maior")
else:
    print("Não existe valor maior, os dois são iguais")

# 39. Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
    # Se ele vai se alistar ao serviço militar
    # Se é hora de se alistar
    # Se já passou do tempo do alistamento
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo
ano = int(input("Digite seu ano de nascimento: "))
atual = 2025
if atual - ano == 18:
    print("Está na hora de se alistar!")
elif atual - ano < 18:
    print("Ainda não é o momento, falta {} ano(s)".format(18 - (atual - ano))) # o prof fez saldo = 18 - idade
else:
    print("Já passou do tempo de se alistar faz {} anos(s)".format((atual -ano) - 18)) # o prof fez saldo = idade - 18

# 40. Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
    # abaixo de 5.0: REPROVADO
    # entre 5.0 e 6.9: RECUPERAÇÃO
    # 7.0 ou superior: APROVADO
nota1 = float(input("Nota da primeira unidade: "))
nota2 = float(input("Nota da segunda unidade: "))
media = (nota1 + nota2) / 2
if media < 5.0:
    print("REPROVADO")
elif 5.0 <= media <= 6.9:
    print("RECUPERAÇÃO")
else:
    print("APROVADO")