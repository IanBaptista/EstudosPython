# Parametrização da função
def loginUsuario(perfil):
    # passando pra Lower case
    if perfil.lower() == 'admin':
        print('Bem-vindo, Administrador')
    else:
        print('Bem-vindo, Usuário')

loginUsuario('Admin')
loginUsuario('Jãumzim23')  # esse eu botei pra ver se ia sair como Usuário mesmo