# Son varialbles globales ya que se va utilizar en todo el programa 
__MODO_HUMANO_HUMANO__ = 1
__MODO_HUMANO_MAQUINA__ = 2
__NOMBRE_MAQUINA__ = "MAQUINA"


def imprimirTitulo():
    '''Imprime las pautas del juego'''
    titulo = "JUEGO DE NIM"
    titulo1 = titulo.center(65, "=")
    print(titulo1)
    print('')
    print('Descripción del Juego:')
    print('')
    print('Es un juego para 2 personas y se juega por turnos.')
    print('En cada turno, un jugador debe eliminar al menos un objeto.')
    print('Se puede eliminar cualquier número de objetos siempre que todos provengan de la misma fila.')
    print('Generalmente el jugador que comienza primero es el ganador.')
    print('Se basa en estrategias matemáticas.')
    print('El jugador que toma el último objeto es el que pierde.')
    print()
    print('¡Que comience el juego!')
    print('')
    print('')


def seleccionContricante():
    """Permite la selección del contricante humano o máquina"""
    contricante = "CONTRA QUIEN VA JUGAR"
    contricante1 = contricante.center(70, "=")
    print(contricante1)
    print('')
    print("1.- Contra otro jugador / 2.-  Contra la máquina ")
    print('')

    
    while True:
        try:
            numero = int(input('Seleccione contra quién va jugar: '))

            assert numero == 1 or numero == 2
            break
        except ValueError:
            print ('Dato invalido, solo puede ingresarse números')
           
        except AssertionError: 
            print('Debe ingresar la opción 1 o 2')
            

    return numero
