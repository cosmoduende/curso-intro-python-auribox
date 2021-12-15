
lenguajes = ["Python", "Kotlin", "Java", "JavaScript", "Go", "C++", "Ruby"]

for lenguaje in lenguajes:
    print(lenguaje)
    print(f"Estoy aprendiendo {lenguaje}")

# For que escribe números

for numero in range(0,20,2):
    print(numero)

# Crear rectángulo 

altura=20
anchura=10

for i in range(altura):
    for j in range(anchura):
        print("* ", end="")
    print()