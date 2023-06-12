#Verifica si los elementos de una lista están en una matriz o arroja las coordenadas de un elemento a buscar
def ubicarElementos(matriz, elementoabuscar, elementos):
    coordenadas = []
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            elemento = matriz[fila][columna]
            if elementos is not None:
                if elemento in elementos:
                    return False
            elif elementoabuscar is not None:
                if elemento == elementoabuscar:
                    coordenadas.append((fila, columna))
    if coordenadas:
        return coordenadas
    return True
   
#___________________________________________________________________________________________________

def revisarNodoRepetido(posibleEstado, nodoPadre):
    if nodoPadre.get_padre() == None: # el nodo no tiene padre (es la raíz)
        return True # el estado del hijo es diferente a todos los ancestros
    #Se compara directamente con el abuelo, porque un padre nunca se tendrá así mismo como hijo
    elif posibleEstado == nodoPadre.get_padre().get_estado(): # el estado del hijo es igual al del padre
        return False # el estado del hijo es igual a uno de sus ancestros
    else:
        return revisarNodoRepetido(posibleEstado, nodoPadre.get_padre()) # recursivamente revisa al siguiente ancestro
