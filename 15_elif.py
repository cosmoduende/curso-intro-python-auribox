
# Ejemplo con elif

ocupacion = "Estudiante"
monto_a_pagar = 500

if ocupacion == "Estudiante":
    print("Tienes el 50% de descuento")
    print(f"Debes pagar ${monto_a_pagar*.50}")
elif ocupacion == "Jubilado":
    print("Tienes 75% de descuento")
    print(f"Debes pagar ${monto_a_pagar*.75}")
elif ocupacion == "Desempleado":
    print("Tienes un 10% de descuento")
    print(f"Debes pagar ${monto_a_pagar*.10}")
else:
    print("Debes pagar el 100%")
    print(f"Debes pagar ${monto_a_pagar}")
