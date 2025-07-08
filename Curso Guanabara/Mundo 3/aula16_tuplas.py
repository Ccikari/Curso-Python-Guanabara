# Aula 16 - Tuplas

# A partir das tuplas é possível criar variáveis compostas (que guardam vários valores). Nesse caso, tuplas
    # Os elementos serão identificados por índices
        # As tuplas são imutáveis. Uma vez que definida, ela ficará daquela forma por todo o programa
            # () - Tuplas 
            # [] - Listas
            # {} = Dicionários

lanche = ("Hamburguer", "Suco", "Pizza", "Pudim") # funciona até sem parênteses, mas usar com
print(lanche)
print(lanche[1]) # vai mostrar Suco
print(lanche[1:3]) # Suco (elemento 1) e Pizza (elemento 2)
print(lanche[:2]) #do início até o elemento 2
# lanche[1] = "Refrigerante" - vai dar erro, não posso atribuir valores à tupla além da sua declaração

print(len(lanche)) # mostra quantos elementos há na tupla

for cont in range(0, len(lanche)):
    print(f"eu vou comer {lanche[cont]} na posição {cont}") # vai listar os elementos, posso usar para uma frase

for comida in lanche:
    print(f"Eu vou comer {comida}") # repete a frase para cada elementop
print("Comi demais")

for pos, comida in enumerate(lanche):
    print(f"Eu vou comer {comida} na posição {pos}") # todas as opções estão certas. Cada ocasião tornará uma melhor ou pior

print(sorted(lanche)) # Coloca em ordem

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = a + b
print(c) # vai colar as tuplas. (a + b é diferente de b + a)
print(c.count(5)) # Quantas vezes aparece o 5 dentro de c?
print(c.index(8)) # Em que posição está o 8?

pessoa = ("Caio", 20, "M", 85.00) # pode misturar os tipos
del(pessoa) # deleta da memória. Posso deletar a tupla inteira, não elementos específicos nela