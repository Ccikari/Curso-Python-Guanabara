# Aula 14 - Estrutura de Repetição While

for c in range(1,10): 
    print(c)
print("FIM")

c = 1
while c < 10: # faz a mesma coisa do for, o bom do while é que vc realiza programas sem limite.
    print(c)        # no for, é preciso determinar um limite; no while, não, realiza-se a ação até chegar no determinado
    c = c + 1
print("FIM")

n = 1
while n != 0: # enquanto n for diferente de 0, fica repetindo
    n = int(input("Digite um valor: "))
print("FIM")

r = "S"
while r == "S":
    n = int(input("Digite um valor: "))
    r = str(input("Quer continuar? [S/N] ")).upper()
print("FIM")

n = 1
par = impar = 0
while n != 0:
    n = int(input("Digite um valor: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar += 1
print("Você digitou {} números pares e {} número ímpares!".format(par, impar))