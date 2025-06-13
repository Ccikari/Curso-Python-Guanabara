# Exercício 14 - Conversor de Temperaturas

# 14. Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit
c = int(input("°C: "))
f = float((c * 9 / 5) + 32) # Pela regra de precedência, nem precisa de parênteses no meio da função
print("{}°C são {:.1f}°F".format(c, f))

# Exercício 15 - Aluguel de Carros

# 15. Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
    # Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado
km = float(input("Quanto Km foram rodados? "))
dia = int(input("Por quantos dias o carro foi alugado? "))
preco = float((km * 0.15) + (dia * 60))
print("O preço do aluguel é R${:.2f}".format(preco))
# é importante dividir os problemas em pequenas tarefas, para ir testando aos poucos.
    # imagina fazer tudo de uma vez; se der erro, onde está o problema?
        # é mais fácil de achar se resolver por etapas
