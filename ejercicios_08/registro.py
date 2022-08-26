from datetime import datetime as dt

class registro():
    """Accede a un archivo para leer y registrar la hora de entrada de una persona"""
    
    _archivo ='ejercicios_08\entrada.txt'
    
    def __init__(self):
        
        opcion = None
        while opcion != '3':
            opcion =input('Buenos días!\n Menu:\n Leer el registro - 1\n Agregar entrada - 2\n Salir - 3\n')
            match opcion:
                case '1':
                    self.leerRegistro()
                case '2':
                    self.agregarRegistro()
                case '3':
                    print('Hasta luego')
                case '':
                    print('Ingersa 1, 2, o 3')

    def leerRegistro(self):
        r = open(self._archivo, 'r' )
        lineas = r.readlines()
        r.close()
        
        for linea in lineas:
            print(linea)
    
    def agregarRegistro(self):
        
        nombre = input('ingrese el nombre:\n')
        fecha = dt.strftime((dt.now() ),'%Y:%m:%d: %H:%M')
        linea = nombre + ' -> ' + fecha + '\n'
        r = open(self._archivo, 'a')
        r.writelines(linea)
        r.close()