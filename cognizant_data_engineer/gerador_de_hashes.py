import hashlib

msg = input('Digite o texto para gerar o hash: ')

menu = int(input('''### MENU - ESCOLHA O TIPO DE HASH ###
                1) MD5
                2) SHA1
                3) SHA256
                4) SHA512
                Digite o número do hash a ser gerado: '''))

if menu == 1:
    resultado = hashlib.md5(msg.encode('utf-8'))
    c = 'MD5'
elif menu == 2:
    resultado = hashlib.sha1(msg.encode('utf-8'))
    c = 'SHA1'
elif menu == 3:
    resultado = hashlib.sha256(msg.encode('utf-8'))
    c = 'SHA256'
elif menu == 4:
    resultado = hashlib.sha512(msg.encode('utf-8'))
    c = 'SHA512'
else:
    print('Algo deu errado! 请再试一次')
    exit()
    
print(f'A hash {c} da string é :', resultado.hexdigest())
