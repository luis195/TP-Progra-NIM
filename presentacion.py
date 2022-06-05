__MODO_HUMANO_HUMANO__ = 1
__MODO_HUMANO_MAQUINA__ = 2
__NOMBRE_MAQUINA__ = "MAQUINA"


def imprimirTitulo ():

    titulo = "JUEGO DE NIM"
    titulo1 = titulo.center(65, "=")
    print(titulo1)
    print ('')
    print('Descripción del Juego:')
    print ('')
    print ('Es un juego matemático de estrategia en el que dos jugadores se turnan para quitar objetos de distintos filas.')
    print ('En cada turno, un jugador debe eliminar al menos un objeto.')
    print ('Se puede eliminar cualquier número de objetos siempre que todos provengan de la misma fila.')
    print('Generalmente el jugador que comienza primero es el ganador.')
    print('Se basa en estrategias matemáticas.')
    print('El jugador que toma el último objeto es el que pierde.')
    print ('¡Que comience el juego!')
    print ('')
    print ('')
    
    

def seleccionContricante ():

    contricante = "Contra quién quieres jugar"
    contricante1 = contricante.center(70, "=")
    print(contricante1)
    print ("1.- Contra otro jugador / 2.-  Contra la máquina ")
    numero = -1
    while True:
        try:
            numero= int (input ('Seleccione contra quién va jugar: '))
        
            assert numero ==1 or numero ==2
            break
        except (ValueError, AssertionError) as e:
            print ('Debe ingresar la opción 1 o 2')
            intento= input ('Desea Ingresar otra vez: S/N:')
            if intento.upper ()=='N':
                pass
            
    return numero