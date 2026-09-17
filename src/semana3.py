'''
validacion 1
esto me ayuda a identificar si el correo es valido o no, a la hora de registrarse.
'''

correo = "usuario@correo.com"

# Validar usando solo if
if "@" in correo and "." in correo:
    if correo.count("@") == 1:
        if not correo.startswith("@") and not correo.endswith("@"):
            print("El correo es potencialmente válido.")
        else:
            print("El correo no es válido.")
    else:
        print("El correo no es válido.")
else:
    print("El correo no es válido.")


'''
validacion 2
Esto me ayuda a identificar si el numero de identificacion es valido.
'''
identificacion = "123456"

if identificacion.isdigit() and 5 <= len(identificacion) <= 10:
    print("El número de identificación es válido.")
else:
    print("El número de identificación no es válido.")