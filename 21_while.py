

pregunta = "Agrega un número y te diré si es par o non \r\n"
pregunta += "(Escribe CERRAR para salir de la aplicación) \r\n"

preguntar = True

while preguntar:

    # Mezclando con operadores

    numero = input(pregunta)

    if numero == "CERRAR":
        preguntar = False
    else:
        numero = int(numero)
        if numero % 2 == 0:  # Usar módulo es obtener el residuo de la división de dos numeros, por ejemplo
            print(f"el número {numero} es par") # 9 % 2 = 1 porque 9/2 es 4.5, la suma de .5 más .5 es 1
        else:
            print(f"el número {numero} es impar")
