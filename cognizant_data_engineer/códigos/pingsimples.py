import os

print("#" * 60)
ip_ou_host = input("Digite o IP ou Host a ser verificado: ")
print("-" * 60)
os.system(f"ping -n 6 {ip_ou_host}")  # -n -> número de pacotes
print("-" * 60)
