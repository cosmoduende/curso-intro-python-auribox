
# Las entradas de datos siempre van a venir por default como string

nombre = input("Cuál es tu nombre? \r\n")
print(f"Hola {nombre}")

edad = input("Cuál es tu edad? \r\n")

# Convertir input por defecto string a int

edad = int(edad)

if edad>=18:
    print("Ya puedes votar")
    if edad>=22:
        print("Además tienes edad para beber en EU")
else:
    print("Aún no puedes votar")

# Mezclando con operadores

numero = input("Agrega un número y te diré si es par o non \r\n")

numero = int(numero)

if numero % 2 == 0:  # Usar módulo es obtener el residuo de la división de dos numeros, por ejemplo
    print(f"el número {numero} es par") # 9 % 2 = 1 porque 9/2 es 4.5, la suma de .5 más .5 es 1
else:
    print(f"el número {numero} es impar")
