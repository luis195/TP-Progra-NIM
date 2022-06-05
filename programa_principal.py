import seleccion_elemento
import tablero

print ('')
titulo = "JUEGO DE NIM"
titulo1 = titulo.center(70, "=")
print(titulo1)
print ('')
print ('')

print('Descripción del Juego:')
print ('')
print('1. El jugador que comienza primero generalmente es el ganador, solo si utiliza estrategias.')
print('2. Necesita dos jugadores.')
print('3. Se basa en estrategias matemáticas.')
print('4. El último jugador que extrae las pilas pierde.')

print('Nim es un juego matemático de estrategia en el que dos jugadores se turnan para quitar objetos de distintos filas.\n Es un juego increible' )

print ('')
print ('')


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
