import projeto as fc


while True:
    print('''
1-Cadastrar usuário
2-Login
    ''')
    op = int(input('Opção: '))
    if op == 1:
        fc.add_user()
    elif op == 2:
        fc.login()
    else:
        print('Opnção inválida.')