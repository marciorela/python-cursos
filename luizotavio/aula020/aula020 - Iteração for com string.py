"""
For in
Iteração de strings com For
continue e break
Função range(start=0, stop, step=1)
"""

texto = 'Python'
for letra in texto:
    print(letra)

for n in range(5, 11, 2):
    print(n)

for n in range(100):
    if n % 8 == 0:
        print(n)
