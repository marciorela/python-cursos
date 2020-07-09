"""
Variáveis - Iniciar com letra, pode conter números, separar _, letras minúsculas
"""

nome = "Márcio Rela"
idade = 45
altura = 1.80
e_maior = idade > 18
peso = 101.4

imc = peso / altura ** 2

print(nome, 'tem', idade, 'anos de idade e seu imc é', imc)
print(f'{nome} tem {idade} anos de idade e seu imc é {imc:.2f}')
print('{0} tem {1} anos de idade e seu imc é {2}'.format(nome, idade, imc))
print('{n} tem {i} anos de idade e seu imc é {im:.2f}'.format(n=nome, i=idade, im=imc))
