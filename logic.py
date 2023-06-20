from ClaseNodo import Nodo  
from funciones import revisarNodoRepetido
#from main import nivel, matriz

#Variables necesarias
matriz = [
    [0, 0, 0, 0, 0, 4, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [10, 0, 1, 0, 0, 0,'N',0],
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
                #Ingresar hijos
                padre_expandido.set_hijos(hijo)

                #Agreguélo al principio de la pila
                pila.insert(0,hijo)
        elif padre_expandido.get_profundidad() == nivel:
            padre_expandido.calcularUtilidad()

        #Agregar padre a la lista de nodos expandidos
        expandidos.append(padre_expandido)
        
    return expandidos   

        
def mejorMovimiento(nivel, matriz):
    arbol = generarArbolProfundidad(nivel, matriz)

    def minimax(nodo, esMaximizador):
        if nodo.get_profundidad() == nivel:
            return nodo.get_valor_utilidad()

        if esMaximizador:
            valor = float('-inf')
            for hijo in nodo.get_hijos():
                valor = max(valor, minimax(hijo, False))
            nodo.set_valor_utilidad(valor)
            return valor
        else:
            valor = float('inf')
            for hijo in nodo.get_hijos():
                valor = min(valor, minimax(hijo, True))
            nodo.set_valor_utilidad(valor)
            return valor

    for nodo in arbol:
        minimax(nodo, True)

    mejor_movimiento = max(arbol, key=lambda x: x.get_valor_utilidad())
    return mejor_movimiento.get_estado()

movimiento = mejorMovimiento(2, matriz)

for fila in movimiento:
    print(fila)

    

