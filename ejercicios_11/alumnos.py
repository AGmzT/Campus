import sqlite3

class Querys():
    """ Clase que tomas las entradas y devuelve un str o listque representa
    la o las querys"""
    
    def queryCrearTabla(self):
        """Crea un str para crear la tabla Alumnos si no existe
        """
        query = '''CREATE TABLE IF NOT EXISTS Alumnos
                    (Id integer primary key autoincrement,
                    Nombre text not null,
                    Apellido text not null)'''
        return query
    
    def queryVerTodo(self):
        """Debuelve un str que representa una query para mostra todos
        los registros.
            Returns:
                query (str): [str devuelto que representa la query a ejecutar]
        """
        query = 'select * from Alumnos order by Apellido asc'
        return query
    
    def queryBuscar(self):
        """Debuelve un str que representa una query para buscar todos
        los registros, o segun una o dos condiciones.
            Parameters:
                nombre (str): [nombre buscado, si se omite se busca cualquiera]
                apellido (str): [apellido buscado, si se omite se busca cualquiera]
                campo (str): [columna en la que se busca, si se omite se busca en todas]
            Returns:
                query (str): [str devuelto que representa la query a ejecutar]
        """
        campo = input('Ingrese la columna en la que busca\n,si lo omite se busca en todas\n')
        nombre = input('Ingrese el nombre buscado, si lo omite se buscan todos\n')
        apellido = input('Ingrese el apellido buscado, si lo omite se buscan todos\n')
        
        query = 'select * from Alumnos'
        if campo == 'Nombre':
            query = f'''select * from Alumnos
            where Nombre = "{nombre}" order by Apellido asc'''
        elif campo == 'Apellido':
            query = f'''select * from Alumnos where 
            Apellido = "{apellido}" order by Nombre asc'''
        elif nombre and apellido:
            query = f'''select * from Alumnos where 
            Nombre = "{nombre}" and
            Apellido ="{apellido}" order by Apellido asc'''
        return query
    
    def queryAgregar(self):
        """Debuelve un list que contiene los querys que se
        ejecutaran para insertar uno o mas registros.
            Parameters:
                nombre (str): [nombre a agregar, no se puede omitir]
                apellido (str): [apellido a agregar, no se puede omitir]
            Returns:
                querys (list): [list devuelto que contiene todas la query a ejecutar]
        """
        querys =[]
        nombre = 'nombre'
        apellido = 'apellido'
        #loop para seguir tomando inputs
        while nombre and apellido :
            nombre = input('Ingrese el nombre a agregar, no se puede omitir\n')
            apellido = input('Ingrese el apellido a agregar, no se puede omitir\n')
            if nombre and apellido:
                query = f'''insert into Alumnos(Nombre, Apellido) Values('{nombre}', '{apellido}')'''
                querys.append(query)
        return querys
    
    def queryMod(self):
        """Debuelve un list que contiene los querys que se
        ejecutaran para modificar uno o mas registros.
            Parameters:
                id (int): [indice del registro que modificara, no se puede omitir] 
                nombre (str): [nuevo nombre, no se puede omitir]
                apellido (str): [nuevo apellido, no se puede omitir]
            Returns:
                querys (list): [list devuelto que contiene todas la query a ejecutar]
        """
        querys = []
        id = 'id'
        #loop para seguir tomando inputs
        while id != '' :
            id = input('Ingrese el id del alumno que desea modificar\n')
            if id != '':
                id = int(id)
                nombre = input('Ingrese el nuevo nombre\n')
                apellido = input('Ingrese el nuevo apellido\n')
                if nombre and apellido:
                    query = f'''update Alumnos set Nombre = "{nombre}", Apellido = "{apellido}" where Id = "{id}"'''
                    querys.append(query)
                elif nombre and not apellido:
                    query = f'''update Alumnos set Nombre = "{nombre}" where Id = "{id}"'''
                    querys.append(query)
                elif not nombre and apellido:
                    query = f'''update Alumnos set Apellido = "{apellido}" where Id = "{id}"'''
                    querys.append(query)
        return querys
          
    def queryBorrar(self):
        """Debuelve un list que contiene los querys que se
        ejecutaran para borrar uno o mas registros.
            Parameters:
                id (int)= [indice del registro que borrara, no se puede omitir] 
            Returns:    
                querys (list): [list devuelto que contiene todas la query a ejecutar]
        """
        querys = []
        id = 'id'
        #loop para seguir tomando inputs
        while id != '' :
            id = input('Ingrese el id del alumno que desea borrar\n')
            if id != '':
                id = int(id)
                query = f'''delete from Alumnos where Id = "{id}"'''
                querys.append(query)
        return querys

