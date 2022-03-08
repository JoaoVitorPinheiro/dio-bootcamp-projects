import os
import time
import csv

# Internet Control Message Protocol (ICMP)) uma rede de protocolo que é responsável
# por comunicar erros através dos meios de geração e envio de mensagens para o
# endereço IP de origem quando existem problemas de rede encontrados pelo sistema.

# Testando requisições ICMP com o ping
host_list = [
    "www.google.com.br",
    "127.0.0.1",
    "8.8.8.8",
    "www.github.com" # should time out
]

# no need for this, just practicing file manipulation
# could go straight from list of hosts
# create csv file from host_list
with open("hosts.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerows(host_list)

# open created file and ping hosts
with open("hosts.csv") as f:
    dump = f.read()
    dump = dump.splitlines()
    
    for ip in dump:
        ip = ip.replace(',', '')
        print(f'Verificando o ip: {ip}')
        print('-'*60)
        os.system(f"ping -n 4 {ip}")
        print('-'*60)
        time.sleep(5)
