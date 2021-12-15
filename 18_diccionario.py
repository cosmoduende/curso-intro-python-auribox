
# Creando un diccionario simple

cancion = {
    "artista" : "Metallica",  # Llave y valor
    "cancion" : "Enter Sadman",
    "lanzamiento" : 1992,
    "likes" : 3000 
}

# Acceder a los elementos del diccionario

artista = cancion["artista"]

print(f"Estoy escuchando a {artista}")

# Agregar nuevos valores

cancion["playlist"] = "Heavy Metal"
print(cancion)

# Reemplazar valor existente

cancion["cancion"] = "Unforgiven"
print(cancion)

# Eliminar valor existente

del cancion["lanzamiento"]
print(cancion)
