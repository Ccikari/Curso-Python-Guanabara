# Aula 17 - Listas (Parte 1)

# () - Tuplas - Imutáveis
# [] - Listas - São mutáveis. Ou seja, podem ser modificadas. 

# Posso substituir elementos da lista, assim como adicionar elementos dentro da listas (pelo .insert(0, "")) ou no fim (pelo .append(" ")).

# Pode deletar elementos por (del xxxx[0]), (xxxx.pop(0)) ou (xxxx.remove(" "))
    # xxxx.pop() usado isoladamente, com os () vazios, elimina o último elemento

# e se tentar remover um elemento de que não existe? Vai dar erro na linguagem; é preciso verificar se o elemento está na linguagem antes
    # if "x" in xxxx:
        # xxxx.remove("x")

# Pode-se criar listas através de um range
valores = list(range(4,11))

valores = [8, 2, 5, 4, 9 ,3, 0] # crio uma lista fora de ordem
valores.sort() # ordena os valores
valores.sort(reverse=True) # ordena na ordem 
len(valores) # diz quantos valores há na lista

num = [2, 5, 9, 1]
num[2] = 3 # o 9 passa a valer 3
num.append(7) # adiciona o valor 7 à lista
num.insert(2, 0) # Na posição 2, inserir o valor 0.
num.pop() # Elimina o último valor
num.pop(2) # Elimina o segundo valor
num.remove(2) # Elimina a primeira ocorrência do valor que foi pedido. Se o valor não estiver na lista dá erro
if 4 in num:
    num.remove(4)
else:
    print("Não achei o número 4")
print(num)
print(f"Essa lista tem {len(num)} elementos")

valores = []
valores.append(5)
valores.append(9)
valores.append(4)

for v in valores:
    print(f"{v}...", end=" ")

valores = list()
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))

for c, v in enumerate(valores):
    print(f"Na posição {c} encontrei o valor {v}!")
print("Cheguei ao final da lista")

a = [2, 3, 4, 7]
b= a
b[2] = 8 # a partir do momento que igualo duas listas, qualquer modificação em uma delas muda na outra também.
print(a)
print(b)
b = a[:] # assim eu crio apenas uma cópia da outra lista e posso modificar sem afetar a outra
b[2] = 5
print(a)
print(b)