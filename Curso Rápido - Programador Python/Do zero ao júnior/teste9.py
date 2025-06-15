# criando um chat de mensagens

import os

# import - permite importar outros scripts; receber outros dados
    # os - usada para interagir com o sistema operacional
mensagens = []

nome = input("Nome: ")

while True:

    #limpando terminal - "cls" para Windows, "clear" para Linux/Mac
    os.system("cls")
 
    if len(mensagens) > 0: # len retorna o tamanho da lista; entao, se a lista for maior que 0
        for m in mensagens: #percorremos a lista de mensagens
            print(m["nome"], "-", m["texto"]) # fazemos um print do nome e do texto de cada mensagem
    # estamos acessando a chave dentro de um loop sem ter ainda adicionado dados na lista
    # por isso, fazemos a verificação na linha 16, só iremos exibir infos da lista se tiver pelo menos um item cadastrado
    print("___________________") #separar a lista de mensagens que será exibida do imput

    # obtendo texto
    texto = input("mensagem: ")
    if texto == "fim": # se o usuario digitar "fim", o programa encerra
        break

    # adicinando mensagem na lista
    mensagens.append({
        "nome": nome,  # adicionando o nome do usuario
        "texto": texto  # adicionando o texto da mensagem  
    })