from email import message
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print('Cliente socket cirado com sucesso!')

host = 'localhost'
porta = 5433
mensagem = 'Teste 1'

try:
    print('Cliente: ' + mensagem)
    s.sendto(mensagem.encode(),(host, 5432))
    
    dados, servidor = s.recvfrom(4096)
    dados = dados.decode()
    print("Cliente: " + dados)
finally:
    print('Cliente: Fechando a conexão')
    s.close()