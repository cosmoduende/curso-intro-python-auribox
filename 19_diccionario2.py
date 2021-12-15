
# Iniciar un diccionrio vacío

jugador = {}
print(jugador)

# Se une un jugador

jugador["nombre"] = "Saúl" 
jugador["puntaje"] = 0
print(jugador)

# Incrementando puntaje

jugador["puntaje"] = 100
print(jugador)

jugador["puntaje"] = 200
print(jugador)

# Acceder a un valor

print(jugador.get("consola", "No existe ese valor"))

# Iterar en el diccionario

for llave, valor in jugador.items():
    print(llave)
    print(valor)