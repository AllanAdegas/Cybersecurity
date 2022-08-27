import itertools
import string
import os
import sys
from passwordGenerator import generator

senha = generator()

print("Essa é a sua senha: " + senha)

string = itertools.permutations(string.ascii_letters + string.digits + "!@#$%¨&*()'-=_+?<>,.;/çÇ", 8)

for i in string:
    # print(''.join(i))
    s = ''.join(i)
    if senha == s:
        print('\n' + s + ' senha quebrada com sucesso')
        input("Pressione ENTER para continuar")
        break

