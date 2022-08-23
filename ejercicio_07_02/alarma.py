
from datetime import datetime, timedelta

class alarma():
    """comprobar la hora del sistema contra la hora de salida"""

    _h =''
    """_h representa la hora de salida en formato 24"""
    _m = ''
    """_m representa los minutos de salida"""
    
    def __init__(self):
        """ el constructor de la clase, pide la hora y los minutos de la salida,
        corre automaticamente la funcion mensaje"""
        self._h = input('Ingrese la hora de salida: \n')
        self._m = input('Ingrese los minutos de salida: \n')
        self.mensaje()

    def set_salida(self):
        """devuelde un obj del tipo datetime.datetime que representa la hora de salida"""
        dia = datetime.now().date().strftime('%Y:%m:%d')
        
        salida = datetime.strptime((dia + ':' + self._h + ':' + self._m + ':'+'00' ),'%Y:%m:%d:%H:%M:%S')
        
        return salida
        
    def set_hora(self):    
        """devuelde un obj del tipo datetime.datetime que representa la hora actual del sistema"""
        hora = datetime.now()
        
        return hora

    def set_dif(self):
        """devuelde un obj del int que representa la diferencia en minutos entre la horas
        de salida y la del sistema"""
        hora = self.set_hora()
        
        salida = self.set_salida()
        
        min = int((salida-hora) / timedelta(minutes= 1))
        
        return min
        
    def mensaje(self):
        """devuelve un str  dependiendo del return de set_dif"""
        minutos = self.set_dif()
        
        if minutos <= 0:
            print('Tu horario de trabajo ya termino')
        
        else:
            t = str(minutos // 60) + ' hrs y ' + str(minutos % 60) + ' min'
            print('Restan ' + t + ' para terminar tu horario')


 