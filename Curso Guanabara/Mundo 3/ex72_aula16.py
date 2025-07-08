# Desafios da Aula 16

# 72. Crie um programa que tenha uma tupla totalmente preenchida com uma contagem por extenso, de zero até 20.
    # O programa deverá ler um número pelo teclado, entre 0 e 20 e mostrá-lo por extenso
next = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez") # fiz até 10, 20 é sacanegem
c = int(input("Digite um número de 0 a 10: "))
if c in range(0, 10):
    print(f"Você digitou o número {next[c]}")
else:
    print("O número digitado não está entre 0 e 10.")
# Resolução do professor:
cont = ("zero", "um", "dois", "três", "quatro", "cinco", "seis", "sete", "oito", "nove", "dez")
while True:
    num = int(input("Digite um número de 0 a 10: "))
    if 0 <= num <= 20:
        break
    print("Tente novamente. ", end=" ")
print(f"Você digitou o número {cont[num]}")

# 73. Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
    # A) Apenas os 5 primeiros colocados. 
    # B) Os últimos colocados da tabela 
    # C) Uma lista dos times em ordem alfabética 
    # D) Em que posição está o time da Chapecoense (Saudosa, vou usar o Vitória)
pos = ("Flamengo", "Cruzeiro", "RB bragantino", "Palmeiras", "Bahia", "Fluminense", "Atletico-MG", "Botafogo", "Mirassol", "Corinthians", "Grêmio", "Ceará", "Vasco", "São Paulo", "Santos", "Vitória", "Internacional", "Fortaleza", "Juventude", "Sport")
print("Lista de Times do Brasileirão: ")
for p in pos:
    print(p) # vai listar os times
print(f"Os cinco primeiros colocados são: {pos[:5]}")
print(f"Os últimos colocados são: {pos[16:]}") # poderia ser [-4:]
print(f"Em ordem alfabética: {sorted(pos)}")
print(f"O Vitória está na {pos.index("Vitória") + 1}ª posição")

# 74. Crie um programa que vai gerar cinco números aleatórios e colocarem uma tupla.
    # Depois disso, mostre a listagem de números gerados e também indique o menor e o maior valor que estão na tupla.
from random import randint
lista = (randint(0,100), randint(0,100), randint(0,100), randint(0,100), randint(0,100))
print(f"Foram sorteados os valores {lista}")
print(f"O maior valor sorteado foi {max(lista)}")
print(f"O maior valor sorteado foi {min(lista)}")

# 75.  Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
    # A) Quantas vezes apareceu o valor 9 
    # B) Em que posição foi digitado o primeiro valor 3 
    # C) Quais foram os números pares
num =(int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")), int(input("Digite um número: ")))
print(f"Você digitou os valores {num}")
print(f"O valor 9 apareceu {num.count(9)} vez(es)")
if 3 in num:
    print(f"O valor 3 foi digitado na {num.index(3) + 1}ª posição")
else:
    print("O valor 3 não foi digitado")
print(f"Os valores pares digitados foram: ", end=" ")
for n in num:
    if n % 2 == 0:
        print(n)

# 76. Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
    # No final, mostre uma listagem de preços, organizando os dados em forma tabular.
prod = ("Cuscuz", "1,50", "Pão Integral", "13,90", "Azeite", "59,90", "Mochila", "125,99")
for item in range(0, len(prod)):
    if item % 2 == 0:
        print(f"{prod[item]:.<30}",end=" ")
    else:
        print(f"R${prod[item]}")

# 77. Crie um programa que tenha uma tupla com várias palavras (não usar acentos). Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
pal = ("sabia", "python", "palavra", "deserto", "stranding", "cobra", "solida")
for p in pal:
    print(f"\nA palavra {p.upper()} tem as vogais:", end=" ")
    for vog in p:
        if vog.lower() in "aeiou":
            print(vog, end=" ")