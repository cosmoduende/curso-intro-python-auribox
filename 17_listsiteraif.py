
lenguajes = ["Python", "Kotlin", "Java", "JavaScript"]

for lenguaje in lenguajes:
    if lenguaje == "Python":
        print(lenguaje.upper())
    elif lenguaje == "Java":
        print(lenguaje.center(25, "*"))
    else:
        print(lenguaje.swapcase())