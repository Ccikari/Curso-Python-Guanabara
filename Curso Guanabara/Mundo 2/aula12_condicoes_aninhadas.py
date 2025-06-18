# Aula 12 - Condições Aninhadas

# Aninhar é colocar coisas dentro de outras, encaixar
    # colocar estruturas condicionais dentro de outras
        # if - se
        # elif - senão, se
        # else - senão

nome = str(input("Qual é o seu nome? "))
if nome == "Caio":
    print("Que nome bonito!")
elif nome == "Rebeca" or nome == "Edcarlos" or nome == "Solange":
    print("Seu nome é familiar.")
elif nome in "Ana Cláudia Jéssica Juliana":
    print("Belo nome feminino.")
else:
    print("Seu nome é bem normal.")
print("Tenha um bom dia, {}".format(nome))
