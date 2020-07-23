"""
while / else
contadores / acumuladores

* não executa o else quando o executar o break dentro do laço


"""

contador = 1
acumulador = 1

while contador <= 100:
    print(contador, acumulador)

    acumulador = acumulador + contador
    contador += 1
else:
    print('Cheguei no else')

