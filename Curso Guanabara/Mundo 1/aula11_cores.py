# Aula 11 - Cores no Terminal

# \033[style; text; back m
    # style - estilo da fonte (negrito, sublinhada, normal)
        # 0 - sem estilo
        # 1 - em negrito
        # 4 - sublinhado
        # 7 - inverte as conigs, o que tá no fundo vai pra letra e vice versa
    # text - cor do texto
        # 30 - branco
        # 31 - vermelho
        # 32 - verde
        # 33 - amarelo
        # 34 - azul
        # 35 - magenta
        # 36 - ciano
        # 37 - cinza (padrão)
        # biblioteca e outras funcionalidades expandem as opções
    # back - cor do fundo
        # mesma ordem da cor do texto, mas de 40 à 47


print("\033[0;30;41mteste\033[m")
print("\033[4;33;44mteste\033[m")
print("\033[1;35;43mteste\033[m")
print("\033[30;42mteste\033[m")
print("\033[mteste\033[m")
print("\033[7;30mteste\033[m")
a = 3
b = 5
print("Os valores são \033[32m{}\033[m e \033[31m{}\033[m!!".format(a, b))