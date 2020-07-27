"""
Listas
append, insert, pop, del, clear, extend, +
min, max
range
"""

# lista = [1, 2, 3, 4, "Nome", True, 10.5]

# lista = ['A', 'B', 'C', 'D', 'E']
# print(lista[0])
# print(lista[-1])
# print(lista)
# print(lista[0:3])
# print(lista[1:4])
# print(lista[:3])
# print(lista[2:])
# print(lista[::2])
# print(lista[::-1])
#
# lista[2] = 'Outra coisa'
# print(lista)

l1 = [1,2,3]
l2 = [4,5,6]
l3 = l1 + l2

l1.extend(l2)
l2.append(15)

l2.insert(0,3)

l2.pop()

print(l1)
print(l2)
print(l3)
print(max(l2))
print(min(l2))

l4 = list(range(1, 10))
print(l4)

for valor in l4:
    print(valor)

l5 = ['string', True, 10, -20.5]

for e in l5:
    print(f'O tipo de {e} é {type(e)}')
