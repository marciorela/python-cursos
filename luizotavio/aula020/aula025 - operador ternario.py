"""
operador ternário
"""

logged_user = True
msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'
print(msg)

idade = 18
msg = 'Pode acessar' if idade >= 18 else 'Não pode acessar'
print(msg)
