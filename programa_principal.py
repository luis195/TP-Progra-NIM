import seleccion_elemento
import tablero
import utilidades
import presentacion



presentacion.imprimirTitulo()

CantidadFilas = utilidades.leerNumeros ('Ingrese la cantidad de filas que va tener el tablero: ')

juegoTablero = tablero.creartablero(CantidadFilas)
tablero.imprimirtablero(juegoTablero)
jugador1 = utilidades.leeJugador ('Ingrese el nombre del primer Jugador 1: ')
jugador2 = utilidades.leeJugador ('Ingrese el nombre del primer Jugador 2: ')
jugadorSiguiente = jugador1
while not (seleccion_elemento.hay_ganador(juegoTablero)):

    print("Jugador " + jugadorSiguiente + " es su turno")

    seleccion_elemento.quitarelemento(juegoTablero)
    tablero.imprimirtablero(juegoTablero)

    if seleccion_elemento.hay_ganador(juegoTablero):
        print("El Jugador " + jugadorSiguiente + " ha ganado")
    
    if (jugadorSiguiente == jugador1):
        jugadorSiguiente = jugador2
    else:
        jugadorSiguiente = jugador1

