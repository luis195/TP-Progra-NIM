'''Módulo para el manejo del archivo de ranking con los jugadores y sus puntajes.'''
__tablaRankings__ = [] # Lista de listas. Cada posición tiene una lista donde cada elemento contiene: 0 - Nombre Jugador y en 1 - Ranking de ese jugador

def cargar_rankings():
    try:
        archivoRankings = open("rankings.txt", "rt")
        __tablaRankings__.clear()
        for linea in archivoRankings:
            linea = linea.rstrip("\n")
            linea = linea.replace(" ", "")
            
            if (linea == ""):
                continue

            registroRanking = linea.split(";")
            registroRanking[1] = int(registroRanking[1]) 
            __tablaRankings__.append(registroRanking)
        
    except:
        print("Error")
    finally:

        archivoRankings.close()

def grabar_rankings():
    archivoRankings = None
    try:
        assert len(__tablaRankings__) > 0

        archivoRankings = open("rankings.txt", "wt") # Sobrescribe el archivo de rankings
        
        for registroRanking in __tablaRankings__:
            linea = registroRanking[0] + ";" + str(registroRanking[1]) + "\n"
            archivoRankings.write(linea)
    except:
        print("Error")
    finally:
        if archivoRankings:
            archivoRankings.close()

def actualizar_ranking_jugador(nombre_jugador, nuevo_ranking):
    try:
        assert nuevo_ranking >= 0
        nuevoGanador = True
        for i in range (len(__tablaRankings__)):
            if __tablaRankings__[i][0] == nombre_jugador:
                __tablaRankings__[i][1] = nuevo_ranking
                nuevoGanador = False
                break

        if nuevoGanador:
            registroNuevo = []
            registroNuevo.append(nombre_jugador)
            registroNuevo.append("1")
            __tablaRankings__.append(registroNuevo)
    except:
        print ("ERROR: El nuevo ranking tiene que ser mayor o igual a 0.")

def obtener_ranking_jugador(nombre_jugador):
    resultado = -1
    for jugador in __tablaRankings__:
        if jugador[0] == nombre_jugador:
            resultado = jugador[1]
            break

    return resultado

def imprimir_ranking():
    print("Listado de rankings")
    for jugador in __tablaRankings__:
        print(jugador[0] + "  " + str(jugador[1]))


''' Test unitarios


cargar_rankings()

imprimir_ranking()

ranking = obtener_ranking_jugador("Juan")
print("El ranking de Juan es: ", ranking)

ranking += 1

actualizar_ranking_jugador("Juan", ranking)

imprimir_ranking()

grabar_rankings()

cargar_rankings()

imprimir_ranking()
'''