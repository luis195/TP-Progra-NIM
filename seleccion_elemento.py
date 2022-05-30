def quitarelemento(tablero):

    filaSeleccion = int(input("Introdzca el numero de la fila de donde desea eliminar elementos: \n"))
    numeroElementosEliminar = int(input("introduzca cuantos elementos desea eliminar de la fila: \n"))
    tablero[filaSeleccion - 1].count('|') - 1

    while numeroElementosEliminar > 0:
        tablero[filaSeleccion - 1][numeroElementosEliminar - 1] = ' '
        numeroElementosEliminar = numeroElementosEliminar - 1
    return tablero


