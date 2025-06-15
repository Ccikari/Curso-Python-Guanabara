# Aula 10 - Condições (Parte 1)

# Numa condição, ou o bloco verdadeiro será exevautado, ou será o falso
# if carro.esquerda():
    # bloque True
# else:
    # bloco False

#Condição Simples
nome = str(input("Qual é seu nome? "))
if nome == "Caio": 
    print("Que nome lindo você tem!") # só vai aparecer se o nome for Caio; se não for, só não aparece e pula para o bom dia
print("Bom dia, {}!".format(nome))

# Condição Composta
tempo = int(input("Quantos anos tem seu carro?"))
if tempo <= 3:
    print("Carro novo")
else:
    print("Carro velho")
print("--FIM--")
# há também uma forma simplificada, mas não recomendaria
print("carro novo") if tempo <= 3 else "carro velho3"
print("--fim--")

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n = (n1 + n2) / 2
print("A sua média foi {:.1f}".format(n))
if n >= 6:
    print("Sua média foi boa. Parabéns!")
else:
    print("Sua média foi ruim. Estude mais!")

