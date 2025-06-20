#Aula 13 - Estrutura de Repetição For

# for c in range( , ) 
    # if : # é possível ter uma estrutura condicional dentro da de repetição 

for c in range(0,6): # de 0 a 6 vai seis vezes 
    print("Oi") # oi 6x
print("FIM")

for c in range (0,6): 
    print(c) # vai contar de 0 a 5
print("FIM")

for c in range (1, 7):
    print(c) # vai contar de 1 a 6
print("FIM")

for c in range(6, 0, -1): 
    print(c) # vai contar de 5 a 1
print("FIM")

for c in range (0, 7, 2):
    print(c) # vai contar de 0 a 6, pulando de 2 em 2
print("FIM")

n = int(input("Digite um número: "))
for c in range(0, n + 1):
    print(c)
print("FIM")

i = int(input("Início: "))
f = int(input("Fim: "))
p = int(input("Passo: ")) # pulando de p em p
for c in range(i, f + 1, p):
    print(c)
print("FIM")

s= 0 # tem que criar a variável que armazenará valor antes
for c in range(0, 3):
    n = int(input("Digite um valor: "))
    s += n # += é um somatório
print("O somatório de todos os valores foi {}".format(s))