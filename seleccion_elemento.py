'''INDICA LOS MOVIMIENTOS DEL JUEGO '''

import utilidades
import random


def quitarelemento(tablero):
    """Elimna filas del tablero"""
    filaSeleccion = utilidades.leerNumeros("Introdzca el número de la fila de donde desea eliminar elementos: ")
    numeroElementosEliminar = utilidades.leerNumeros("introduzca cuantos elementos desea eliminar de la fila: ")

    posicionAborrar = tablero[filaSeleccion - 1].count('|') - 1
    while numeroElementosEliminar > 0:
        tablero[filaSeleccion - 1][posicionAborrar] = ' '
        numeroElementosEliminar -=  1
        posicionAborrar -= 1
    return tablero

def quitarelementoMaquina(tablero, dificultad):
    """Elimna filas del tablero"""

    if dificultad == 1: # CASO 1 (Facil): La máquina mueve por valores random
        while True:
            filaSeleccion = random.randint(1,len(tablero))
            maxElementosEnFila = tablero[filaSeleccion - 1].count('|')
            if maxElementosEnFila == 0:
                continue
            numeroElementosEliminar = random.randint(1,maxElementosEnFila)
            break
    elif dificultad == 2: # CASO 2 (Intermedio): La máquina mueve mitad random y mitad ???
        while True:
            filaSeleccion = random.randint(1,len(tablero))
            maxElementosEnFila = tablero[filaSeleccion - 1].count('|')
            if maxElementosEnFila == 0:
                continue
            numeroElementosEliminar = random.randint(1,maxElementosEnFila)
            break
    elif dificultad == 3: # CASO 3 (Dificil): La maquina mueve en base a ???
        while True:
            filaSeleccion = random.randint(1,len(tablero))
            maxElementosEnFila = tablero[filaSeleccion - 1].count('|')
            if maxElementosEnFila == 0:
                continue
            numeroElementosEliminar = random.randint(1,maxElementosEnFila)
            break

    posicionAborrar = tablero[filaSeleccion - 1].count('|') - 1
    while numeroElementosEliminar > 0:
        tablero[filaSeleccion - 1][posicionAborrar] = ' '
        numeroElementosEliminar -=  1
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

