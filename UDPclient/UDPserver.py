from socket import socket


import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

print("Socket Criado com sucesso")

host = 'localhost'
port = 5432

s.bind((host,port))#liga client e servidor através do host e da porta
mensagem = "\nServidor: Teste 2"

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print("Servidor enviando mensagem ...")
        s.sendto(dados + (mensagem.encode()), end)