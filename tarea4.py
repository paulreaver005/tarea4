import random
import math
def potecia():
    for x in range(10):
        valor = random.randint(1, 10)
    return valor


camion = lambda x : (2 * x)+1
tractor = lambda x: round((math.log(x, 2)))
sedan = lambda x: (3 * x)**2
bus = lambda x: 5 * x

def ganador(x):
    if x >= 1000:
        return True
    return False

flota = {
    'camion' : camion,
    'tractor' : tractor,
    'sedan' : sedan,
    'bus' : bus
}

ciclo = 1
competidor = False
distanciaVehiculo = 0
distanciacamion = 0
distanciatractor = 0
distanciasedan = 0
distanciabus = 0


while ciclo < 5:
    for vehiculo in flota.keys():
            distanciaVehiculo =  flota[vehiculo](potecia())
            if vehiculo == 'camion':
                distanciacamion = distanciacamion + distanciaVehiculo
                competidor = ganador(distanciacamion)
                print(vehiculo, distanciacamion, ganador(distanciacamion))
            elif vehiculo == 'tractor':
                distanciatractor = distanciatractor + distanciaVehiculo
                competidor = ganador(distanciatractor)
                print(vehiculo, distanciatractor, ganador(distanciatractor))
            elif vehiculo == 'sedan':
                distanciasedan = distanciasedan + distanciaVehiculo
                competidor = ganador(distanciasedan)
                print(vehiculo, distanciasedan, ganador(distanciasedan))
            elif vehiculo == 'bus':
                 distanciabus = distanciabus + distanciaVehiculo
                 competidor = ganador(distanciabus)
                 print(vehiculo, distanciabus, ganador(distanciabus))
    ciclo +=1



distanciaAcumulada = {
    'camion': distanciacamion,
    'tractor': distanciatractor,
    'sedan': distanciasedan,
    'bus': distanciabus
}

for x in distanciaAcumulada.keys():
    print(x,distanciaAcumulada[x])



