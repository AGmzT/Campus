#Escribe un programa que sea capaz de mostrar los números del 1 al 100 en orden inverso

lista = []

n = 100
while n >= 1:
    lista.append(n)
    n -=1

print(lista)