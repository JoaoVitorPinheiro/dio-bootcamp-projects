import socket    
# chama a API Socket do SO
# responsável pelo relacionamento entre a placa de rede e o SO

import sys
# fornece acesso a algumas funções que tem interação com o interpretador 

def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print("A conexão falhou")
        print(f"Erro: f{e}")
        sys.exit()
    
    print("Socket criado com sucesso!")
    
    target_host = input("Digite o Host ou IP a ser conectado: ")
    target_port = input("Digite a porta a ser conectada: ")

    try:
        s.connect((target_host, int(target_port)))
        print(f"Cliente TCP conectado!\nHost: {target_host}, Porta: {target_port}")
        s.shutdown(2)
    except socket.error as e:
        print("A conexão falhou!\n Não foi possível conectar no Host: {target_host}, Porta: {target_port}")
        print(f"Erro: f{e}")
        sys.exit()

if __name__=='__main__':
    main()
