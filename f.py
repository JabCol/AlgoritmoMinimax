def podarArbol(nivel, matriz):
    
    nodos_expandidos = generarArbolProfundidad(nivel, matriz)
    posicion_nodo = 0
    arreglo_nodos = []
    padre_nodo_actual = None
    se_poda = 'no'

    for i in range(posicion_nodo+1, len(nodos_expandidos)):
        
        nodo_hoja_actual = nodos_expandidos[i]
        if nodo_hoja_actual.get_profundidad() == nivel:
            posicion_nodo = i

            if padre_nodo_actual is None:
                padre_nodo_actual = nodo_hoja_actual.get_padre()
            elif se_poda == 'si' and nodo_hoja_actual.get_padre() == padre_nodo_actual:
                nodos_expandidos.remove(nodo_hoja_actual)
                continue  # Continuar con el siguiente nodo en el bucle

            se_poda = 'no'

            if nodo_hoja_actual.get_padre().get_padre().get_valor_utilidad() in [float('-inf'), float('inf')]:
                nodo_hoja_actual.calcularUtilidad()
                arreglo_nodos.append(nodo_hoja_actual)

                if padre_nodo_actual != nodo_hoja_actual.get_padre():
                    arreglo_nodos.sort(key=lambda x: x.get_valor_utilidad())
                    if padre_nodo_actual.get_padre().get_valor_utilidad() == float('-inf'):
                        padre_nodo_actual.quitarInfinito(arreglo_nodos[-1].get_valor_utilidad())
                    elif padre_nodo_actual.get_padre().get_valor_utilidad() == float('inf'):
                        padre_nodo_actual.quitarInfinito(arreglo_nodos[0].get_valor_utilidad())

                    padre_nodo_actual.get_padre().quitarInfinito(padre_nodo_actual.get_valor_utilidad())
                    padre_nodo_actual = nodo_hoja_actual.get_padre()
                    continue  # Continuar con el siguiente nodo en el bucle

            if nodo_hoja_actual.get_padre() != padre_nodo_actual:
                if arreglo_nodos:
                    arreglo_nodos.sort(key=lambda x: x.get_valor_utilidad())
                    if padre_nodo_actual.get_tipo() == 'MAX' and arreglo_nodos[-1].get_valor_utilidad() > padre_nodo_actual.get_valor_utilidad():
                        padre_nodo_actual.set_valor_utilidad(arreglo_nodos[-1].get_valor_utilidad())
                    elif padre_nodo_actual.get_tipo() == 'MIN' and arreglo_nodos[0].get_valor_utilidad() < padre_nodo_actual.get_valor_utilidad():
                        padre_nodo_actual.set_valor_utilidad(arreglo_nodos[0].get_valor_utilidad())
                elif padre_nodo_actual.get_padre().get_tipo() == 'MAX' and padre_nodo_actual.get_padre().get_valor_utilidad() < padre_nodo_actual.get_valor_utilidad():
                    padre_nodo_actual.get_padre().set_valor_utilidad(padre_nodo_actual.get_valor_utilidad())
                    arreglo_nodos.clear()
                    padre_nodo_actual = nodo_hoja_actual.get_padre()

            nodo_hoja_actual.calcularUtilidad()

            if padre_nodo_actual.get_padre().get_tipo() == 'MAX':
                if nodo_hoja_actual.get_valor_utilidad() > padre_nodo_actual.get_padre().get_valor_utilidad():
                    arreglo_nodos.append(nodo_hoja_actual)
                else:
                    se_poda = 'si'
                    padre_nodo_actual.set_valor_utilidad(nodo_hoja_actual.get_valor_utilidad())
                    continue  # Continuar con el siguiente nodo en el bucle
            elif padre_nodo_actual.get_padre().get_tipo() == 'MIN':
                if nodo_hoja_actual.get_valor_utilidad() < padre_nodo_actual.get_padre().get_valor_utilidad():
                    arreglo_nodos.append(nodo_hoja_actual)
                else:
                    se_poda = 'si'
                    padre_nodo_actual.set_valor_utilidad(nodo_hoja_actual.get_valor_utilidad())
                    continue  # Continuar con el siguiente nodo en el bucle

    return nodos_expandidos





