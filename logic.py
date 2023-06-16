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
                hijo.asignarUtilidadProvisional()

                #Si es la raíz o si el estado del hijo no existe en el árbol
                if (padre_expandido.profundidad == 0 or revisarNodoRepetido(hijo.get_estado(), padre_expandido)):
                    #Agreguélo al principio de la pila
                    pila.insert(0,hijo)

        #Agregar padre a la lista de nodos expandidos
        expandidos.append(padre_expandido)
        
    return expandidos   


def generarHijos(primerHermano, padre, listaNodos):
    hijos = []
    hijos.append(primerHermano)

    ultima_posicion = -1  # Inicializar la variable con un valor inválido
    for i, nodo in enumerate(listaNodos):
        if nodo.get_padre() == padre:
            hijos.append(nodo)
            ultima_posicion = i  # Actualizar la posición del último nodo añadido

    return hijos, ultima_posicion


def calcularUtilidadHijoEnLista(lista_hijos):

    for hijo in lista_hijos:
        hijo.calcularUtilidad()

    lista_hijos.sort(key=lambda x: x.get_valor_utilidad())    

    return lista_hijos

def podarHijos(lista_hijos, listaArbol, num):
    nodos_a_eliminar = lista_hijos[num:]  # Excluye el primer nodo de lista_hijos
    listaArbol = [nodo for nodo in listaArbol if nodo not in nodos_a_eliminar]
    return listaArbol



def podaAlphaBetha (nivel, matriz):

    nodos_expandidos = generarArbolProfundidad(nivel, matriz)
    posicion_nodo = 0
    padre_nodo_actual = None
    abuelo_padre_actual = None
    nodo_actual = None

    while (posicion_nodo < len(nodos_expandidos)):

        #Si el nodo no tiene la profundidad correspondiente
        if nodos_expandidos[posicion_nodo].get_profundidad() != nivel:
            posicion_nodo += 1
            continue

        nodo_actual = nodos_expandidos[posicion_nodo]

        #Si el padre y el abuelo del nodo actual aun no se ha  o si el padre actual es diferente del padre del nodo actual
        if padre_nodo_actual is None or padre_nodo_actual != nodo_actual.get_padre():
            padre_nodo_actual = nodo_actual.get_padre()
            abuelo_padre_actual = padre_nodo_actual.get_padre()

        hijos, posicion_nodo = generarHijos(nodo_actual, padre_nodo_actual, nodos_expandidos)
        posicion_nodo +=1

        lista_hijos = calcularUtilidadHijoEnLista(hijos)
        
        #Si el nodo tiene utilidad infinita
        if abuelo_padre_actual.get_valor_utilidad() in [float('-inf'), float('inf')]: 

            if padre_nodo_actual.get_tipo() == 'MAX':
                padre_nodo_actual.set_valor_utilidad(lista_hijos[-1].get_valor_utilidad())
            else:
                padre_nodo_actual.set_valor_utilidad(lista_hijos[0].get_valor_utilidad())
            abuelo_padre_actual.set_valor_utilidad(padre_nodo_actual.get_valor_utilidad())   
            
            continue

        else:
            if abuelo_padre_actual.get_tipo() == 'MAX':

                for i, nodo in enumerate(lista_hijos):
                    if (abuelo_padre_actual.get_valor_utilidad() >= nodo.get_valor_utilidad()):
                        nodos_expandidos = podarHijos(lista_hijos, nodos_expandidos, i+1)     
                        padre_nodo_actual.set_valor_utilidad(min(padre_nodo_actual.get_valor_utilidad(), nodo_actual.get_valor_utilidad()))
                        abuelo_padre_actual.set_valor_utilidad(max(abuelo_padre_actual.get_valor_utilidad(), padre_nodo_actual.get_valor_utilidad()))
                        posicion_nodo -= len(lista_hijos)-(i+1)
                        break
                    padre_nodo_actual.set_valor_utilidad(min(padre_nodo_actual.get_valor_utilidad(), nodo.get_valor_utilidad()))
                    abuelo_padre_actual.set_valor_utilidad(max(abuelo_padre_actual.get_valor_utilidad(), padre_nodo_actual.get_valor_utilidad()))
            else:
                for i, nodo in enumerate(lista_hijos):
                    if (abuelo_padre_actual.get_valor_utilidad() <= nodo.get_valor_utilidad()):
                        nodos_expandidos = podarHijos(lista_hijos, nodos_expandidos, i+1)    
                        padre_nodo_actual.set_valor_utilidad(max(padre_nodo_actual.get_valor_utilidad(), nodo_actual.get_valor_utilidad()))
                        abuelo_padre_actual.set_valor_utilidad(min(abuelo_padre_actual.get_valor_utilidad(), padre_nodo_actual.get_valor_utilidad())) 
                        posicion_nodo+= (i+1)
                        break
                    padre_nodo_actual.set_valor_utilidad(max(padre_nodo_actual.get_valor_utilidad(), nodo.get_valor_utilidad()))
                    abuelo_padre_actual.set_valor_utilidad(min(abuelo_padre_actual.get_valor_utilidad(), padre_nodo_actual.get_valor_utilidad()))

    children, pos = generarHijos(nodos_expandidos[1], nodos_expandidos[1].get_padre(), nodos_expandidos) 
    proximo_movimiento = children.pop(children.index(max(children, key=lambda x: x.get_valor_utilidad())))

    return proximo_movimiento               

for fila in podaAlphaBetha(2, matriz).get_estado():
    print(fila, '\n')
    

