import sqlite3
import pprint

class Alumnos():
    archivo = 'alumnos.txt'
    op =''
    selStatement = ''
    def __init__(self):
        super().__init__()
        self.crearTabla()
        #self.menuPrincipal()
        
    
    def crearTabla(self):
        con = sqlite3.connect('ejercicios_11\\alumnos.db')
        cur = con.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS Alumnos
                    (Id integer primary key autoincrement,
                    Nombre text not null,
                    Apellido text not null)''')
        cur.close()
        con.close()
          
    def menuPrincipal(self):
            
        print('Bienvenidos al adminstrador de Alumnos\nQue desea hacer?')
        menu ='Ver alumnos:\t\t1\nBuscar Alumno:\t\t2\nAgregar alumno:\t\t3\n'\
                   'Modificar alumno:\t4\nQuitar alumno:\t\t5\nSalir:\t\t\t6\n'
        print(menu)
        op =input()
        if op != '6':
            self.op = op
        else:
            print('Hasta luego')
    """
    def selAccion(self):
        match self.op:
            case '1':
                self.selStatement = 'SELECT'
            case '1':
                self.selStatement = 'SELECT'
            case '1':
            case '1':
            case '1':
    """    
    
    def presentarDatos(self, datos):
        for d in datos:
            linea = f'{d[0]:<10}{d[1]:20}{d[2]:20}'
            print(linea)
        
    def verAlumnos(self,  nombre = ''):
        nombre = nombre.split()
        largo = len(nombre)
        query1 = ''
        query2 = ''
        match largo:
            case 0:
                query1 = f'''select * from Alumnos'''
            case 2:
                query1 = f'''select * from Alumnos where 
                            Nombre = "{nombre[0]}" and
                            Apellido ="{nombre[1]}"'''
            case 1:
                query1 = f'''select * from Alumnos where 
                            Nombre = "{nombre[0]}"'''
                query2 = f'''select * from Alumnos where 
                            Apellido ="{nombre[0]}"'''
        con = sqlite3.connect('ejercicios_11\\alumnos.db')
        cur = con.cursor()
        rows = cur.execute(query1)
        campos = list(map(lambda x: x[0], rows.description))
        lineas = rows.fetchall()
        if len(lineas) == 0:
            rows = cur.execute(query2)
            campos = list(map(lambda x: x[0], rows.description))
            lineas = rows.fetchall()
        cur.close()
        con.close()
        encabezado =(campos[0], campos[1], campos[2])
        datos = [encabezado]
        for l in lineas:
            datos.append(l)
        return datos
    
    def buscarAlumno(self):
        nombre = input('Ingrese al alumno buscado\n')
        datos = self.verAlumnos(nombre)
        return datos   
    
    def AgregarAlmuno(self):
        datos =[]
        entrada = 'nombre apellido'
        print('Ingrese los nombres y apellidos\n')
        #loop para tomar cada input como una tupla y agregarla a una lista
        while entrada != '':
            entrada = input()
            if entrada != '':
                entrada = entrada.split()
                nap = (entrada[0], entrada[1])
                datos.append(nap)
        con = sqlite3.connect('ejercicios_11\\alumnos.db')
        #inserto en la tabla cada tupla de la lista como un nuevo alumno
        con.executemany('insert into Alumnos(Nombre, Apellido) Values(?, ?)', datos)
        con.commit()
        con.close()
                
if __name__ == '__main__':
    alumno = Alumnos()
    
    
    
    

