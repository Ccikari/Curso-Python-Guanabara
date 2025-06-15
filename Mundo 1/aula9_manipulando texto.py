# Aula 9 - Manipulando Texto/Cadeia de Texto (string)

frase = "Curso em Vídeo Python"
    # o python coloca essa frase na memória do computador, criando miniespaços dentro da memória e em cada miniespaço haverá um caractere. Nessa frase, vai de 0 a 20.

# Fatiamento de string
print(frase[9])
print(frase[9:14]) #9 a 14 pega de as letras de 9 a 13, pois o último valor não entra na contagem
print(frase[9:21]) #se fosse 9:20 cortaria o python
print(frase[9:21:2]) #vai de 9 a 21 pulando de dois em dois
print(frase[:5]) # quando se omite o início, ele começa do 0
print(frase[15:]) # aqui o inverso, pois indiquei o início, mas não o fim. Logo, irá até o final da string
print(frase[9::3]) # começa do 9, omite o fim, e pula de três em três

# Análise de string
len(frase) # len siginifica comprimento. Qual o comprimento da frase? Nesse caso, seriam 21 caracteres, do 0 ao 20
frase.count("o") # estou pedindo para contar quantas vezes a letra "o" aparece na string
frase.count("o",0,13) # contagem com fatiamento, delimitando o início e o fim da frase
frase.find("deo") # vai dizer quantas vezes ele encontrou o "deo" na frase. Ele vai dizer em que momento começou o "deo".
frase.find("Android") # se ele não achar nada igual, vai aparecer "-1" como resultado
"curso" in frase # existe "curso" em frase? True ou False

# Transformação de string
frase.replace("Python", "Android") # onde tiver Python, ele vai substituir por Android
frase.upper() # deixa a frase em maiúscula, o que já for ele mantém, o que não for fica
frase.lower() # o inverso do upper
frase.capitalize # joga todos os caracteres para minúsculos e dps deixa só a primeira letra da frase como maiúscula
frase.title() # deixa apenas a primeira letra de cada palavra como maiúsucla

frase = "   Aprenda Python   "

frase.strip() # remove os espaços inúteis no texto, os iniciais e finais (extremidades), deixando apenas aqueles entre as palavras
frase.rstrip() # a variação "r" faz com que remova apenas os espaços a direita
frase.lstrip() # o inverso do r, remove os da esquerda

# Divisão de string
frase = "Curso em Vídeo Python"
frase.split() # ocorre uma divisão na string dentre os seus espaços, refazendo cada índice em uma lista
    # Ou seja, "Curso em Vídeo Python" fica "Curso" "em" "Vídeo" "Python"
    # tem mais funcionalidades, é bom estudar mais depois. Já que se pode reconfigurar sua função

# Junção de string
"-".join(frase) # Junta todos os elementos de frase, formando uma string única com o que está entre parêenteses
    # "Curso" "em" "Vídeo" "Python" ficaria "Curso-em-Vídeo-Python"

# É possível unir as funções
print(frase.upper().count("o"))

# Se quiser escrever um texto longo na texto longo na tela, que use mais de uma linha, é preciso usar aspas 3 vezes para deixar tudo no mesmo print
print("""oioioioioioioioioioioioioioioioioioioioioioioioioioiiii
ioioioooooooooooooooooooooooooooooooooooooooooooooooooooooiiiiii
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooiiiii
oooooooooooooooooooooooooooooooooooooooooooooooooooooooiioioioio
iooooooooooooooodasjdaskkkkkkkkkkkkkkkkkkkoooooooooooooooooooooo
oooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooooi""") # se usasse só uma aspas ele não reconheceria

# Testar todas as funcionalidades depois para ir entendendo cada funçao
