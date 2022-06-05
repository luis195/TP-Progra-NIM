def leerNumeros(mensaje):
    while True:
        try:
            nro = int(input(mensaje))
            break
                   
        except ValueError:
            print('Dato invalido')
            print('Intentelo de nuevo')

    return nro


def quitarelemento(tablero):
    filaSeleccion = leerNumeros("Introdzca el número de la fila de donde desea eliminar elementos: \n")
    numeroElementosEliminar = leerNumeros("introduzca cuantos elementos desea eliminar de la fila: \n")

    tablero[filaSeleccion - 1].count('|') - 1

    while numeroElementosEliminar > 0:
        tablero[filaSeleccion - 1][numeroElementosEliminar - 1] = ' '
        numeroElementosEliminar = numeroElementosEliminar - 1
    return tablero


def hay_ganador(tablero):
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

