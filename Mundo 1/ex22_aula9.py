# Exercícios da Aula 9

# 22. Crie um programa que leia o nome completo de uma pessoa e mostre:
    # o nomes com todas as letras maiúsculas;
    # o nome com todas as letras minúscula;
    # quantas letras ao todo (sem considerar espaços)
    # quantas letras tem o primeiro nome.
nome = str(input("Digite seu nome completo: ")).strip() # sempre deixar explícito o tipo (str, int, float); já pode usar o strip aqui
print(nome.upper())
print(nome.lower())
print(len(nome) - nome.count(" "))
print( "Seu primeiro nome tem {} letras".format(nome.find(" "))) # . find vai achar a localização do primeiro espaço e, consequentemente, o tamanho do primeiro nome
# existe outra maneira mais trabalhosa
separa = nome.split()
print("Seu primeiro nome é {} e ele tem {} letras".format(separa[0], len(separa[0])))

print("-" * 30)

# 23. Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos digitos separados
    # ex: digite um número: 1834'
    # unidade: 4
    # dezena: 3
    # centena: 8
    # milhar: 1
n = int(input("Digite um número de 0 a 9999: "))
num = str(n)
u = print("Unidade: {}".format(num[3]))
d = print("Dezena: {} ".format(num[2]))
c = print("Centena: {}".format(num[1]))
m = print("Milhar: {}".format(num[0])) # o problema disso é que se o número não tiver 4 dígitos, vai dar erro
# Solução melhor
n = int(input("Digite um número de 0 a 9999: "))
u = print("Unidade: {}".format(n // 1 % 10))
d = print("Dezena: {} ".format(n // 10 % 10))
c = print("Centena: {}".format(n // 100 % 10))
m = print("Milhar: {}".format(n // 1000 % 10))


print("-" * 30)

# 24. Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com a palavra "Santo"
cidade = str(input("Digite o nome da cidade: ")).strip().capitalize() # ele não usou capitalize e fez print(cidade[:5].upper() == "SANTO")
print("Santo" in cidade) # n sei o que fiz, mas só com esse comando ele considera apenas a primeira palavra

print("-" * 30)

# 25. Crie um programa que leia o nome de uma pessoa e diga se ela tem "Silva" no nome
nome = str(input("Qual seu nome? ")).strip()
print("Seu nome tem Silva? {}".format("silva" in nome.lower()))

print("-" * 30)

# 26. Faça um programa que leia uma frase pelo teclado e mostre:
    # quantas vezes aparece a letra "A"
    # em que posição ela aparece a primeira vez
    # em que posição ela aparece a última vez
frase = str(input("Escreva uma frase: ")).upper(). strip()
print("A letra A aparece {} vezes".format(frase.count("A")))
print("A letra A aparece pela primeira vez na posição {}".format(frase.find("A") + 1)) # + 1 pois do jeito que estava o resultado seria 0
print("A letra A apareceu pela última vez na posição {}".format(frase.rfind("A") + 1)) # procure a partir do lado direito

print("-" * 30)

# 27. Faça um programa que leia o nome completo de uma pessoa e mostre em seguida o primeiro e o último nome separadamente
    # ex: Ana Maria de Souza
    # primeiro: Ana
    # último: Souza
nome = str(input("Digite seu nome completo: ")).strip().split()
print("Seu primeiro nome é: {}".format(nome[0]))
print("Seu último nome é: {}".format(nome[len(nome) - 1]))