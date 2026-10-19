def sistema_login():
    print('Bem-vindo ao seu cadastro!!\n')

    user_cadastrado = input('Crie o seu usuário: ')
    password_cadastrada = input('Crie a sua senha: ')

    if user_cadastrado == '' or password_cadastrada == '':
        print('\nErro: Usuário ou senha não podem ser vazios. Encerrando.')
        return

    print('\nUsuário cadastrado com sucesso! Faça login.')
    print('-' * 30)

    print('ÁREA DE LOGIN')

    for tentativa in range(3):
        user_login = input('Digite seu usuário para logar: ')
        password_login = input('Digite sua senha para logar: ')

        if user_login == user_cadastrado and password_login == password_cadastrada:
            print('\nLogin realizado com sucesso! Seja bem-vindo,', user_cadastrado, '.')
            exibir_menu()
            return
        else:
            print('\nUsuário ou senha incorretos.')
            print('Tentativa', tentativa + 1, 'de 3.\n')

    print('Número máximo de tentativas atingido. Acesso negado.')


def exibir_menu():
    print('\n' + '=' * 20 + ' MENU ' + '=' * 20)
    print('1. Ver Perfil')
    print('2. Configurações')
    print('3. Sair')
    print('=' * 46)

    opcao = input('Escolha uma opção: ')
    print('\nVocê escolheu a opção', opcao, '.')


sistema_login()