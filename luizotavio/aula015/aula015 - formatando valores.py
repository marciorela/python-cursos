"""
Formatando valores com modificadores

:s - TExto (string)
:d - Inteiros (int)
:f - Número de ponto flutuante (float)
:.(NUMERO)f - Quantidade de casas decimais (float)
:(CARACTERE)(> ou < ou ^)(QUANTIDADE)(TIPO - s, d ou f)

> - Esquerda
< - Direita
^ - Centro
"""

num_1 = 10
num_2 = 3
divisao = num_1 / num_2

print(divisao)
print('{:.2f}'.format(divisao))
print(f"{divisao:.2f}")

nome = "Marcio Rela"
# nome_formatado = "{:@>50}".format(nome)
nome_formatado = "{n:@>50}".format(n=nome)
print(f"{nome:s}")
print(f"{nome_formatado}")

print(f"{num_1:0>10}")
print(f"{num_1:0<10}")
print(f"{num_1:0^10}")
