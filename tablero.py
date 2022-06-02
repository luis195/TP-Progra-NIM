def creartablero(filas):
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
    for fila in tablero:
        for elemento in fila:
            print("%4s" % elemento, end="")
        print()


tab = creartablero(6)
imprimirtablero(tab)


