# Validacion Match-case
nivel_de_educacion = 2
match nivel_de_educacion:
    case 5:
        print("Educacion superior")
    case 4:
        print("Nivel de educación bueno")
    case 3:
      print("Nivel de educación regular")
    case 2:
        print("Nivel de educación bajo")
    case 1:
        print("Nivel de educación muy bajo")
    case n if n <= 0:
        print("Ingrese un valor entre 1 y 5")
    case _:
        print("Nivel de educación desconocido")
        
        
   # Validacion Match-case 2 
def categorize_age(age):
    match age:
        case _ if age < 0:
            return "Edad inválida"
        case _ if 0 <= age <= 12:
            return "Niño"
        case _ if 13 <= age <= 17:
            return "Adolescente"
        case _ if 18 <= age <= 64:
            return "Adulto"
        case _ if age >= 65:
            return "Adulto mayor"

# Ejemplos de uso
print(f"La edad 5 es: {categorize_age(5)}")
print(f"La edad 15 es: {categorize_age(15)}")
print(f"La edad 30 es: {categorize_age(30)}")
print(f"La edad 70 es: {categorize_age(70)}")
print(f"La edad -2 es: {categorize_age(-2)}")


# EJEMPLO ANGEL

# Solicitamos al usuario que ingrese su género
genero = input("Por favor, ingresa tu género (Masculino / Femenino): ")

# Limpiamos espacios en blanco y convertimos el texto a minúsculas para facilitar la validación
genero_limpio = genero.strip().lower()

# Realizamos las validaciones con if
if genero_limpio == "masculino":
    print("El género validado es: Masculino.")
elif genero_limpio == "femenino":
    print("El género validado es: Femenino.")
else:
    print("Entrada no válida. Por favor, ingresa 'Masculino' o 'Femenino'.")  

#EJEMPLO ANGEL 2

# Solicitamos el estado civil al usuario
estado_civil = input("Por favor, ingresa tu estado civil (Soltero / Casado / Divorciado / Viudo): ")
# Limpiamos el texto (quitamos espacios y pasamos a minúsculas)
estado_civil_limpio = estado_civil.strip().lower()
# Validamos la opción ingresada usando condicionales
if estado_civil_limpio == "soltero" or estado_civil_limpio == "soltera":
    print("Estado civil registrado: Soltero/a.") 
elif estado_civil_limpio == "casado" or estado_civil_limpio == "casada":
    print("Estado civil registrado: Casado/a.")
elif estado_civil_limpio == "divorciado" or estado_civil_limpio == "divorciada":
    print("Estado civil registrado: Divorciado/a.")   
elif estado_civil_limpio == "viudo" or estado_civil_limpio == "viuda":
    print("Estado civil registrado: Viudo/a.")   
else:
    print("Opción no válida. Por favor, ingresa Soltero, Casado, Divorciado o Viudo.")
