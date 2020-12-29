# CRIANDO LISTA
lista_vazia = []  # Cria uma lista vazia.
lista = ['Matemática', 'Português', 'Química', 'Geografia']

print(lista)  # Mostra a lista pura.
print(len(lista))  # Mostra a quantidade de dados presentes na lista.
print(lista[0])  # Mostra o dado selecionado pelo valor (index) nos colchetes (de 0 a 3)
# Usar um index que não seja um existente gerará um erro.


# INDEX NEGATIVO:
if lista[3] == lista[-1]:
    print('São o mesmo dado...')


# SELEÇÃO PRECISA DE TERMOS:
print(lista[0:2])  # O o primeiro termo da index é incluído na seleção, já o segundo não.
print(lista[2:])  # A partir do terceiro dado (Contido), mostrar até o final.
print(lista[:3])  # Delimita apenas o final da seleção, que não é incluído.


# MÉTODOS DE FORMATAÇÃO DE UMA LISTA:
# Adição
lista.append('Física')
print(lista)

lista.insert(0, 'Biologia')  # O método insert requer dois argumentos: (posição e valor)
print(lista)

lista2 = ['Educação Física', 'Artes']
lista.insert(0, lista2)
print(lista)
print(lista[0])  # Aqui a lista2 que foi inserida dentro da lista principal se torna um único dado.

lista.extend(lista2)  # Adiciona cada dado da lista2 como dados separados na lista principal.
print(lista)


# Remoção
lista.remove(lista2)
print(lista)

dado_retirado = lista.pop()  # Remove o último dado da lista e retorna o termo excluído.
print(lista)
print(dado_retirado)


# INVERTENDO UMA LISTA:
lista.reverse()  # Inverte a ordem de precedência de uma lista.
print(lista)
# Pode-se usar também o argumento reverse=True dentro de um método list


# ORDENAR UMA LISTA:
lista.sort()  # Ordena a lista em ordem crescente de letras.
print(lista)

lista_numerica = [123, 43, 12, 53, 23, 44]
lista_numerica.sort()
print(lista_numerica)

lista_numerica.sort(reverse=True)  # Aqui a lista continuará ordenada, porém invertida
print(lista_numerica)

lista3 = ['leonardo', 'wandscheer', 'oliveira']
sorted(lista3)
print(lista3)

lista_ordenada = sorted(lista3)  # A função sorted cria uma variação da lista, so que ordenada.
print(lista_ordenada)  # A nova lista feita na função sorted necessita de uma variável para transcreve-lá


# RETOMANDO DETERMINADOS VALORES EM UMA LISTA QUANTIFICADA:
print(min(lista_numerica))  # Procura o menor valor dentro da lista.
print(max(lista_numerica))  # Procura o maior valor dentro da lista.
print(sum(lista_numerica))  # Soma os valores dentro da lista.
