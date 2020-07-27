"""
1 - Crie uma função que exibe uma saudação com os parâmetros saudacao e nome.
"""
def saudacao(saud, nome):
    print(f"{saud}, {nome}")

saudacao("Olá", "Joaquim")

"""
2 - Crie uma função que recebe 3 números como parâmetros e exiba a soma entre 
eles.
"""
def soma(n1, n2, n3):
    print(n1 + n2 + n3)

soma(10, 20, 30)

"""
3 - Crie uma função que receba 2 números. O primeiro é um valor e o segundo um
percentual (ex. 10%). Retorne (return) o valor do primeiro número somado
do aumento do percentual do mesmo.
"""
def percent(valor, porc):
    return valor * ((porc/100) + 1)

print(percent(100, 20))
print(percent(50, 10))

"""
4 - Fizz Buzz - Se o parâmetro da função for divisível por 3, retorne fizz,
se o parâmetro da função for divisível por 5, retorne buzz. Se o parâmetro da
função for divisível por 5 e por 3, retorne FizzBuzz, caso contrário, retorne o
número enviado.
"""
def fizzbuzz(n1):
    retorno = ""

    if n1 % 3 == 0:
        retorno += "Fizz"

    if n1 % 5 == 0:
        retorno += "Buzz"

    return n1 if retorno == "" else retorno

print(fizzbuzz(9))
print(fizzbuzz(5))
print(fizzbuzz(15))
print(fizzbuzz(14))
