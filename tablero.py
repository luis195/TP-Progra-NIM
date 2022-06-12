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
            if tablero.index(fila) % 2 == 0 and tablero.index(fila) % 3 != 0:
                print(paleta.colores["amarillo"] + "%4s" % elemento, end="" + paleta.colores["reset"])
            elif tablero.index(fila) % 3 == 0:
                print(paleta.colores["magenta"] + "%4s" % elemento, end="" + paleta.colores["reset"])
            else:
                print(paleta.colores["cyan"] + "%4s" % elemento, end="" + paleta.colores["reset"])
        print()

        contadorLinea += 1


def obtener_cantidades_por_fila(tablero):
    resultado = []

    for fila in tablero:
        cantidad_en_fila = fila.count("|")
        resultado.append(cantidad_en_fila)

    return resultado
