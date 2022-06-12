import seleccion_elemento
import tablero
import utilidades
import presentacion
import ranking

tablaRankings = ranking.cargar_rankings()

presentacion.imprimirTitulo()

modoJugadores = presentacion.seleccionContricante()

CantidadFilas = utilidades.leerNumeros('Ingrese la cantidad de filas que va tener el tablero: ')

juegoTablero = tablero.creartablero(CantidadFilas)
tablero.imprimirtablero(juegoTablero)

dificultad_modo_maquina = -1  # inicializar la variable en algo diferente de los niveles

if modoJugadores == presentacion.__MODO_HUMANO_HUMANO__:
    jugador1 = utilidades.leeJugador('Ingrese el nombre del primer Jugador: ')
    jugador2 = utilidades.leeJugador('Ingrese el nombre del segundo Jugador: ')
else:
    jugador1 = presentacion.__NOMBRE_MAQUINA__
    dificultad_modo_maquina = utilidades.leerNumeros('Ingrese el nivel de dificultad deseado (1-Facil | 2-Intermedio '
                                                     '| 3-Dificil): ')
    while dificultad_modo_maquina < 0 or dificultad_modo_maquina > 3:
        print('La opciones elegidas deben estar entre 1 a 3')
        dificultad_modo_maquina = utilidades.leerNumeros('Ingrese el nivel de dificultad deseado (1-Facil | '
                                                         '2-Intermedio | 3-Dificil): ')

    jugador2 = utilidades.leeJugador('Ingrese el nombre del Segundo Jugador: ')

jugadorSiguiente = jugador1
turno = 0
while not (seleccion_elemento.hay_ganador(juegoTablero)):

    print("Jugador " + jugadorSiguiente + " es su turno")

    if jugadorSiguiente == presentacion.__NOMBRE_MAQUINA__:
        turno = turno + 1
        seleccion_elemento.quitarelementoMaquina(juegoTablero, dificultad_modo_maquina, turno)
    else:
        seleccion_elemento.quitarelemento(juegoTablero)
    tablero.imprimirtablero(juegoTablero)

    if seleccion_elemento.hay_ganador(juegoTablero):
        break

    if jugadorSiguiente == jugador1:
        jugadorSiguiente = jugador2
    else:
        jugadorSiguiente = jugador1

print("El Jugador " + jugadorSiguiente + " ha ganado")

rankingGanador = ranking.obtener_ranking_jugador(jugadorSiguiente, tablaRankings)

rankingGanador += 1

ranking.actualizar_ranking_jugador(jugadorSiguiente, rankingGanador, tablaRankings)

ranking.grabar_rankings(tablaRankings)

ranking.imprimir_ranking(tablaRankings)
