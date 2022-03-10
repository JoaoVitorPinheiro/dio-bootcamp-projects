import itertools

# Permutações e Combinações

word = input('Digite a sequência de caracteres: ')

n_iterations = len(word)
resultado = itertools.permutations(word, n_iterations)

for i in resultado:
    print(''.join(i))

print(f'Número de permutações: ', resultado)

# Number of items returned: n! / (n-r)!
