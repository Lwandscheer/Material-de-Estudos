lista = ['Matemática', 'História', 'Física', 'Português']
print('Física' in lista)
print('Química' in lista)


# ESTRUTURA DE REPETIÇÃO EM FOR:
# cria um loop em que será feito uma série de comandos para cada "dado" dentro da nossa lista.
for dados in lista:
    print(dados)
# A variável dados dentro da estrutura de repetição pode assumir literalmente qualquer valor, como x.

for index, dados in enumerate(lista, start=1):  # dentro da estrutura for podemos botar mais de uma variável.
    print(index, '-', dados)  # Devido ao argumento start = 1, a contagem começa a partir do 1.


# TRANSFORMANDO UMA LISTA EM STRING:
lista_string = ', '.join(lista)
print(lista_string)
print(type(lista_string))

nova_lista = lista_string.split(' - ')
print(nova_lista)