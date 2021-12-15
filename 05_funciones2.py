
# Ojo, hay que añadir siempre precediendo la letra f para relacionar una variable con un string correctamente

def informacion(nombre):
    print(f"Soy {nombre}")

informacion("Saul")
informacion("Pedro")
informacion("Juan")

# Probando con más de un parámetro

def informacionCompleta(nombre, puesto):
    print(f"Soy {nombre} y soy {puesto}")

informacionCompleta("Saul", "Programador")
informacionCompleta("Pedro", "Diseñador")
informacionCompleta("Juan", "Nini")


# Probando con un parámetro desconocido

def informacionCompleta(nombre, puesto="Desconocido"):
    print(f"Soy {nombre} y soy {puesto}")

informacionCompleta("Saul", "Programador")
informacionCompleta("Pedro", "Diseñador")
informacionCompleta("Juan")
