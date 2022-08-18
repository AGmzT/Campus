#Escribe una función que calcule el área de un triángulo, recibiendo la altura
# y la base como parámetros y otra función que calcule el área de un 
# círculo recibiendo el radio del mismo.

import math

def area_tri():
    alto = int(input('Ingresa el alto del triángulo  '))
    base = int(input('Ingresa la base del triángulo  '))

    return alto * base

def area_circ():
    radio = int(input('Ingresa el radio del círculo  '))

    return radio**2*math.pi

print(area_tri())
print(area_circ())