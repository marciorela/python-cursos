"""
funções
"""

def func(*args, **kwargs):
    print(args)
    print(kwargs['nome'], kwargs['sobrenome'])

    idade = kwargs.get('idade')
    if idade is not None:
        print(idade)
    else:
        print("Idade não existe")

lista1 = [1, 2, 3, 4, 5]
lista2 = [10, 20, 30, 40, 50]
func(*lista1, *lista2, nome="joaquim", sobrenome="miranda")
