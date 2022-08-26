from datetime import datetime as dt

class vehiculo():
    """Representacion de un vehiculo, con los atributos de marca, modelo, color y precios """
    
    _archivo ='ejercicios_08\listaVehiculos.txt'
    
    def __init__(self):
        
        opcion = None
        while opcion != '4':
            opcion =input('Buenos días!\n Menu:\n Ver todos los Vehículo- 1\n Agregar Vehículo - 2\n Borrar Vehículo - 3\n Salir - 4\n')
            match opcion:
                case '1':
                    self.verVeh()
                case '2':
                    self.agregarVeh()
                case '3':
                    self.borrarVeh()
                case '4':
                    print('Hasta luego')
                case '':
                    print('Ingersa 1, 2, 3, o 4')

    def verVeh(self):
        r = open(self._archivo, 'r' )
        lineas = r.readlines()
        r.close()
        
        for linea in lineas:
            print(linea)
    
    def agregarVeh(self):
        
        marca = input('ingresa la marca: ')
        modelo = input('ingresa el modelo: ')
        color =  input('ingresa el color: ')
        precio =  input('ingresa el precio: ')
        linea = f'{marca:20}{modelo:20}{color:20}{precio:20}\n'
        r = open(self._archivo, 'a')
        r.writelines(linea)
        r.close()

    def borrarVeh(self):
        r = open(self._archivo, 'r' )
        lineas = r.readlines()
        r.close()
        for linea in lineas:
            indice = lineas.index(linea)
            l = linea
            if indice == 0:
                print('Indice\t'+l )
            else:
                print(indice, '\t',linea)
        op = int(input('Ingresa el indice del vehiculo que deseas borrar: '))
        lineas.pop(op)
        r = open(self._archivo, 'w')
        for linea in lineas:
            r.write(linea)
        r.close()