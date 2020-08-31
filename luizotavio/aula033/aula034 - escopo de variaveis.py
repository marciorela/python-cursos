"""
Escopo de variáveis
"""

variavel = "valor"

def func1():
    print(variavel)

def func2():
    variavel = "Outro valor"
    print(variavel)

def func3():
    global variavel
    variavel = "Mais um valor"
    print(variavel)

func1()
print(variavel)

func2()
print(variavel)

func3()
print(variavel)
