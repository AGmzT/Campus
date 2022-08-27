from datetime import datetime as dt
from re import A

class vehiculo():
    """Representacion de un vehiculo, con los atributos de marca, modelo, color y precios """
    
    _archivo ='ejercicios_08\listaVehiculos.txt'
    _datos =''
    def __init__(self):
        self._datos = self.leerArchivo()
        """
        op = None
        while opcion != '4':
            a = 'Buenos días!\n Menu:\n'
            b = 'Ver todos los Vehículos:'
            c = 'Agregar Vehículo:'
            d = 'Borrar Vehículo:' 
            e = 'Salir:'
            mensaje =f'{a}{b:25}1\n{c:25}2\n{d:25}3\n{e:25}4\n'
            op = input(mensaje)
            match op:
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
        """
    def leerArchivo(self):
        r = open(self._archivo, 'r' )
        lineas = r.readlines()
        r.close()
        return lineas
    
    def reescribirArchivo(self, lineas):
        r = open(self._archivo, 'w')
        for linea in lineas:
            r.write(linea)
        r.close()
    
    def obt_datos(self):
        lineas = self.leerArchivo()
        lista_v = []
        for linea in lineas:
            linea = linea.replace('\n', ' ')
            linea = linea.split()
            lista_v.append(linea)
        return lista_v
    
    def verVeh(self):
        lineas = self._datos
        for linea in lineas:
            indice = lineas.index(linea)
            l = linea
            if indice == 0:
                print('Indice\t'+l )
            else:
                print(indice, '\t',linea)
    
    def agregarVeh(self):
        linea = input('Ingresa la marca, el modelo, el color'\
        ' y el precio; separados por coma y espacio\n')
        linea = linea.split(', ')
        nuevo = f'{linea[0]:20}{linea[1]:20}{linea[2]:20}{linea[3]:20}'
        r = open(self._archivo, 'a')
        r.writelines(nuevo + '\n')
        r.close()

    def borrarVeh(self):
        lineas = self._datos
        self.verVeh()
        op = int(input('Ingresa el indice del vehiculo que deseas borrar: '))
        lineas.pop(op)
        self.reescribirArchivo(lineas)
        
    def modVeh(self):
        datos = self.obt_datos()
        self.verVeh()
        i = int(input('Ingresa el indice del vehiculo que deseas modificar: '))

        p = None
        while p != '5':
            a, b, c, d, e = 'Marca', 'Modelo', 'Color', 'Precio', 'Cancelar'
            print('Indica que quieres modificar')    
            p = input(f'{a:10}1\n{b:10}2\n{c:10}3\n{d:10}4\n{e:10}5\n')
            n = input('Ingreso el nuevo valor')
            match p:
                case '1':
                    datos[i][0] = n
                case '2':
                    datos[i][1] = n
                case '3':
                    datos[i][2] = n
                case '4':
                    datos[i][3] = n
        self.reescribirArchivo(datos)
                
    
    
        
e = vehiculo()
#e.modVeh()
datos = e.obt_datos()
e.verVeh()
i = int(input('Ingresa el indice del vehiculo que deseas modificar: '))
print(datos[i])
p = None
while p != '5':
    a, b, c, d, e = 'Marca', 'Modelo', 'Color', 'Precio', 'Cancelar'
    print('Indica que quieres modificar')    
    p = input(f'{a:10}1\n{b:10}2\n{c:10}3\n{d:10}4\n{e:10}5\n')
    n = input('Ingreso el nuevo valor')
    match p:
        case '1':
            datos[i][0] = n
        case '2':
            datos[i][1] = n
        case '3':
            datos[i][2] = n
        case '4':
            datos[i][3] = n
print(datos[i])





