import seleccion_elemento
import tablero

"""Aqui unimos todas las funciones."""

juegoTablero = tablero.creartablero(6)
tablero.imprimirtablero(juegoTablero)

seleccion_elemento.quitarelemento(tablero)
tablero.imprimirtablero(tablero)
