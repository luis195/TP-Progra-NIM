'''INGRESO DE DATOS '''

def leerNumeros (mensaje):
    """Ingresa números positivos"""
    while True:
        try:
            nro= int (input (mensaje))
            
            assert nro > 0 
            break
                   
        except ValueError:
            print ('Dato invalido, solo puede ingresarse números')
            intento= input ('Desea ingresarlo otra vez? (S/N): ')
            if intento.upper()== "N":
                print("Saliste del Juego")
                print(quit())
        except AssertionError:
            print ('El número debe ser mayor a cero')
            
    return nro


def leeJugador (mensaje):
    """Ingresa el nombre de los jugadores"""
    
    while True:
        try:
            jugador= input (mensaje)
            assert jugador.isalpha ()
            break
               
        except AssertionError:
            print ('Dato invalido, solo puede ingresarse letras')
            
            
    return jugador
    