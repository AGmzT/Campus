#Programa que tenga una clase llamada Alumno que tenga como atributos su nombre y su nota.
# Deberéis de definir los métodos para inicializar sus atributos,imprimirlos y
# mostrar un mensaje con el resultado de la nota y si ha aprobado o no.

class Alumno():
    _nombre = None
    _nota = None

    def __init__(self, nombre, nota):
        self._nombre = nombre
        if 0<= nota  <= 10:
            self._nota = nota
        else:
            print('La nota debe estar entre  0 y 10 incluidos')
    
    def set_Nota(self, nota):
        self._nota = nota

    def ver_Alumno(self):
        print('Nombre:' + self._nombre + '\n'
            'Nota: ' + str(self._nota))
        if self._nota < 7:
            print('Alumno no aprobado')
        else:
            print('Alumno aprobado')

ale = Alumno('Alejandro', 10)
ale.ver_Alumno()
ale.set_Nota(8)
ale.ver_Alumno()