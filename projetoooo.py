import os
import shutil
from shutil import make_archive
import smtplib
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email import encoders


users = {'phablo': ['123'], 'cristian': ['123']}

def add_user():
    user = input('usu�rio: ')
    if user not in users:
        password = input('senha: ')
        users[user] = [password]
        os.mkdir(f'C:\\Users\CTRC2-M\Documents\server\\{user}')
    else:
        print('Nome de usu�rio indispon�vel.')


def login():
    user = input('login: ')
    password = input('senha: ')
    if user in users and password == users[user][0]:
        print('Usu�rio logado com sucesso.')
        print('''
1-Upload
2-Download
3-Listar arquivos da pasta
4-Apagar aquivo da pasta
5-Zipar e enviar por e-mail
        ''')
        op = int(input('Op��o desejada:'))
        if op == 1:
            source = input('Nome do arquivo (caminho completo): ')
            destination = (f'C:\\Users\CTRC2-M\Documents\server\\{user}')
            shutil.copy(source, destination)
        elif op == 2:
            file_name = input('Nome do arquivo: ')
            source = (f'C:\\Users\CTRC2-M\Documents\server\\{user}\\{file_name}')
            destination = input('Destino (caminho completo): ')
            shutil.copy(source, destination)
        elif op == 3:
            file_list = os.listdir(f'C:\\Users\CTRC2-M\Documents\server\\{user}')
            for i in file_list:
                print(i)
        elif op == 4:
            path = (f'C:\\Users\CTRC2-M\Documents\server\\{user}')
            dir = os.listdir(path)
            for i in dir:
                print(i)
            arq = input('Nome do arquivo e extens�o: ')
            if arq in dir:
                os.remove(path + "\\" + arq)
        elif op == 5:
            pasta = (f'C:\\Users\CTRC2-M\Documents\server\\{user}')
            destino = (f'C:\\Users\CTRC2-M\Documents\server\\{user}')
            make_archive(pasta, 'zip', destino)
            email= 'lip.pratica'
            senha= 'L#P12345'

            servidor=smtplib.SMTP('smtp.gmail.com', 587)
            servidor.ehlo()
            servidor.starttls()
            servidor.login(email,senha)
            destinatario= input('E-mail de destino:')
            subject= input('Assunto: ')
            body = "Segue seus arquivos zipados.\nRenomear o aquivo para .zip "

            msg = MIMEMultipart()
            msg['From'] = '� noix pirraia'
            msg['To'] = destinatario
            msg['Subject'] = subject
            msgText = MIMEText(body)
            msg.attach(msgText)

            nomedoarquivo=(pasta+'.zip')
            with open(nomedoarquivo, 'rb') as f:
                mime = MIMEBase('application', 'zip',)
                mime.set_payload(f.read())

            encoders.encode_base64(mime)
            mime.add_header('Content-Disposition', 'attachment', filename=(nomedoarquivo+'2'))
            msg.attach(mime)
            servidor.sendmail(email, destinatario, msg.as_string())

            servidor.quit()

    else:
        print('Usu�rio ou senha inexistente. Tente novamente.')
    

while True:
    print('''
1-Cadastrar usu�rio
2-Login
    ''')
    op = int(input('op��o: '))
    if op == 1:
        add_user()
    elif op == 2:
        login()
    else:
        print('Op��o inv�lida.')
