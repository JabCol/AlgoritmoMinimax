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
   
#_____________________________________________________________________________________________

