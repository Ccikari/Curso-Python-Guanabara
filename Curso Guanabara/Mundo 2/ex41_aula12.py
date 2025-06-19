# Continuação dos desafios da Aula 12

# 41. A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
    # até 9 anos: Mirim
    # até 14 anos: Infantil
    # até 19 anos: Junior
    # até 20 anos: Sênior
    # acima: Master
from datetime import date
ano = date.today().year
nasc = int(input("Ano de Nascimento: "))
idade = ano - nasc
if idade <= 9:
    print("Categoria Mirim")
elif idade <=14:
    print("Categoria Infantil")
elif idade <= 19:
    print("Categoria Junior")
elif idade <= 25:
    print("Categoria Sênior")
else:
    print("Categoria Master")

# 42. Refaça o desafio 35 dos triângulos, acrescentando o recusro de mostrar que tipo de triângulo será formado:
    # Equilátero: todos os lados iguais
    # Isósceles: dois lados iguais
    # Escaleno: todos os lados são diferentes
r1 = float(input("Primeiro segmento: "))
r2 = float(input("Segundo segmento: "))
r3 = float(input("Terceiro segmento: "))
if r1 < r2 + r3 and r2 < r1 +  r3 and r3 < r1 + r2:
    print("Os segmentos podem formar um triângulo ", end= "") #faz-se isso para o próximo print continuar na mesma linha
    if r1 == r2 == r3: # Não se usa elif, pois a condição anterior deve ser mantida
        print("equilátero")   
    if r1 != r2 != r3:
        print("escaleno")
    else:
        print("isósceles")
else:
    print("Os segmentos NÃO podem formar um triângulo")

# 43. Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, de acordo com a tabela abaixo:
    # abaixo de 18.5: abaixo do peso
    # entre 18.5 e 25: peso ideal
    # 25 até 30: Sobrepeso
    # 30 até 40: Obesidade
    # Acima de 40: Obesidade Mórbida
peso = float(input("Digite seu peso (Kg): "))
altura = float(input("Digite sua altura (m): "))
imc = peso / (altura ** 2)
if imc < 18.5:
    print("abaixo do peso")
elif 18.5 <= imc < 25:
    print("peso ideal")
elif 25 <= imc < 30:
    print("Sobrepeso")
elif 30 <= imc < 40:
    print("Obesidade")
else:
    print("Obesidade Mórbida")

# 44. Elabore um programa que calcula o valor a ser pago por um produto, considerando seu preço normal e condição de pagamento:
    # à vista dinheiro/cheque: 10% de desconto
    # à vista no cartão: 5% de desconto
    # em até 2x no cartão: preço normal
    # 3x ou mais no cartão: 20% de juros
v = float(input("Valor do Produto: "))
print("""Escolha o método de pagamento:
[ 1 ] A vista (dinheiro/cheque)            
[ 2 ] A vista (Cartão)
[ 3 ] Até 2x no cartão                 
[ 4 ] 3x ou mais no cartão""")
v1 = v * 0.90
v2 = v * 0.95
v4 = v * 1.20
opcao = int(input("Qual o método escolhido? "))
if opcao == 1:
    print("O preço total será R${:.2f}".format(v1))
elif opcao == 2:
    print("O preço total será R${:.2f}".format(v2))
elif opcao == 3:
    parc = int(input("Quantas parcelas? "))
    print("O preço total será R${:.2f} em {}x de R${:.2f}".format(v, parc, v / parc))
elif opcao == 4:
    parc = int(input("Quantas parcelas? "))
    print("O preço total será R${:.2f} em {}x de R${:.2f} com juros".format(v4, parc, v4 / parc))
else:
    print("Opção inválida!")

# 45. Crie um programa que faça o computador jogar Jokempô com você.
from random import randint
from time import sleep
lista = ("Pedra","Papel", "Tesoura")
pc = randint(0, 2)
print("""Suas opções:
[ 0 ] Pedra
[ 1 ] Papel 
[ 2 ] Tesoura """)
vc = int(input("Qual a sua jogada? "))
print("JO")
sleep(1)
print("KEN")
sleep(1)
print("PO!")
print("-=" * 20)
print("O computador escolheu {}".format(lista[pc]))
print("O jogador escolheu {}".format(lista[vc]))
print("-=" * 20)
if pc == 0:
    if vc == 0:
        print("EMPATE")
    elif vc == 1:
        print("VITÓRIA")
    elif vc == 2:
        print("DERROTA")
    else:
        print("Jogada inválida")
if pc == 1:
    if vc == 0:
        print("VITÓRIA")
    elif vc == 1:
        print("EMPATE")
    elif vc == 2:
        print("DERROTA")
    else:
        print("Jogada inválida")
if pc == 2:
    if vc == 0:
        print("VITÓRIA")
    elif vc == 1:
        print("DERROTA")
    elif vc == 2:
        print("EMPATE")
    else:
        print("Jogada inválida")
