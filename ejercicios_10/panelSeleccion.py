
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from msilib.schema import RadioButton

class Selector(tk.Tk):
    def __init__(self):
        super().__init__()
    
        ##configuración de la ventana
        #tamaño
        self.geometry('150x200')
        #titulo
        self.title('Seleccionador')
        #sin icono en barra de titulo
        self.attributes('-toolwindow', True)
        #no se puede cambiar el tamaño
        self.resizable(False, False)
        #ancho de la columna
        self.columnconfigure(0, weight = 1)
        #ejecuta la funcion aceptar
        self.aceptar()
    
    def salir(self):
        # funcion para cerrar la ventana
        self.quit()
     
    def aceptar(self):   
        ##contrucción de los componentes
        #variable que almacena la eleccion
        seleccion = tk.StringVar()
        
        def limpiar():
            #muestra un mensaje con que eleccion se tomo
            showinfo('Mensaje', message= 'Selecciono la '+ str(seleccion.get()), )
            #limpia la seleccion
            seleccion.set(None)
        #define y configura los Radiobutton
        sel1 = ttk.Radiobutton(self, text= 'Opción 1', value= 'Opción 1', variable= seleccion)
        sel2 = ttk.Radiobutton(self, text= 'Opción 2', value= 'Opción 2', variable= seleccion)
        sel3 = ttk.Radiobutton(self, text= 'Opción 3', value= 'Opción 3', variable= seleccion)
        
        sel1.grid(column= 0, row= 0, padx= 5, pady= 5)
        sel2.grid(column= 0, row= 1, padx= 5, pady= 5)
        sel3.grid(column= 0, row= 2, padx= 5, pady= 5)

        #define y configura los bottons
        button1 = ttk.Button(self, text= 'Aceptar', command= limpiar)
        button1.grid(column= 0, row= 3, padx= 5, pady= 5)
        
        button2 = ttk.Button(self, text= 'Salir', command= self.salir)
        button2.grid(column= 0, row= 5, padx= 5, pady= 5)
        
if __name__ == '__main__':
    selector = Selector()
    selector.mainloop()