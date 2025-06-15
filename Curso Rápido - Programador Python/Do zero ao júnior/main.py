nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
peso = float(input("Digite seu peso: "))

# input() - armazena entrada de dados do usuário, ou seja, o que ele digitar

print(nome)
print(idade)
print(peso)
print(type(idade))
print(type(peso))

# control s para salvar o arquivo
# control shift p para abrir a barrinha de comandos

# uma variável armazena dados, sejam eles textos; numeros interiso, negativos ou postivos, ou com casas decimais
    # string - str - texto, entre aspas simples ou duplas
    # inteiro - int - numeros inteiros, negativos ou positivos
    # float - numeros com casas decimais, negativos ou positivos
    # boolean - bool - verdadeiro ou falso, 1 ou 0
is_python = True
is_java = False

#exemplificando a variável booleana
ingressos = 50
compradores = 250
tem_ingressos_suficientes = ingressos >= compradores
print(tem_ingressos_suficientes)
