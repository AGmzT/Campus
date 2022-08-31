from functools import reduce

def sumarImpares():
    #pido los numeros y los transformo en una lista
    cadenas = input('ingrese los numeros:\n ').split(', ' )
    # transformo la lista de string en una lista de enteros
    numeros = []
    
    for cad in cadenas:
        numeros.append(int(cad))
    #descarto los numeros pares de la lista
    impares = filter(lambda x: x % 2, numeros)
    #sumo los numeros impares
    suma = reduce(lambda a, b : a + b, impares)
    
    return suma