class Ejecutor():
    """Clase que toma los querys y realiza la ejecuciones correspondientes
        Attributes:
        archivo (str): representa el archivo de la DB
    """
    archivo = 'ejercicios_11\\alumnos.db'
    
    
    def crearTabla(self, query):
        """Ejecuta la creacion de la tabla Alumnos en la DB"""
        con = sqlite3.connect(self.archivo)
        cur = con.cursor()
        cur.execute(query)
        cur.close()
        con.close()
    
    def buscar(self, query):
        """"Ejecuta la busqueda de uno o más registros
            Devuelve un list con los registro obtenidos
            Parameters:
                query (str): la query que  se ejecutara
                rows (cursos): contiene el resultado de la ejecucion
                campos (tuple): tuple que contine los nombre de las columnas
                lineas (list): wraps rows en una lista cuyos items son
                                tuplas, cada tupla es un registro de la
                                tabla
            Returns:
                datos (list): list que combina campos y lista
            """
        con = sqlite3.connect(self.archivo)
        cur = con.cursor()
        rows = cur.execute(query)
        campos = tuple(map(lambda x: x[0], rows.description))
        lineas = rows.fetchall()
        cur.close()
        con.close()
        datos = [campos]
        for l in lineas:
            #loop para agregar de a uno cada item de lineas a datos
            datos.append(l)
        return datos
    
    def agregar(self, querys):
        """"Ejecuta la inserción de uno o más registros
            Parametars:
                querys (list): list que contiene la query o querys
                                que ejecutaran
            """
        con = sqlite3.connect(self.archivo)
        cur = con.cursor()
        for query in querys:
            #loop para ejecutar y commit cada query de a una
            con.execute(query)
            con.commit()
        cur.close()
        con.close()
    
    def modificar(self, querys):
        """"Ejecuta la modificación de uno o más registros
            Parameters:
                querys (list): list que contiene la query o querys
                                que ejecutaran
            """
        con = sqlite3.connect(self.archivo)
        cur = con.cursor()
        for query in querys:
            #loop para ejecutar y commit cada query de a una
            con.execute(query)
            con.commit()
        cur.close()
        con.close()
    
    def borrar(self, querys):
        """"Ejecuta la eliminación de uno o más registros
            Parameters:
                querys (list): list que contiene la query o querys
                                que ejecutaran
            """
        con = sqlite3.connect(self.archivo)
        cur = con.cursor()
        for query in querys:
            #loop para ejecutar y commit cada query de a una
            con.execute(query)
            con.commit()
        cur.close()
        con.close()
         
class Alumnos():
    """Clase principal del modulo, adminstra la base de datos
    Attributes:
        archivo (str): base de datos
        query (Querys): 
        ejec (Ejecutor):
    """
    
    archivo = 'ejercicios_11\\alumnos.db'
    query = Querys()
    ejec = Ejecutor()
    
    def __init__(self):
        super().__init__()
        """Constructor de la clase"""    
        self.menuPrincipal()
        
    def presentarDatos(self, datos):
        """Metodo para representar los datos
        Parameters:
            datos (list): lista que contiene los datos a representar
        """ 
        for d in datos:
            linea = f'{d[0]:<10}{d[1]:20}{d[2]:20}'
            print(linea)

    def menuPrincipal(self):
        """Menu que ejecuta al iniciar el programa
        Paraemters:
            op (str): opcion elejida por el usuario
        """   
        print('Bienvenidos al adminstrador de Alumnos\n')
        op = ''
        """loop que continua mostrando el menu hasta que
            se elige salir"""
        while op != '6':
            print('\n\
                Que desea hacer?\n\
                Ver alumnos:\t\t1\n\
                Buscar Alumno:\t\t2\n\
                Agregar alumno:\t\t3\n\
                Modificar alumno:\t4\n\
                Quitar alumno:\t\t5\n\
                Salir:\t\t\t6')
            op =input()
            match op:
                case '1':
                    """muestra todos los registros"""
                    query = self.query.queryVerTodo()
                    datos = self.ejec.buscar(query)
                    self.presentarDatos(datos)
                case '2':
                    """muestra los registros que coinciden con
                    las condiciones de busqueda"""
                    query = self.query.queryBuscar()
                    datos = self.ejec.buscar(query)
                    self.presentarDatos(datos)
                case '3':
                    """"agrega nuevos registros a la DB"""
                    querys = self.query.queryAgregar()
                    self.ejec.agregar(querys)
                case '4':
                    """"modifica registros en la DB"""
                    query1 =self.query.queryVerTodo()
                    datos = self.ejec.buscar(query1)
                    self.presentarDatos(datos)
                    querys2 = self.query.queryMod()
                    self.ejec.modificar(querys2)
                case '5':
                    """borra registros en la DB"""
                    querys1 = self.query.queryVerTodo()
                    datos1 = self.ejec.buscar(querys1)
                    self.presentarDatos(datos1)
                    querys2 = self.query.queryBorrar()
                    self.ejec.borrar(querys2)
                case '6':
                    """sale del programa"""
                    print('Hasta luego')
      
if __name__ == '__main__':
    aaa = Alumnos()
    
    
    
    
    

