"""CREA EL TABLERO DE JUEGO NIM """

import colores as paleta  # con el as se cambio el alias porque no podiamos dar el mismo nombre tablero, de esta manera lo diferenciamos del tablero


def creartablero(filas):
    """Crea el tablero del juego"""
    columnas = filas
    tablero = []
    for f in range(filas):
        tablero.append([])
        for c in range(columnas):
            tablero[f].append(' ')
    contadorFilas = 0
    while contadorFilas < len(tablero):
        contadorColumnas = 0
        while contadorColumnas <= contadorFilas:
            tablero[contadorFilas][contadorColumnas] = '|'
            contadorColumnas += 1
        contadorFilas += 1

    return tablero


def imprimirtablero(tablero):
    """Imprime el tablero de juego"""
    contadorLinea = 1 # Para imprimir los números de la fila
    for fila in tablero:
        print(paleta.colores["rojo"] + "%4s -->>" % contadorLinea, end="" + paleta.colores["reset"])
        for elemento in fila:
            if contadorLinea % 2 == 0 and contadorLinea % 3 != 0: # para que pueda intercambiarse los 3 colores
                print(paleta.colores["amarillo"] + "%4s" % elemento, end="" + paleta.colores["reset"])
            elif contadorLinea % 3 == 0:
                print(paleta.colores["magenta"] + "%4s" % elemento, end="" + paleta.colores["reset"])
            else:
                print(paleta.colores["cyan"] + "%4s" % elemento, end="" + paleta.colores["reset"])
        print()

        contadorLinea += 1


def obtener_cantidades_por_fila(tablero):
    '''Para ver la cantidad de palitos en cada fila en base al tablero y devuelve una lista'''
    resultado = []

    for fila in tablero:
        cantidad_en_fila = fila.count("|")
        resultado.append(cantidad_en_fila)

    return resultado
