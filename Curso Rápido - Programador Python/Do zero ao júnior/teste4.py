salario = float(input("Informe o salário: "))

if salario <= 3000:
    print("programador júnior")
elif salario > 3000 and salario <= 6000:
    print("programador pleno")
elif salario > 6000 and salario <= 15000:
    print("programador sênior")
else:
    print("gerente de projetos")

# and - e; ambos os lados devem ser verdadeiros - coloca mais uma condição no if
# or - ou; pelo menos um dos lados deve ser verdadeiro

# > - maior que
# < - menor que
# >= - maior ou igual a
# <= - menor ou igual a
# == - igual a
# != - diferente de
