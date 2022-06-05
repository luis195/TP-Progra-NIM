import seleccion_elemento
import tablero
import utilidades
import presentacion
import ranking

ranking.cargar_rankings()

presentacion.imprimirTitulo()

modoJugadores = presentacion.seleccionContricante()

CantidadFilas = utilidades.leerNumeros ('Ingrese la cantidad de filas que va tener el tablero: ')

juegoTablero = tablero.creartablero(CantidadFilas)
tablero.imprimirtablero(juegoTablero)

if (modoJugadores == presentacion.__MODO_HUMANO_HUMANO__):
    jugador1 = utilidades.leeJugador ('Ingrese el nombre del primer Jugador 1: ')
    jugador2 = utilidades.leeJugador ('Ingrese el nombre del primer Jugador 2: ')
else:
    jugador1 = presentacion.__NOMBRE_MAQUINA__
    jugador2 = utilidades.leeJugador ('Ingrese el nombre del primer Jugador 2: ')

jugadorSiguiente = jugador1
while not (seleccion_elemento.hay_ganador(juegoTablero)):

    print("Jugador " + jugadorSiguiente + " es su turno")

    seleccion_elemento.quitarelemento(juegoTablero)
    tablero.imprimirtablero(juegoTablero)

    if seleccion_elemento.hay_ganador(juegoTablero):
        break
    
    if (jugadorSiguiente == jugador1):
        jugadorSiguiente = jugador2
    else:
        jugadorSiguiente = jugador1

print("El Jugador " + jugadorSiguiente + " ha ganado")

rankingGanador = ranking.obtener_ranking_jugador(jugadorSiguiente)

rankingGanador += 1

ranking.actualizar_ranking_jugador(jugadorSiguiente, rankingGanador)

ranking.grabar_rankings()

ranking.imprimir_ranking()