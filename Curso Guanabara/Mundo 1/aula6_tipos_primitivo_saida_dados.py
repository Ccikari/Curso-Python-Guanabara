# Aula 6 - Tipos Primitivos e Saída de Dados

# voltando ao exercício 3 da aula 4, onde o usuário digitou dois números e a soma não funcionou corretamente
n1 = input("Digite o primeiro número: ")  # Lê o primeiro número como string
n2 = input("Digite o segundo número: ")  # Lê o segundo número como string
s = n1 + n2  # Soma os dois números como strings, resultando em concatenação
print("A soma é:", s)  # Exibe a soma como string, resultando em concatenação e nâo adição
# Para corrigir, precisamos converter as strings para números inteiros ou flutuantes

n1 = int(input("Digite o primeiro número: "))  # Converte o primeiro número para inteiro
n2 = int(input("Digite o segundo número: "))  # Converte o segundo número para inteiro
s = n1 + n2  # Soma os dois números como inteiros
print("A soma é:", s)  # Exibe a soma como número inteiro

# Os 4 Tipos primitivos mais básicos em Python: int(), float(), bool(), str()
    # int() - Números inteiros (7, -4, 0, 987654321)
    # float() - Números reais (7.0, -4.5, 0.0, 987654321.123456789)
    # bool() - Valores booleanos (True, False)
    # str() - Strings (texto) ("Olá", "123", "7.5", "")

# Forma diferente e recomendada de usar o print()
print("A soma vale {}".format(s))  # Exibe a soma usando o método format, que formata a string
print("A soma entre {} e {} vale {}".format(n1, n2, s))  # Exibe a soma entre os dois números com formatação

# Ver o tipo de uma variável
n3 = input("Digite um número: ")
print(type(n3))  # Exibe o tipo da variável n3, que será string
n4 = int(input("Digite outro número: "))
print(type(n4))  # Exibe o tipo da variável n4, que será inteiro 
x1 = input("Digite algo: ")
print(x1.isnumeric())  # Verifica se o valor digitado é numérico (apenas números) - True ou False
print(x1.isalpha())  # Verifica se o valor digitado é alfabético (apenas letras) - True ou False
print(x1.isalnum())  # Verifica se o valor digitado é alfanumérico (letras e números) - True ou False
print(x1.isupper())  # Verifica se o valor digitado está em maiúsculas - True ou False
print(x1.islower())  # Verifica se o valor digitado está em minúsculas - True ou False
print(x1.isprintable())  # Verifica se o valor digitado é imprimível (não contém caracteres especiais) - True ou False
# tem vários outros métodos para verificar o tipo de dado, como isdecimal(), isspace(), etc.

# Exercício 3 - Crie um programa que leia dois números e mostre a soma entre eles.
num1 = int(input("Digite o primeiro número: "))  # Lê o primeiro número e converte para inteiro
num2 = int(input("Digite o segundo número: "))  # Lê o segundo número e converte para inteiro
soma = num1 + num2  # Soma os dois números
print("A soma entre {} e {} é {}".format(num1, num2, soma))  # Exibe a soma formatada
print("A soma vale {}".format(num1 + num2)) # Exibe a soma diretamente, sem armazenar em uma variável.

# Exercício 4 - Faça um programa que leia algo pelo teclado e mostre na tela o seu time primitivo e todas as informações possíveis sobre ela.
algo = input("Digite algo:")  # Lê algo do teclado
print("O Tipo primitvo é: {}".format(type(algo)))  # Exibe o tipo primitivo do dado, que sempre será string, pela forma como foi formatado
print("É um número?", algo.isnumeric())  # Verifica se o dado é numérico
print("É alfabético?", algo.isalpha())  # Verifica se o dado é alfabético
print("É alfanumérico?", algo.isalnum())  # Verifica se o dado é alfanumérico
print("Está em maiúsculas?", algo.isupper())  # Verifica se o dado está em maiúsculas
print("Está em minúsculas?", algo.islower())  # Verifica se o dado está em minúsculas
# dentre vários outros métodos que podem ser usados para verificar o tipo de dado
