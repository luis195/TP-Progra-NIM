"""Modulo de estrategia ganadora"""
import tablero


def suma_nim(cantidades_por_fila_tablero):
    """Suma de los resultados con el operador Xor"""
    resultado = -1

    if len(cantidades_por_fila_tablero) == 1:
        return cantidades_por_fila_tablero[0]
    else:
        resultado_xor = cantidades_por_fila_tablero[0] ^ cantidades_por_fila_tablero[1]
        cantidades_por_fila_tablero = cantidades_por_fila_tablero[2:] 
        cantidades_por_fila_tablero.insert(0, resultado_xor)
        resultado = suma_nim(cantidades_por_fila_tablero)

    return resultado


def estrategia_ganadora(cantidades_por_fila_tablero):
    """Calcula la proxima jugada para Nim en base a la estrategia ganadora.

    Si hay una jugada ganadora:
        Devuelve una tupla con el índice del tablero y la cantidad de fichas a eliminar (indice_fila_tablero, cantidad_a_eliminar)
    else:
        Devuelve una tupla con el índice del tablero con mayor elementos y 1 como elementos a eliminar esperando a que el otro jugador equivoque la estrategia ganadora

    """

    es_casi_final_del_juego = False
    contador_mayores_1 = sum(1 for x in cantidades_por_fila_tablero if x > 1)  # mientras haya mas de un palito por fila
    es_casi_final_del_juego = (contador_mayores_1 <= 1)

    # La suma nim devolverá la jugada correcta para
    # forzar al oponente a realizar la última movida
    if es_casi_final_del_juego:
        movidas_restantes = sum(1 for x in cantidades_por_fila_tablero if x > 0)
        es_impar = (movidas_restantes % 2 == 1)
        tamano_max = max(cantidades_por_fila_tablero)
        indice_del_elemento_max = cantidades_por_fila_tablero.index(tamano_max)

        if tamano_max == 1 and es_impar:
            return indice_del_elemento_max, 1  # No hay mejor jugada y se perderá la partida

        # Reduce el juego a un elemento impar de 1s
        return indice_del_elemento_max, tamano_max - int(es_impar)

    resultado_suma_nim = suma_nim(cantidades_por_fila_tablero)
    if resultado_suma_nim == 0:
        tamano_max = max(cantidades_por_fila_tablero)
        indice_del_elemento_max = cantidades_por_fila_tablero.index(tamano_max)
        return indice_del_elemento_max, 1  # No hay mejor jugada y se perderá la partida

    # Calcular qué movida realizar
    for indice, cantidad_en_fila in enumerate(cantidades_por_fila_tablero):
        tamano = cantidad_en_fila ^ resultado_suma_nim
        if tamano < cantidad_en_fila:
            cantidad_a_eliminar = cantidad_en_fila - tamano
            return indice, cantidad_a_eliminar
