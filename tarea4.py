import random
import math

def potecia():
    for x in range(10):
        valor = random.randint(1, 10)
    return valor

def mayor(num1,num2,num3,num4):
    if(num1>=num2) and (num1>=num3) and (num1>=num4):
         numeroMayor = num1
    elif(num2>=num1) and (num2>=num3) and (num2>=num4):
         numeroMayor = num2
    elif(num3>=num1) and (num3>=num2) and (num3>=num4):
         numeroMayor = num3
    else:
         numeroMayor = num4
    return numeroMayor

camion = lambda x : (2 * x)+1
tractor = lambda x: round((math.log(x, 2)))
sedan = lambda x: (3 * x)**2
bus = lambda x: 5 * x

flota = {
    'camion' : camion,
    'tractor' : tractor,
    'sedan' : sedan,
    'bus' : bus
}

ciclo = 1
lider = 0
distanciaVehiculo = 0
distanciacamion = 0
distanciatractor = 0
distanciasedan = 0
distanciabus = 0


while lider <= 1000:
    for vehiculo in flota.keys():
            distanciaVehiculo =  flota[vehiculo](potecia())
            if vehiculo == 'camion':
                distanciacamion = distanciacamion + distanciaVehiculo

            elif vehiculo == 'tractor':
                distanciatractor = distanciatractor + distanciaVehiculo

            elif vehiculo == 'sedan':
                distanciasedan = distanciasedan + distanciaVehiculo

            elif vehiculo == 'bus':
                 distanciabus = distanciabus + distanciaVehiculo

    ciclo +=1
    lider = mayor(distanciacamion,distanciatractor,distanciasedan,distanciabus)


distanciaAcumulada = {
    'camion': distanciacamion,
    'tractor': distanciatractor,
    'sedan': distanciasedan,
    'bus': distanciabus
}

for x in distanciaAcumulada.keys():
    print(x, 'Distancia recorrida: ', distanciaAcumulada[x], ' metros ', ' - Cantidad de vueltas: ',ciclo)

for x in distanciaAcumulada.keys():
    if lider == distanciaAcumulada[x]:
        print('\nEL VEHICULO GANADOR ES: ',x, 'con un recorrido de ' ,lider, ' metros' )



