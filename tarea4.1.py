hoja_calculo = [
    ['carlos', 54.54,6.57,3.64],
    ['juan', 5.54,9.57,4.64],
    ['luis', 9.54,7.57,1.64] ,
]

def transpuesta(hoja_calculo):
    return [list(i) for i in zip(*hoja_calculo)]

b = transpuesta(hoja_calculo)

def multiplicacion(x):
    for i in range(1, 4):
        b[i] = list(map(lambda x: x * x, b[i]))
    i+=1
    return b

def veintePorCiento(x):
    for i in range(1, 4):
        b[i] = list(map(lambda x: x * 0.20, b[i]))
    i+=1
    return b

def suma(x):
    num = 1
    total = 0
    for i in range(1,4):
        for ele in range(0,len(x[num])):
            total = total + x[num][ele]
    i+=1
    return total

def promedio(x):
    num1 = 1
    cuenta = 0
    total = suma(b)
    for i in range(1,4):
        for valor in range(0,len(x[num1])):
            cuenta = cuenta + 1
    i+=1
    return total / cuenta




diccionario = {
    'Suma': suma,
    'Promedio': promedio,
    'Multiplicacion': multiplicacion,
    'Veinte por ciento': veintePorCiento,
    'Transpuesta': transpuesta

}

print('Lista Original:')
print(hoja_calculo)
print('Lista Transpuesta')
print(b)

for f in diccionario.keys():
    print('resultado de ', f,': ',  diccionario[f](b))







