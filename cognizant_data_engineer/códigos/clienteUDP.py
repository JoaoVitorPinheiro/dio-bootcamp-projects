import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Cliente Socket criado com sucesso!")
host = 'localhost'
port = 5433
message = "你好！"

try:
    print(f"Cliente: {message}")
    s.sendto(message.encode(), (host, 5432))
    
    data, server = s.recvfrom(4096) #bytes
    data = data.decode()
    print(f"Cliente: {data}")
    
finally:
    print("Cliente: Fechando a conexão...")
    s.close()
