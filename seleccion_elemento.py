'''INDICA LOS MOVIMIENTOS DEL JUEGO '''

import utilidades


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
    if cantidadElementos == 1:
        hayGanador = True
    return hayGanador

