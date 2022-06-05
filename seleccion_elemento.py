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

def leeJugador (mensaje):
    while True:
        try:
            jugador= input (mensaje)
            assert jugador.isalpha ()
            break
        except ValueError:
            print ('Dato invalido, solo puede ingresarse letras')
            intento= input ('Desea ingresarlo otra vez? (S/N): ')
            if intento.upper()== "N":
                pass
        except AssertionError:
            print ('Solo se permiten letras')
            
    return jugador

def rankingDelJugador ():
    try:
        archivo= open ('Ranking.txt', 'wt')

        contador= 1
        jugador= leeJugador ('Ingrese el nombre del Primer jugador:')

        while contador < 2:
            archivo.write (jugador + '\n')
            jugador= leeJugador ('Ingrese el nombre del Segundo jugador:')
            contador += 1
                        
    
        print ('El archivo se grabo correctamente')
        
    except OSError as mensaje:
        print ('No se puede grabar el archivo', mensaje)
    finally:
        try:
            archivo.close ()
        except NameError:
            pass




        




def quitarelemento(tablero):
    filaSeleccion = leerNumeros("Introdzca el número de la fila de donde desea eliminar elementos: \n")
    numeroElementosEliminar = leerNumeros("introduzca cuantos elementos desea eliminar de la fila: \n")

    tablero[filaSeleccion - 1].count('|') - 1

    while numeroElementosEliminar > 0:
        tablero[filaSeleccion - 1][numeroElementosEliminar - 1] = ' '
        numeroElementosEliminar = numeroElementosEliminar - 1
    return tablero


def hay_ganador(tablero):
    fila = 0
    hayGanador = False
    cantidadElementos = 0
    while fila < len(tablero):
        columna = 0
        while columna <= fila:
            if tablero[fila][columna] == '|':
                cantidadElementos = cantidadElementos + 1
            columna = columna + 1
        fila = fila + 1
    if cantidadElementos == 1:
        hayGanador = True
    return hayGanador

