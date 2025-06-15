# Funções são blocos reutilizáveis de código que realizam uma tarefa específica.

def minha_funcao(valor1, valor2): # a função espera receber dois valores como parâmetros
    return valor1 + valor2# função de soma os dois valores e retorna o resultado

resposta = minha_funcao(10, 10)

print("resposta: ", resposta)

def minha_funcao(valor1, valor2):
    return valor1 + valor2

while True: 
    valor1 = int(input("Valor1:"))
    valor2 = int(input("Valor2:"))
    
    resposta = minha_funcao(10, 10)
    print("resposta: ", resposta)