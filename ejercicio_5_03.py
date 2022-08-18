#Escribe una función que pueda decirte si un año (número entero) es bisiesto o no.

def bisiesto(year):
    if year < 1583:
        return 'debe ser un año mayor a 1582'

    elif not year % 4  and (year % 100 or not year % 400):
        return 'Es año bisiesto'
        
    else:
        return 'No es año bisiesto'



