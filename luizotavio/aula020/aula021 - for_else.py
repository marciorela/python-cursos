"""
For / Else
"""

lista = ['nome1', 'axis']

for item in lista:
    if (item.startswith('x')):
        print(f'{item} começa com x')
    else:
        print(f'{item} não começa com x')

for item in lista:
    if item.lower().startswith('x'):
        break
else:
    print(f'Não existe uma palavra que comece com x.')


