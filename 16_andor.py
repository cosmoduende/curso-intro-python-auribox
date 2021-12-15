
# Operadores and y or

usuario_logueado = True
usuario_admin = True
usuario_editor = False
usuario_redactor = False

if usuario_logueado and usuario_admin:
    print("Acceso al sistema como Administrador")
elif usuario_logueado:
    print("Acceso al sistema como usuario normal")
    if usuario_editor or usuario_redactor:
        print("Acceso al sistema con permisos de edición")
else:
    print("Debes iniciar sesión")