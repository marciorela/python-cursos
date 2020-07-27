"""

"""

frase = 'o rato roeu a roupa do rei de roma'

entrada = input("Qual a letra deseja deixar maiúscula? ")
resultado = ""

contador = 0
while contador < len(frase):
    letra = frase[contador]

    if letra == entrada:
        resultado += entrada.upper()
    else:
        resultado += letra

    contador += 1

print(resultado)
