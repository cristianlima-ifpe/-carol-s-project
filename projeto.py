import os
import shutil
users = {'phablo': ['123'], 'cristian': ['123']}


def add_user():
    user = input('usuário: ')
    if user not in users:
        password = input('senha: ')
        users[user] = [password]
        os.mkdir(f'C:\\Users\CTRC2-M\Documents\server\\{user}')
    else:
        print('Nome de usuário indisponível.')


def login():
    user = input('login: ')
    password = input('senha: ')
    if user in users and password == users[user][0]:
        print('Usuário logado com sucesso.')
        print('''
1-Upload
2-Download (os arquivos serão listados.)
        ''')
        op = int(input('Opção desejada:'))
        if op == 1:
            source = input('Nome do arquivo (caminho completo): ')
            destination = (f'C:\\Users\CTRC2-M\Documents\server\\{user}')
            shutil.copy(source, destination)
        elif op == 2:
            file_list = os.listdir(f'C:\\Users\CTRC2-M\Documents\server\\{user}')
            for i in file_list:
                print(i)
            file_name = input('Nome do arquivo: ')
            source = (f'C:\\Users\CTRC2-M\Documents\server\\{user}\\{file_name}')
            destination = input('Destino (caminho completo): ')
            shutil.copy(source, destination)
    else:
        print('Usuário ou senha inexistente. Tente novamente.')
    

while True:
    print('''
1-Cadastrar usuário
2-Login
    ''')
    op = int(input('opção: '))
    if op == 1:
        add_user()
    elif op == 2:
        login()
    else:
        print('Opção inválida.')
