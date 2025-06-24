# Aula 15 - Interrompendo Repetições While

# while True: # faz ficar num loop eterno

n = s = 0
while True:
    n = int(input("Digite um número: "))
    if n == 999:
        break # Se digitar 999, interrompe o programa. Inclusive evita a gambiarra que eu fiz no desafio 064 de colocar - 999
    s += n
print("A soma vale {}".format(s))

# comando f strings - simplificam o .format()
print(f"A soma vale {s}")

nome = "José"
idade = 33
salario = 987.30
print(f"O {nome:^20} tem {idade} anos e ganha R${salario:.2f}")
print(f"O {nome:20} tem {idade} anos e ganha R${salario:.2f}")
print(f"O {nome:-<20} tem {idade} anos e ganha R${salario:.2f}")
print(f"O {nome:->20} tem {idade} anos e ganha R${salario:.2f}")
print(f"O {nome:-^20} tem {idade} anos e ganha R${salario:.2f}")