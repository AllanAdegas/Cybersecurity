import ipaddress

ip = '192.168.0.1'
rede = '192.168.0.0/27'

endereco = ipaddress.ip_address(ip)
net = ipaddress.ip_network(rede, strict=False)

print(endereco)
print(net)
print('-'*30)

for ip in net:
    print(ip)