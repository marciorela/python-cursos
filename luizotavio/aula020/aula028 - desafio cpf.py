cpf = "168995350"
cpf = "177875028"

# PRIMEIRO DÍGITO
soma = 0
for i, r in enumerate(range(10, 1, -1)):
    soma += (int(cpf[i]) * r)

dig_1 = 11 - (soma % 11)
dig_1 = dig_1 if dig_1 < 10 else 0

# SEGUNDO DÍGITO
soma = 0
for i, r in enumerate(range(11, 1, -1)):
    soma += (int(cpf[i]) * r)

dig_2 = 11 - (soma % 11)

print(dig_1, dig_2)
