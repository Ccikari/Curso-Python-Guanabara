# Exercícios da Aula 7

# 5. Faça um programa que leia um número inteiro e mostre na tela o seu sucessor e seu antecessor
n1 = int(input("Digite um número:  "))
print("O sucessor do número {} é o número {} e o antecessor é o número {}".format(n1, n1 + 1, n1 - 1))
    # o professor fez duas variáveis, a = n1 - 1, s = n1 + 1. Isso é feito para guardar a variável, se ela for necessária depois.
    # "Analisando o valor {}, seu antecessor é {} e o seu sucessor {}."format...

# 6. Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n2 = int(input("Digite um número: "))
print("Você escolheu o número {}, seu dobro é {}, o triplo é {} e a raíz quadrada é {}.".format(n2, n2 * 2, n2 * 3, n2 ** (1/2)))
    # as variáveis seriam: d = n2 * 2, t = n2 * 3, r = n2 ** (1/2)
    # "o dobro de {} vale {},\n o triplo vale {},\n sua raíz quadrada é {}.".format...

# 7. Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input("Nota do Aluno: "))
nota2 = float(input("Nota do Aluno: "))
media = (nota1 + nota2) / 2
print("A média do aluno é {:.1f}".format(media))

# 8. Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
m = float(input("Digite a metragem: "))
cm = int(m * 100)
mm = int(m * 1000)
print("{} metros equivalem a {} centímetros, ou a {} milímetros".format(m, cm, mm))

# 9. Faça um programa que leia um número inteiro qualquer e mostre na tela a sua tabuada.
n3 = int(input("Digite um número para ver sua tabuada: "))
print("A tabuada de {} é:\n{};\n{};\n{};\n{};\n{};\n{};\n{};\n{};\n{};\n{}.".format(n3, n3 * 1, n3 * 2, n3 * 3, n3 * 4, n3 * 5, n3 * 6, n3 * 7, n3 * 8, n3 * 9, n3 * 10))
    #print("("-" * 12)\n{} x 1 = {}\n{} x 2 = {}\n{} x 3 = {}\n".format(n3,n3 * 1, n3, n3 * 2, n3, n3 * 3) e assim por diante
    # ou fazer um print para cada operação, para deixar organizado, usar print("{} x {:2} = {}".format())
        # faz isso ({:2}) para deixar todos com dois dígitos, já que na tabuada 10 desogarnizaria a tabuada
    # Dá pra ficar bem mais simples com estruturas de repetição, ainda aprenderei

# 10. Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar. (Considere U$1,00 = R$3,27)
carteira = float(input("Quanto você tem na carteira? "))
dolar = carteira / 3.27
print("É possível comprar U${:.2f} com R${}".format(dolar, carteira))

# 11. Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2m2>
largura = float(input("Largura da parede: "))
altura = float(input("Altura da parede: "))
area = largura * altura
tinta = area / 2
print("A área da parede é de {:.2f}m2, pintá-la exigirá {:.2f}l de tinta".format(area, tinta))

# 12. Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.
preco = float(input("Qual é o preço do produto? R$")) #opção 1
preco5= preco * (95/100) #posso fazer também: preco - preco - (preco * (5/100)); ou simplesmente preco * 0.95
print("Com o desconto, o produto passa a custar R${:.2f}".format(preco5))
desconto = preco * (5/100)
print("O produto tem desconto de R${:.2f}, custando R${:.2f}".format(desconto, preco - desconto))

# 13. Faça um algortimo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input("Digite o salário: R$"))
salarion = salario * 1.15 # posso utilizar as outras opções como utilizei no exercício anterior, apenas somando ao invés de subtrair
print("Após o aumento de 15%, o novo salário será {:.2f}.".format(salarion))
