
lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

print(lenguajes)

# Elegimos el primer elemento de la lista

print(lenguajes[0])

# Ordenamos alfabéticamente

lenguajes.sort()
print(lenguajes)

# Acceder a un elemento dentro de un texto

aprendiendo = f"EStoy aprendiendo {lenguajes[3]}"
print(aprendiendo)

# Modificar un elemento de un List

lenguajes[2] = 'PHP'
print(lenguajes)

# Agregar elementos a un List

lenguajes.append('Ruby')
print(lenguajes)

#Eliminar elemento de un List

del lenguajes[1]
print(lenguajes)

# Elimina el último elemento

lenguajes.pop() 
print(lenguajes)

# Elimina elemento de una posición

lenguajes.pop(0) 
print(lenguajes)

# Eliminar elemento por nombre

lenguajes.remove("PHP")
print(lenguajes)