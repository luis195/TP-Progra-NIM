"""Módulo para el manejo del archivo de ranking con los jugadores y sus puntajes."""


def cargar_rankings():
    try:
        archivoRankings = open("rankings.txt", "rt")
        tablaRankings = []  # Lista de listas. Cada posición tiene una lista donde cada elemento contiene: 0 - Nombre
        # Jugador y en 1 - Ranking de ese jugador
        for linea in archivoRankings:
            linea = linea.rstrip("\n")
            linea = linea.replace(" ", "")

            if linea == "":
                continue

            registroRanking = linea.split(";")
            registroRanking[1] = int(registroRanking[1])
            tablaRankings.append(registroRanking)
        return tablaRankings

    except:
        print("Error")
    finally:
        try:
            archivoRankings.close()
        except NameError:
            pass


def grabar_rankings(tablaRankings):
    archivoRankings = None
    try:
        assert len(tablaRankings) > 0

        archivoRankings = open("rankings.txt", "wt")  # Sobrescribe el archivo de rankings

        for registroRanking in tablaRankings:
            linea = registroRanking[0] + ";" + str(registroRanking[1]) + "\n"
            archivoRankings.write(linea)
    except:
        print("Error")
    finally:
        if archivoRankings:
            archivoRankings.close()


def actualizar_ranking_jugador(nombre_jugador, nuevo_ranking, tablaRankings):
    try:
        assert nuevo_ranking >= 0
        nuevoGanador = True
        for i in range(len(tablaRankings)):
            if tablaRankings[i][0] == nombre_jugador:
                tablaRankings[i][1] = nuevo_ranking
                nuevoGanador = False
                break

        if nuevoGanador:
            registroNuevo = []
            registroNuevo.append(nombre_jugador)
            registroNuevo.append("1")
            tablaRankings.append(registroNuevo)
    except:
        print("ERROR: El nuevo ranking tiene que ser mayor o igual a 0.")


def obtener_ranking_jugador(nombre_jugador, tablaRankings):
    resultado = -1
    for jugador in tablaRankings:
        if jugador[0] == nombre_jugador:
            resultado = jugador[1]
            break

    return resultado


def imprimir_ranking(tablaRankings):
    print("Listado de rankings")
    for jugador in tablaRankings:
        print(jugador[0] + "  " + str(jugador[1]))


''' Test unitarios


tablaRankings = cargar_rankings()

imprimir_ranking(tablaRankings)

ranking = obtener_ranking_jugador("Juan", tablaRankings)
print("El ranking de Juan es: ", ranking)

ranking += 1

actualizar_ranking_jugador("Juan", ranking, tablaRankings)

imprimir_ranking(tablaRankings)

grabar_rankings(tablaRankings)

tablaRankings = cargar_rankings()

imprimir_ranking(tablaRankings)
'''
