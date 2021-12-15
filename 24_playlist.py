
playlist = {} # Diccionario vacío
playlist["canciones"] = [] # Lista vacía de canciones

# Función principal

def app():
    # Agregar playlist

    agregar_playlist = True

    while agregar_playlist:
        nombre_playlist = input("Cómo deseas nombrar la playlist? \r\n")

        if nombre_playlist:
            playlist["nombre"] = nombre_playlist

            # Ya tenemos un nombre, desactivar el True para terminar while
            agregar_playlist = False
            print(playlist)

            agregar_canciones()

def agregar_canciones():
    # Bandera para agregar canciones
    agregar_cancion = True
    
    while agregar_cancion:
        # Preguntar al usuario qué canción agregar
        nombre_playlist = playlist["nombre"]
        pregunta = f"Agrega canciones para la playlist {nombre_playlist}: \r\n"
        pregunta += "Escribe X para dejar de agregar canciones \r\n"

        cancion = input(pregunta)

        if cancion == "X":
            # Dejar de agregar canciones
            print("Finalizando...")
            agregar_cancion = False
            # Mostrar resumen de la playlist
            mostrar_resumen()
        else:
            # Agregar canciones a playlist
            playlist["canciones"].append(cancion)
            print(playlist)

def mostrar_resumen():
    nombre_playlist = playlist["nombre"]
    print("Mostrando resumen...")
    print(f"Playlist: {nombre_playlist} \r\n")
    print("Canciones: \r\n")
    for cancion in playlist["canciones"]:
        print(cancion)

app()