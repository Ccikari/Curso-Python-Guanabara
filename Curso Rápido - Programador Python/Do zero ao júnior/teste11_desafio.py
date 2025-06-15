# codigo sem funcao
# Desafio: o que poderia ser reutilizado?

fluxo_caixa = []

print("___________")
print("@ Fluxo caixa")
print("___________")
print("1 -- Adicionar receita")
print("2 -- Adicionar despesa")
print("\n# Digite outro numero para encerra #\n")

while True:

    opcao = int(input("Digite a opcao: ") )

    if opcao == 1:
        nome = input("Nome: ")
        valor = float( input("Valor: ") )
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
    elif opcao == 2:
        nome = input("Nome: ")
        valor = float(input("Valor: ") )
        fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
    else:
        break

# nota fiscal
total = 0
for fc in fluxo_caixa:
    print("nome: ", fc["nomes"], ", valor: R$", fc ["valor"])
    total = fc["valor"]

print("Saldo atual: R$", total)
