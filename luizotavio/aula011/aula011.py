"""
len(string)
"""

usuario = input("Digite o nome de usuário: ")
qtd_caracteres = len(usuario)

print(usuario, qtd_caracteres, type(usuario))
if qtd_caracteres < 6:
    print("Você precisa digitar pelo menos 6 caracteres")
else:
    print("Você foi cadastrado no sistema")
