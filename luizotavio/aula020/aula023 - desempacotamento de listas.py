"""
Desempacotamento de listas
"""
lista = ["Luiz", "João", "Maria", 1, 2, 3, 4, 5, 6]

n1, n2, *outra_lista, ultimo_da_lista = lista

print(n2, ultimo_da_lista, outra_lista)
