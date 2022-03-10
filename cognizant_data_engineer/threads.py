from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0 
    while trajeto <= 100:
        trajeto +=velocidade
        time.sleep(0.5)
        print(f'{piloto}: {trajeto}Km')
        
    print(f'{piloto} chegou!')

t_carro1 = Thread(target = carro, args = [10, 'Dick Vigarista'])
t_carro2 = Thread(target = carro, args = [20, 'Mbappé'])
    
t_carro1.start()
t_carro2.start()
