import seleccion_elemento
import tablero


titulo = "JUEGO DE NIM"
titulo1 = titulo.center(60, "=")
print(titulo1)

print('Este juego depende de dos factores:')
print('1.	El jugador que comienza primero, generalmente gana si hace uso de estrategias.')
print('2.	La configuración inicial de las pilas / montones.')
print('Necesita dos jugadores.\n Se basa en estrategias matemáticas o estrategias ganadoras.\n El último jugador que '
      'extrae las pilas pierde.')

"""Aqui unimos todas las funciones."""

def leerNumeros (mensaje):
    while True:
        try:
            nro= int (input (mensaje))
            
            assert nro >= 0 
            break
                   
        except ValueError:
            print ('Dato invalido, solo puede ingresarse números')
            intento= input ('Desea ingresarlo otra vez? (S/N): ')
            if intento.upper()== "N":
                pass
        except AssertionError:
            print ('El número debe ser mayor a cero')
            
    return nro



CantidadFilas = leerNumeros ('Ingrese la cantidad de filas que va tener el tablero: ')

juegoTablero = tablero.creartablero(CantidadFilas)
tablero.imprimirtablero(juegoTablero)
jugador = 1

while not (seleccion_elemento.hay_ganador(juegoTablero)):

    print("Jugador " + str(jugador) + " es su turno")

    seleccion_elemento.quitarelemento(juegoTablero)
    tablero.imprimirtablero(juegoTablero)

    if seleccion_elemento.hay_ganador(juegoTablero):
        print("El Jugador " + str(jugador) + " ha ganado")
    else:
        jugador = 2
