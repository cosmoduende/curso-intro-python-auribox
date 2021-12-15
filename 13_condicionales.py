
# If simple

balance = 500
if balance>401:
    print("Puedes pagar el producto")

# If else

balance = 0
if balance>0:
    print("Puedes pagar")
else:
    print("No tienes saldo")


likes = 200
if likes >= 200:
    print("Tu publicación en FB es popular")
else:
    print("Tu publicación aún no es popular")



# Caso particular con booleanos no se usa operador "==", se añade inmediato la variable

usuario_autenticado = True
if usuario_autenticado:
    print("Acceso al sistema")
else:
    print("Inicia sesión primero")