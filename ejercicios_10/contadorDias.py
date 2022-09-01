import tkinter
from datetime import datetime as dt
from datetime import timedelta as td
from tkinter.font import Font

class contador():
    def dias():
        hoy = dt.now( )
        inicio = dt.strptime(('2022:05:19'),'%Y:%m:%d')
        dif = int((hoy - inicio) / td(days=1))
        return dif

    dias = dias()    
    ventana = tkinter.Tk()
    #tamaño de la ventana
    ventana.geometry('200x200')
    #ventana sin titulo
    ventana.title('')
    #ventana transparente
    ventana.attributes('-alpha', 0.5)
    #sin icno en la barra de titulo
    ventana.attributes('-toolwindow', True)

    #fuente a usar
    fuente1 = Font(family='Comic Sans Ms', size= 25,slant= 'roman', weight='bold')
    fuente2 = Font(family='Comic Sans Ms', size= 50,slant= 'roman', weight='bold')

    #etiquetas
    dia_label1 = tkinter.Label(ventana, text = 'DÍAS', bg = 'white', fg= 'green', font= fuente1)
    dia_label1.pack(ipadx=50, ipady= 10, fill= 'both')

    dia_label2 = tkinter.Label(ventana, text = dias, bg = 'white', fg= 'green', font = fuente2)
    dia_label2.pack(ipadx=50, ipady= 50, fill= 'both')


    ventana.mainloop()

