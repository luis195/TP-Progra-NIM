"""INDICA LOS MOVIMIENTOS DEL JUEGO """

import utilidades
import random
import estrategia_maquina
import tablero as modulo_tablero


def quitarelemento(tablero):
    """Elimna filas del tablero"""
    while True:
        try:
            # Para validar la seleccionar la fila
            filaSeleccion = utilidades.leerNumeros("Introduzca el número de la fila de donde desea eliminar elementos: ")

            assert filaSeleccion > 0 and filaSeleccion <= len(tablero), "El número de fila excede rangos del tablero"

            #Para validar la cantidad de elementos que se elimina sean los que quedaron en el tablero 
            numeroElementosEliminar = utilidades.leerNumeros("introduzca cuantos elementos desea eliminar de la fila: ")
            
            assert numeroElementosEliminar <= tablero[filaSeleccion - 1].count('|'), "La cantidad de elementos a eliminar debe" \
                                                                                      "   ser igual o menor a la cantidad de palitos existentes"

            posicionAborrar = tablero[filaSeleccion - 1].count('|') - 1
            while numeroElementosEliminar > 0:
                tablero[filaSeleccion - 1][posicionAborrar] = ' '
                numeroElementosEliminar -= 1
                posicionAborrar -= 1

            break
        except AssertionError as mensaje:
            print(mensaje)
            pass

    return tablero


def quitarelementoMaquina(tablero, dificultad, turno):
    """Elimna filas del tablero. Permite la selección de dificultad y la rotación de turno"""

    if dificultad == 1:  # CASO 1 (Fácil): La máquina mueve por valores random
        while True:
            # Selecciona la fila por azar
            filaSeleccion = random.randint(1, len(tablero))
            maxElementosEnFila = tablero[filaSeleccion - 1].count('|')
            if maxElementosEnFila == 0:
                continue
            # Selecciona los elementos al azar
            numeroElementosEliminar = random.randint(1, maxElementosEnFila)
            break
    elif dificultad == 2:  # CASO 2 (Intermedio): La máquina mueve mitad random y mitad estrategia ganadora
        # Si el turno es par se selecciona por azar la elección de la fila y cantidad de elementos a eliminar 
        if turno % 2 == 0:
            while True:
                filaSeleccion = random.randint(1, len(tablero))
                maxElementosEnFila = tablero[filaSeleccion - 1].count('|')
                if maxElementosEnFila == 0:
                    continue
                numeroElementosEliminar = random.randint(1, maxElementosEnFila)
                break
        else:
            cantidades_por_fila_tablero = modulo_tablero.obtener_cantidades_por_fila(tablero)
            tupla_ganadora = estrategia_maquina.estrategia_ganadora(cantidades_por_fila_tablero)
            filaSeleccion = tupla_ganadora[0] + 1
            numeroElementosEliminar = tupla_ganadora[1]

    elif dificultad == 3:  # CASO 3 (Dificil): La maquina mueve en base a la estrategia ganadora de NIM
        cantidades_por_fila_tablero = modulo_tablero.obtener_cantidades_por_fila(tablero)
        tupla_ganadora = estrategia_maquina.estrategia_ganadora(cantidades_por_fila_tablero)
        filaSeleccion = tupla_ganadora[0] + 1
        numeroElementosEliminar = tupla_ganadora[1]

    posicionAborrar = tablero[filaSeleccion - 1].count('|') - 1
    while numeroElementosEliminar > 0:
        tablero[filaSeleccion - 1][posicionAborrar] = ' '
        numeroElementosEliminar -= 1
        posicionAborrar -= 1
    return tablero


def hay_ganador(tablero):
    """Indica quien se quedo con el último elemento"""
    fila = 0
    hayGanador = False
    cantidadElementos = 0
    while fila < len(tablero):
        columna = 0
        while columna <= fila:
            if tablero[fila][columna] == '|':
                cantidadElementos = cantidadElementos + 1
            columna = columna + 1
        fila = fila + 1
    if cantidadElementos <= 1:
        hayGanador = True
    return hayGanador
