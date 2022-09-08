import tkinter as tk
from datetime import datetime as dt
from datetime import timedelta as td
from tkinter.font import Font

class contador(tk.Tk):
    def __init__(self):
        super().__init__()
        
        
        #tamaño de la ventana
        self.geometry('200x200')
        #ventana sin titulo
        self.title('Contador de días')
        #ventana transparente
        self.attributes('-alpha', 0.5)
        #sin icono en la barra de titulo
        self.attributes('-toolwindow', True)
        
        hoy = dt.now( )
        inicio = dt.strptime(('2022:05:19'),'%Y:%m:%d')
        dif = int((hoy - inicio) / td(days=1))
       
        #fuente a usar
        fuente1 = Font(family='Comic Sans Ms', size= 25,slant= 'roman', weight='bold')
        fuente2 = Font(family='Comic Sans Ms', size= 50,slant= 'roman', weight='bold')

        #etiquetas
        dia_label1 = tk.Label(self, text = 'DÍAS', bg = 'white', fg= 'green', font= fuente1)
        dia_label1.pack(ipadx=50, ipady= 10, fill= 'both')

        dia_label2 = tk.Label(self, text = dif, bg = 'white', fg= 'green', font = fuente2)
        dia_label2.pack(ipadx=50, ipady= 50, fill= 'both')
    

if __name__ == '__main__':
    cont = contador()
    cont.mainloop()