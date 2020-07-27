"""
Split - Dividir uma string # str
Join - Juntar uma lista # str
Enumerate - Enumerar elementos da lista # iteráveis
"""

string = "O Brasil é o país do futebol, o Brasil é penta."

lista_1 = string.split(' ')
lista_2 = string.split(',')

print(lista_1)
print(lista_2)

palavra = ''
contagem = 0
for valor in lista_1:
    # print(f'A palavra {valor} apareceu {lista_1.count(valor)} vezes na frase')
    qtd_vezes = lista_1.count(valor)

    if qtd_vezes > contagem:
        contagem = qtd_vezes
        palavra = valor

print(f'A palavra que apareceu mais vezes foi {palavra} ({contagem}x).')

for valor in lista_2:
    print(valor.strip().capitalize())

string = " ".join(lista_1)
print(string)

for v1, v2 in enumerate(lista_1):
    print(v1, v2)

lista = [
    [1, 2],
    [3, 4],
    [5, 6]
]
for v in lista:
    print(v[0], v[1])

# desempacotamento de lista
lista = ["Luiz", "João", "Maria"]

n1, n2, n3 = lista
print(n2)
