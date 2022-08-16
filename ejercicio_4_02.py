#Escribe un programa capaz de mostrar todos los números impares desde un número de inicio y otro final.
#Por ejemplo: teniendo numero_inicial = 2 y numero_final = 8, el programa debe imprimir por consola: [3, 5, 7]

num_Inic = int(input('Ingresa el numero inicial\n\n'))

num_fin = int(input('\nIngresa el numero final\n\n'))

lista_Num =[]

n = num_Inic
while n <= num_fin:
    if n % 2 == 1:
        lista_Num.append(n)
    n += 1

print('\n')
print(lista_Num)