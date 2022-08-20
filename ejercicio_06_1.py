#En este ejercicio vais a crear la clase Vehículo la cual tendrá los siguientes atributos:
#Color, Ruedas, Puertas
#Por otro lado crearéis la clase Coche la cual heredará de Vehículo y tendrá los siguientes atributos:
#Velocidad, Cilindrada
#Por último, tendrás que crear un objeto de la clase Coche y mostrarlo por consola.

from tokenize import PseudoExtras
from turtle import pu


class Vehiculo():
    
    _color = None
    _ruedas = None
    _puertas = None

    def __init__(self, color, ruedas, puertas) -> None:
        self._color = color
        self._ruedas = ruedas
        self._puertas = puertas
    
    def set_color(self, color):
        self._color = color

    def set_ruedas(self, ruedas):
        self._ruedas = ruedas

    def set_puertas(self, puertas):
        self._puertas = puertas

    def get_color(self):
        return self._color
    
    def get_ruedas(self):
        return self._ruedas

    def get_puertas(self):
        return self._puertas

class Coche(Vehiculo):

    _veloc = None
    _cilind = None

    def __init__(self, color, ruedas, puertas, veloc, cilind):
        super().__init__(color, ruedas, puertas)
        self._veloc = veloc
        self._cilind =cilind

    def set_veloc(self, veloc):
        self._veloc = veloc

    def set_cilind(self, cilind):
        self._cilind = cilind

    def get_veloc(self):
        return self._veloc
    
    def get_cilind(self):
        return self._cilind

    def ver_todo(self):
        print('Color: '+ self._color + '\n'+
            'Ruedas: '+ self._ruedas + '\n'+
            'Puertas: '+ self._puertas + '\n'+
            'Velocidad: '+ self._veloc + '\n'+
            'Cilindrada: '+ self._cilind )

bmw = Coche('negro','4','2','250','500')
bmw.ver_todo()



