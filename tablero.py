"""CREA EL TABLERO DE JUEGO NIM """

import colores as paleta


def creartablero(filas):
    """Crea el tablero del juego"""
    columnas = filas
    tablero = []
    for f in range(filas):
        tablero.append([])
        for c in range(columnas):
            tablero[f].append(' ')
    p = 0
    while p < len(tablero):
        q = 0
        while q <= p:
            tablero[p][q] = '|'
            q = q + 1
        p = p + 1

    return tablero


def imprimirtablero(tablero):
    """Imprime el tablero de juego"""
    contadorLinea = 1
    for fila in tablero:
        print(paleta.colores["rojo"] + "%4s -->>" % contadorLinea, end="" + paleta.colores["reset"])
        for elemento in fila:
            if fila.count("|") % 2 == 0 and fila.count("|") % 3 != 0:
                print(paleta.colores["amarillo"] + "%4s" % elemento, end="" + paleta.colores["reset"])
            elif fila.count("|") % 3 == 0:
                print(paleta.colores["magenta"] + "%4s" % elemento, end="" + paleta.colores["reset"])
            else:
                print(paleta.colores["cyan"] + "%4s" % elemento, end="" + paleta.colores["reset"])
        print()

        contadorLinea += 1
