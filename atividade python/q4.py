login_padrao = 'admin'
senha_padrao = "123"

login = ' '
senha = ' '

login = input('login: ')
senha = input('senha: ')
if login == login_padrao and senha == senha_padrao:
    print(f'olá admin,seja bem-vindo')
else:
    print(f'login ou senha incorretos, tente novamente')