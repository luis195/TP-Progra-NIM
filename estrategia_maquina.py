"""Modulo de estrategia ganadora"""
import tablero


def a_binario(n):
    """Funcion recursiva para calcular decimal a binario"""
    if n == 0:
        return '0'
    else:
        return a_binario(n // 2) + str(n % 2)


# def nim_sum(arreglo):


def estrategia_ganadora(tablero):
    """Estrategia perfecta juego de maquina"""

    numeroElementos = 0
    arregloBinario = ['01', '010', '011', '0100', '0101', '0110']

    for fila in tablero:
        numeroElementos = fila.count('|')
        arregloBinario.append(a_binario(numeroElementos))

    return arregloBinario


tableroPrueba = tablero.creartablero(6)
cantidadElementos = estrategia_ganadora(tableroPrueba)
arreglo = ['01',
           '010',
           '011',
           '0100',
           '0101',
           '0110']
print(len(arreglo[5]))
