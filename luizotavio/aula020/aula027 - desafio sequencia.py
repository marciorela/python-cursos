"""
duas listas:
  uma crescente de 0-8
  outra decrescente de 10 a 2
"""

# minha solução
for var in range(0,9):
    print(var, 10-var)

# solução
for p, r in enumerate(range(10, 1, -1)):
    print(p, r)
