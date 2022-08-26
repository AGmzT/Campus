"""Ejercios del tema 8"""
from registro import registro as reg
from vehiculo import vehiculo as ve
def main():
    op = input('Elige un ejercicio a realizar\n Ejercicio 1: 1\n Ejercicio 2: 2\n Salir: 3\n')
    while op != '3':
        if op == '1':
            e = reg()
        elif op == '2':
            e = ve()
        elif op == '3':
            print('Saliendo')
        else:
            print('Ingrese 1 o 2')
        

if __name__ == '__main__':
    main()