import hashlib

# Cria arquivo e compara as Hashes
text_1 = input('Texto do arquivo 1: ')
text_2 = input('Texto do arquivo 2: ')

file_1 = "arquivo1.txt"
file_2 = "arquivo2.txt"

with open(file_1, "w", newline='') as f:
    f.write(text_1)

with open(file_2, "w", newline='') as f:
    f.write(text_2)

hash1 = hashlib.new('ripemd160')
hash1.update(open(file_1, 'rb').read())

hash2 = hashlib.new('ripemd160')
hash2.update(open(file_2, 'rb').read())

if hash1.digest() != hash2.digest():
    print(f"O arquivo {file_1} é diferente do arquivo {file_2}")
else:
    print(f"O arquivo {file_1} é igual do arquivo {file_2}")

print(f"O hash do arquivo {file_1} é:", hash1.hexdigest())
print(f"O hash do arquivo {file_2} é:", hash2.hexdigest())
