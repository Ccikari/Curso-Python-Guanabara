# for - loop que percorre sequências, repetindo ações para cada elemento
# while - loop que executa ações enquanto uma condição for verdadeira

for x in range (10):
    print(x)

# x é uma variavel temporaria que será modificada de acordo com a execução do loop; pode ser usada apenas dentro do bloco de repetição
    # na primeira execução, o x equivale a 0; na próxima, a 1; e assim por diante; nesse caso, até 9; pois occoreu 10 repetições a partir de 0

notas = []

for x in range (5):
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

print( "quantidade notas", len(notas) )

for n in notas:
    codigo_aluno = n[0]
    nota = n[1]
    print("O aluno, com RM:", codigo_aluno, "tirou a nota:", nota)

# é possível fazer a mesma coisa com o while

notas = []

contador = 1

while contador <= 5:
    codigo_aluno = input("RM: ")
    nota = float(input("Nota: "))
    resultado = [codigo_aluno, nota]
    notas.append(resultado)

    # alterantiva: contador += 1
    contador = contador + 1

print( "quantidade de notas", len(notas) )