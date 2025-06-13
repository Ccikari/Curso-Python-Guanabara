# Aula 4 - Primeiros comandos em Python3

print("Olá, Mundo!") # toda função fica entre parênteses (string) == Olá Mundo!
print(7 + 4) # números, para calcular, não ficam entre aspas = 11
print("7 + 4") # entre aspas = 7 + 4
print("7" + "4") # entre aspas, mas com números = 74 (string)
print("Olá" , 5) # Olá 5 (string e número)

# Variáveis - são espaços na memória do computador que guardam valores

nome = "Caio" # variável nome recebe o valor Caio
idade = 20 # variável idade recebe o valor 20
peso = 84.5 # variável peso recebe o valor 84.5
# Para mostrar os valores das variáveis, basta usar a função print
print(nome, idade, peso) # Caio 20 84.5; (nome + idade + peso) daria erro, pois são tipos diferentes

# Criando uma interação com o usuário

nome = input("Qual é o seu nome? ") # input() recebe o valor digitado pelo usuário
idade = input("Qual é a sua idade? ") # input() recebe o valor digitado pelo usuário
peso = input("Qual é o seu peso? ") # input() recebe o valor digitado pelo usuário
print("Olá", nome, "você tem", idade, "anos e pesa", peso, "kg") # Olá Caio você tem 20 anos e pesa 84.5 kg

#-------------------------------------------- Exercícios --------------------------------------------

# 1. Crie um script Python que leia o nome de uma pessoa e mostre uma mensagem de boas-vindas de acordo com o valor digitado.
nome = input("Qual é o seu nome? ")
print("Bem-vindo(a),", nome + "!")  # Bem-vindo(a), Caio!

# 2. Crie um script Python que leia o dia, o mês e o ano de nascimento de uma pessoa e mostre uma mensagem com a data formatada.
dia = input("Qual é o dia do seu nascimento? ")
mes = input("Qual é o mês do seu nascimento? ")
ano = input("Qual é o ano do seu nascimento? ")
print("Voce nasceu no dia", dia, "de", mes, "de", ano, ". Correto?")  # Voce nasceu no dia x de x de x. Correto?

# 3. Crie um script Python que leia dois números e tente mostar a soma entre eles.
numero1 = input("Digite o primeiro número: ")
numero2 = input("Digite o segundo número: ")
print(numero1 + numero2)  # Isso dará erro, pois os números estão em formato de string. Para corrigir, use int() ou float().
numero1 = int(numero1)  # Converte o primeiro número para inteiro
numero2 = int(numero2)  # Converte o segundo número para inteiro
print(numero1 + numero2)  # Agora a soma funcionará corretamente, mostrando o resultado como um número inteiro
