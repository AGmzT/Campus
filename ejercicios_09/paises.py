def pedirPaises():
    #pide al usuario que ingre los paises, y devuelve un lista conteniendolos
    listaPaises = input('Ingresa los paises separados por coma y espacio:\n ').split(', ')
    
    return listaPaises

def mostrarPaises():
    # toma la lista que retorna pedirPaises y la transforma en un set
    lista = pedirPaises()
    paises = set()
    
    for l in lista:
        paises.add(l.capitalize())
    return paises


paises = mostrarPaises()
print(paises, type(paises))


