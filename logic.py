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
    return len(nodos_expandidos)

print(podarArbol(2, matriz))