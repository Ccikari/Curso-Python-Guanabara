# Exercícios da Aula 8 

# 16. Crie um programa que leia um número real qualquer pelo teclado e mostre sua porção inteira
from math import trunc
num = float(input("Digite um número real: "))
print(trunc(num))
print(int(num)) # nem precisa importar a biblioteca

# 17. Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente de um triângulo retângulo e mostre o comprimento da hipotenusa
    # hipotenusa^2 = a soma dos catetos^2, mas tem um módulo que ajuda
cat_op = float(input("Comprimento do cateto oposto: "))
cat_ad = float(input("Comprimento do cateto adjacente: "))
hip = ((cat_op**2) + (cat_ad**2)) ** (1/2)
print("O comprimento da hipotenusa é {:.2f}".format(hip))
from math import hypot
    # forma muito mais fácil
hip = hypot(cat_op, cat_ad)
print("O comprimento da hipotenusa é {:.2f}".format(hip))

# 18. Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo
from math import sin, cos, tan, radians # só funciona se for em radianos
ang = float(input("Ângulo qualquer: "))
sen = sin(radians(ang))
coss = cos(radians(ang))
tang = tan(radians(ang))
print("O ângulo de {} tem como seno {:.2f}, cosseno {:.2f} e tangente {:.2f}".format(ang, sen, coss, tang))

# 19. Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele, lendo o nome deles e escrevendo o nome do escolhido.
import random
al1 = str(input("Primeiro aluno: "))
al2 = str(input("Segundo aluno: "))
al3 = str(input("Terceiro aluno: "))
al4 = str(input("Quarto aluno: "))
lista = [al1, al2, al3, al4] # Listas ficam entre colchetes
escolhido = random.choice(lista)
print("O aluno escolhido foi {}".format(escolhido))

# 20. O mesmo professor quer sortear a ordem de apresentação dos alunos. Faça um programa que leia o nomes dos quatro alunos e mostre a ordem sorteada.
al1 = str(input("Primeiro aluno: "))
al2 = str(input("Segundo aluno: "))
al3 = str(input("Terceiro aluno: "))
al4 = str(input("Quarto aluno: "))
lista = [al1, al2, al3, al4]
random.shuffle(lista)
print("A ordem de apresentação será {}".format(lista))

# 21. Faça um programa em Python que abra e reproduza o áudio de um arquivo mp3
    # Para a forma que ele ensinou, é preciso ter a música na pasta e importar o pygame