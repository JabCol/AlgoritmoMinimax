from funciones import ubicarElementos
import copy

# Clase Nodo
class Nodo:
    #Constructor
    def __init__(self, estado, padre, operador):
        self.estado = estado
        self.padre = padre
        self.operador = operador
        self.puntuacion_max = 0
        self.puntuacion_min = 0
        self.valor_utilidad = float('-inf')
        self.tipo = 'MAX'
        self.profundidad = 0
        self.hijos = []

    #Métodos getters
    def get_padre(self):
        return self.padre
    
    def get_estado(self):
        return self.estado

    def get_profundidad(self):
        return self.profundidad  

    def get_puntuacion_min(self):
        return self.puntuacion_min    
    
    def get_puntuacion_max(self):
        return self.puntuacion_max 

    def get_tipo(self):
        return self.tipo 
    
    def get_operador(self):
        return self.operador
    
    def get_valor_utilidad(self):
        return self.valor_utilidad
    
    def get_hijos(self):
        return self.hijos
    
    #Métodos set
    def set_hijos (self,valor):
        self.hijos.insert(0,valor)

    def set_valor_utilidad (self, valor):
        self.valor_utilidad = valor

    def set_punto_max(self, valor):
        self.puntuacion_max = valor

    def set_punto_min(self, valor):
        self.puntuacion_min= valor              

    #Métodos necesarios para el programa
    def pruebaTerminal(self):
        return ubicarElementos(self.estado, None, [1,2,3,4,5,6,7]) 
    
    def quitarInfinito(self, valor):
        self.valor_utilidad = valor

    def asignarUtilidadProvisional (self):
        if (self.tipo == 'MAX'):
            self.valor_utilidad = float('-inf')
        else:
            self.valor_utilidad = float('inf')  

    def modificarTipo (self):
        if self.padre is None:
            self.tipo = 'MAX' 
        elif self.padre.get_tipo() == 'MAX':
            self.tipo = 'MIN'   
        else:
            self.tipo = 'MAX'    

    def modificarProfundidad (self):
        if (self.padre != None):
            self.profundidad = self.padre.get_profundidad() +1  

    def calcularUtilidad(self):
        resultado = self.puntuacion_max - self.puntuacion_min
        self.valor_utilidad = resultado
        # if resultado > 0:
        #     self.valor_utilidad = 1
        # elif resultado < 0:
        #     self.valor_utilidad = -1
        # else:
        #     self.valor_utilidad = 0        

    # def calcularUtilidad(self):
    #     resultado = self.puntuacion_max - self.puntuacion_min
    #     puntaje_max = 0

    #     for movimiento, punmax, punmin, operador in self.moverElemento():
    #         puntaje_max = max(puntaje_max, punmax)

    #     print(resultado)
    #     if resultado != 0:
    #         if (puntaje_max) > self.puntuacion_min:
    #             self.valor_utilidad = 1
    #         elif (puntaje_max) < self.puntuacion_min:
    #             self.valor_utilidad = -1     
    #         else:  
    #             self.valor_utilidad = 0      
    #     else:
    #         if (self.puntuacion_max+puntaje_max) > self.puntuacion_min:
    #             self.valor_utilidad = 0.5
    #         else:
    #             self.valor_utilidad = 0
                       
    def moverElemento(self):

        matriz = self.estado
        
        if self.tipo == 'MAX':
            # Ubicar a caballo blanco y sus coordenadas
            elemento = ubicarElementos(matriz, 'B', None)
            ficha = 'N'
        else:
            # Ubicar a caballo negro y sus coordenadas
            elemento = ubicarElementos(matriz, 'N', None)
            ficha='B'

        fila = elemento[0][0]
        columna = elemento[0][1]

        # Variable necesaria
        movimientos = []
        puntoMAX = self.puntuacion_max
        puntoMIN = self.puntuacion_min

        # Intentar realizar cada movimiento válido
        for row, column, operador in [(2, 1, "baja-derecha"), (2, -1, "baja-izquierda"), (-2, 1, "sube-derecha"), (-2, -1, "sube-izquierda"),(1, 2, "derecha-baja"), (-1, 2, "derecha-sube"), (1, -2, "izquierda-baja"), (-1, -2, "izquierda-sube")]:

            # Verificar si el movimiento es válido
            if fila + row in range(len(matriz)) and columna + column in range(len(matriz[0])) and matriz[fila + row][columna + column] != ficha:

                #copiar matriz original
                matriz_aux = copy.deepcopy(matriz)

                #sume lo que halla en la casilla
                if (ficha == 'N'):
                    #Almacéne la puntuacion en el hijo, puntuacion del padre mas uno.
                    puntoMAX += matriz_aux[fila + row][columna + column]
                else:
                    puntoMIN += matriz_aux[fila + row][columna + column]   
                #Actualizar la matriz con el movimiento
                matriz_aux[fila + row][columna + column] = matriz_aux[fila][columna]
                matriz_aux[fila][columna] = 0
                
                # Agregar la actualización al arreglo    
                movimientos.append((matriz_aux, puntoMAX, puntoMIN, operador))
                puntoMAX = self.puntuacion_max
                puntoMIN = self.puntuacion_min

        # Devolver el arreglo de movimientos válidos
        return movimientos  
    
# matriz = [
#     [0, 0, 0, 0, 0, 4, 0, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
#     [0, 0, 1, 0, 0, 0,'N',0],
#     [0, 1, 0, 0, 3, 0, 0, 0],
#     [0,'B',0, 0, 0, 0, 0, 0],
#     [0, 0, 0, 0, 6, 0, 0, 0],
#     [0, 0, 5, 0, 0, 0, 2, 0],
#     [0, 0, 0, 0, 0, 0, 0, 0],
# ]

# nodo = Nodo(matriz,None,None)
# nodo.set_punto_max(5)
# nodo.set_punto_min(5)
# nodo.calcularUtilidad()
# print(nodo.get_valor_utilidad())