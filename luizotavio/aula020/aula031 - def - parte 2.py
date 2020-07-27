"""
Funções def (retorno)
"""

def func(var):
    print(var)

def divisao(n1, n2):
    if n2 > 0:
        return n1 / n2

def ttt():
    return ("um", "nome")

def dumb():
    return func

divide = divisao(8, 2)
if divide:
    print(divide)

var = dumb()("Impressão")

# ponteiro para função
var = dumb()
print(id(var), id(func))

# tuplas
var = ttt()
print(var[0])
