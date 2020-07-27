"""
Funções def
"""

def saudacao(msg="Olá", nome="usuário"):
    return f"{msg}, {nome}"

print(saudacao("Olá", "Joaquim"))
print(saudacao("Oi", "Maria"))
print(saudacao(nome="Zezinho"))

