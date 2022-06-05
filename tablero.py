'''CREA EL TABLERO DE JUEGO NIM '''


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
        print("%4s -->>" % contadorLinea, end="")
        for elemento in fila:
            print("%4s" % elemento, end="")
        print()
        
        contadorLinea += 1




