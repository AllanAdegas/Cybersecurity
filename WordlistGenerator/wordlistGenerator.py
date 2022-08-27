import itertools

string = input("Entre com a string q deseja gerar a wordlist:\n")
resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))