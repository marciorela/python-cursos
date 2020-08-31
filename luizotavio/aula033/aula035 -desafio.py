"""
1 - Crie uma função que recebe uma função2 como parâmetro e retorne o valor da função2 executada.
"""
def func1(funcao):
    return funcao()

def func2():
    return 10

print (func1(func2))

"""
2 -  Crie uma função1 que recebe uma função2 como parâmetro e retorne o valor fa função2 executada. Faça a função1 executar duas funções que recebam um número diferente de argumentos.
"""

def mestre(funcao, *args, **kwargs):
    return funcao(*args, **kwargs)

def fala_oi(nome):
    return f"Oi {nome}"

def saudacao(nome, saudacao):
    return f"{saudacao} {nome}"

executando = mestre(fala_oi, 'Joaquim')
print(executando)

executando = mestre(saudacao, 'Joaquim', saudacao = "Bom dia")
print(executando)
