import random
import string

# Gerador de Senhas
tamanho = 16

chars = string.ascii_letters + string.digits + 'ç#%$&()-=+?'
rnd = random.SystemRandom()   # os.urandom

print(''.join(rnd.choice(chars) for i in range(tamanho)))
