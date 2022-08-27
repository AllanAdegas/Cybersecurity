from base64 import decode
import hashlib
from passwordGenerator import generator

senha = generator()
resultado = hashlib.sha256(senha.encode())

print(f'Senha: {senha}')
print(f'Hash: {resultado.hexdigest()}')

