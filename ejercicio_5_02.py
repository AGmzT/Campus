#Escribe una función que pueda decirte si un número (número entero) es primo o no.

def es_primo(numero):
     
    for n in range(2, numero):
        if numero % n == 0:
            return 'no es primo'
            break
    return 'es primo'  

print(es_primo(15))