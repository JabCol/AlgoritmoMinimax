from ClaseNodo import Nodo  
from funciones import revisarNodoRepetido

#Variables necesarias
matriz = [
    [0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 1, 0, 0, 0,'N',0],
    [0, 7, 0, 0, 3, 0, 0, 0],
    [0,'B',0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 6, 0, 0, 0],
    [0, 0, 5, 0, 0, 0, 2, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
]
pila = [] #Guardará los nodos hijos

#Función que genera árbol por profundidad dependiendo de la matriz que le ingrese y el nivel
def generarArbolProfundidad (nivel, matrizE):
    #Definir padre inicial
    padre = Nodo(matrizE, None, None)
    #Agregar padre a la pila
    pila.insert(0,padre)
    #Variable que contendrá el primer elemeto de la pila, es decir el padre
    padre_expandido = 0
    #Lista de nodos expandidos
    expandidos = []
    
    #Verificar si terminó el juego
    if padre.pruebaTerminal():
        #Ya hay un resultado final
        return
    
    #Ejecute mientras la pila este llena
    while pila:
        #Sacar padre de la pila
        padre_expandido = pila.pop(0)

        if padre_expandido.get_profundidad() < nivel:
            #Crear hijos
            for nueva_matriz, puntoMAX, puntoMIN, operador in padre_expandido.moverElemento():
                #Cree el nodo hijo
                hijo = Nodo(nueva_matriz, padre_expandido, operador)
                #Modificar puntuación
                hijo.set_punto_max(puntoMAX)
                hijo.set_punto_min(puntoMIN)
                #Modificar tipo
                hijo.modificarTipo()
                #Modificar profundidad
                hijo.modificarProfundidad()
                #Modificar utiilidad
                hijo.set_valor_utilidad()

                #Si es la raíz o si el estado del hijo no existe en el árbol
                if (padre_expandido.profundidad == 0 or revisarNodoRepetido(hijo.get_estado(), padre_expandido)):
                    #Agreguélo al principio de la pila
                    pila.insert(0,hijo)

        #Agregar padre a la lista de nodos expandidos
        expandidos.append(padre_expandido)
    return expandidos

def podarArbol(nivel, matriz):
    nodos_expandidos = generarArbolProfundidad(nivel, matriz)
    posicion_nodo = 0
    arreglo_nodos = []
    padre_nodo_hoja=0
    se_poda = 'no'

    for nodo in nodos_expandidos[posicion_nodo+1]:
        if nodo.get_profundidad() == nivel:
            posicion_nodo = nodos_expandidos.index(nodo)
            nodo_hoja_actual = nodo

            if padre_nodo_hoja == 0:
                padre_nodo_hoja = nodo_hoja_actual.get_padre()    
    
            if nodo_hoja_actual.get_padre().get_padre().get_valor_utilidad() in [float('-inf'), float('inf')]:
                nodo_hoja_actual.calcularUtilidad()
                padre_nodo_hoja.quitarInfinito(nodo_hoja_actual.get_valor_utilidad())
                padre_nodo_hoja.get_padre().quitarInfinito(padre_nodo_hoja.get_valor_utilidad())


print(podarArbol(2, matriz))