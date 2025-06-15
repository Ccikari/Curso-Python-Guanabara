# codigo sem funcao
# Resposta: if opcao == 1 e elif opcao == 2 são praticamente a mesma coisa
    # bora criar uma função para unificar esse codigo e reutilizar no nosso loop

fluxo_caixa = []

print("___________")
print("@ Fluxo caixa")
print("___________")
print("1 -- Adicionar receita")
print("2 -- Adicionar despesa")
print("\n# Digite outro numero para encerra #\n")

def adicionar_transacao():
    nome = input("Nome: ")
    valor = float( input("Valor: ") )
    fluxo_caixa.append({
            "nome": nome,
            "valor": valor
        })
while True:

    opcao = int(input("Digite a opcao: ") )

    if opcao == 1:
        adicionar_transacao()
    elif opcao == 2:
        adicionar_transacao()
    else:
        break

# nota fiscal
total = 0
for fc in fluxo_caixa:
    print("nome: ", fc["nome"], ", valor: R$", fc ["valor"])
    total = total + fc["valor"]

print("Saldo atual: R$", total)