from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    while trajeto <= 100:
        print("Piloto {} Km: {}\n".format(piloto, trajeto))
        trajeto+=velocidade
        time.sleep(0.5)

     
t_carro1 = Thread(target=carro, args=[1, 'Jeferson'])
t_carro2 = Thread(target=carro, args=[1.5, 'Mario'])

t_carro1.start()
t_carro2.start()
