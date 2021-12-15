
# Evaluar elemento de una lista

lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

if "PHP" in lenguajes:
    print("PHP si existe en la lista")
else:
    print("PHP no existe en la lista")


# If anidados

usuario_autenticado = True
usuario_admin = True

if usuario_autenticado:
    if usuario_admin:
        print("ACCESO TOTAL")
    else:
        print("Acceso al sistema")
else:
    print("Inicia sesión primero")