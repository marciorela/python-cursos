exercicio = 3

"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número inteiro,
informe que não é um número inteiro.
"""
if exercicio == 1:
    num1 = input("Digite um número: ")

    if not num1.isdigit():
        print(f"{num1} não é um número inteiro.")

    else:
        num1 = int(num1)
        if num1 % 2 == 0:
            print(f"O número {num1} é par.")
        else:
            print(f"O número {num1} é ímpar.")

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário
descrito, exiba a saudação apropriada. Ex:
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23
"""
if exercicio == 2:
    hora = input("Que horas são? ")

    try:
        hora = int(hora)

        if hora < 0 or hora > 23:
            print("Hora deve estar entre 0 e 23")

        elif hora >= 0 and hora <= 11:
            print("Bom dia!")

        elif hora >= 12 and hora <= 17:
            print("Boa tarde!")

        else:
            print("Boa noite!")

    except:
        print(f"{hora} não é um número inteiro.")

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grannde".
"""
if exercicio == 3:
    nome = input("Digite seu nome: ")

    if len(nome) <= 4:
        print("Seu nome é curto!")

    elif len(nome) <= 6:
        print("Seu nome é normal")

    else:
        print("Seu nome é muito grande!")
