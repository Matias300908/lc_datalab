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

# Ejemplo Dluca (1)

# Crear una contraseña
contraseña = input("Crea una contraseña: ")

# Digitar la contraseña para comprobarla
contraseña_digitada = input("Digite su contraseña: ")

# Comparar las dos contraseñas
if contraseña == contraseña_digitada:
    print("La contraseña es correcta.")
else:
    print("La contraseña no es correcta.")

    #Ejemplo Dluca (2)
    
    # Crear el correo
correo_creado = input("Cree su correo: ")

# Digitar el correo para verificar
correo_ingresado = input("Digite su correo: ")

# Verificar si el correo ingresado es igual al que creó
if correo_ingresado == correo_creado:
    print("El correo es correcto.")
else:
    print("El correo no es correcto.")

    """
validaciones_basicas.py

Material de apoyo - Lógica Computacional
Semana 04 - Ciclos for y range()

Validaciones básicas reutilizables.
"""

import re


# ============================================================
# 1. VALIDACIONES BÁSICAS DE TEXTO
# ============================================================

def validar_cadena_no_vacia(texto):
    """
    Verifica que una cadena tenga contenido.
    """
    if texto is None:
        return False

    return texto.strip() != ""


def validar_longitud(texto, minimo, maximo):
    """
    Verifica que la longitud de una cadena esté dentro de un rango.
    """
    if texto is None:
        return False

    longitud = len(texto.strip())

    return minimo <= longitud <= maximo


# ============================================================
# 2. CORREO ELECTRÓNICO
# ============================================================

def validar_correo(correo):
    """
    Validación básica de correo electrónico.
    """

    if not validar_cadena_no_vacia(correo):
        return False

    patron = r"^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$"

    return re.match(patron, correo.strip()) is not None


# ============================================================
# 3. NOMBRES DE PERSONAS
# ============================================================

def validar_nombre(nombre):
    """
    Verifica que un nombre contenga solamente letras y espacios.
    """

    if not validar_cadena_no_vacia(nombre):
        return False

    patron = (
        r"^[A-Za-zÁÉÍÓÚáéíóúÑñÜü]+"
        r"( [A-Za-zÁÉÍÓÚáéíóúÑñÜü]+)*$"
    )

    return re.match(patron, nombre.strip()) is not None


# ============================================================
# 4. TELÉFONO CELULAR
# ============================================================

def validar_celular(celular):
    """
    Validación básica para números de celular colombianos.

    Debe:
    - Tener 10 dígitos.
    - Comenzar por 3.
    """

    if not validar_cadena_no_vacia(celular):
        return False

    patron = r"^3\d{9}$"

    return re.match(patron, celular.strip()) is not None


# ============================================================
# 5. VALORES NUMÉRICOS DENTRO DE UN RANGO
# ============================================================

def validar_rango(valor, minimo, maximo):
    """
    Verifica que un número esté entre un mínimo y un máximo.
    """

    return minimo <= valor <= maximo


# ============================================================
# 6. EDAD
# ============================================================

def validar_edad(edad):
    """
    Edad válida entre 0 y 120 años.
    """

    return validar_rango(edad, 0, 120)


# ============================================================
# 7. NOTA ACADÉMICA
# ============================================================

def validar_nota(nota):
    """
    Valida una nota académica entre 0.0 y 5.0.
    """

    return validar_rango(nota, 0.0, 5.0)


# ============================================================
# 8. DOCUMENTO NUMÉRICO
# ============================================================

def validar_documento(documento):
    """
    Verifica que un documento contenga únicamente números.

    Longitud permitida: entre 6 y 12 dígitos.
    """

    if not validar_cadena_no_vacia(documento):
        return False

    patron = r"^\d{6,12}$"

    return re.match(patron, documento.strip()) is not None


# ============================================================
# 9. CÓDIGO DE PRODUCTO
# ============================================================

def validar_codigo_producto(codigo):
    """
    Código de producto.

    Ejemplos:
        ABC123
        PROD001

    Reglas:
        - 2 a 6 letras mayúsculas.
        - 2 a 6 números.
    """

    if not validar_cadena_no_vacia(codigo):
        return False

    patron = r"^[A-Z]{2,6}[0-9]{2,6}$"

    return re.match(patron, codigo.strip()) is not None


# ============================================================
# 10. VALORES PERMITIDOS
# ============================================================

def validar_valor_permitido(valor, valores_permitidos):
    """
    Verifica si un valor pertenece a una lista de opciones.
    """

    return valor in valores_permitidos


# ============================================================
# 11. RESPUESTA SÍ / NO
# ============================================================

def validar_si_no(respuesta):
    """
    Permite solamente SI o NO.

    Acepta:
        SI
        Si
        si
        sI
        NO
        No
        no
    """

    if not validar_cadena_no_vacia(respuesta):
        return False

    respuesta = respuesta.strip().upper()

    return respuesta == "SI" or respuesta == "NO"


# ============================================================
# 12. MATCH - NIVEL DE ESCOLARIDAD
# ============================================================

def nivel_escolaridad(codigo):
    """
    Convierte un código numérico en una descripción.
    """

    match codigo:
        case 0:
            return "Sin estudio"
        case 1:
            return "Primaria"
        case 2:
            return "Secundaria"
        case 3:
            return "Técnico/Tecnólogo"
        case 4:
            return "Universitario"
        case 5:
            return "Posgrado"
        case _:
            return "Código no válido"


# ============================================================
# 13. MATCH - ESTADO DE UN REGISTRO
# ============================================================

def estado_registro(codigo):
    """
    Convierte un código de estado en una descripción.
    """

    match codigo:
        case 1:
            return "Activo"
        case 2:
            return "Inactivo"
        case 3:
            return "Pendiente"
        case 4:
            return "Bloqueado"
        case _:
            return "Estado no válido"


# ============================================================
# 14. MATCH - TIPO DE DOCUMENTO
# ============================================================

def tipo_documento(codigo):
    """
    Clasifica un tipo de documento.
    """

    match codigo:
        case 1:
            return "Cédula de ciudadanía"
        case 2:
            return "Tarjeta de identidad"
        case 3:
            return "Cédula de extranjería"
        case 4:
            return "Pasaporte"
        case _:
            return "Tipo de documento no válido"


# ============================================================
# 15. MATCH - TIPO DE USUARIO
# ============================================================

def tipo_usuario(codigo):
    """
    Clasifica el tipo de usuario.
    """

    match codigo:
        case 1:
            return "Estudiante"
        case 2:
            return "Docente"
        case 3:
            return "Administrativo"
        case 4:
            return "Externo"
        case _:
            return "Tipo de usuario no válido"


# ============================================================
# 16. MATCH - ESTADO CIVIL
# ============================================================

def estado_civil(codigo):
    """
    Clasifica el estado civil.
    """

    match codigo:
        case 1:
            return "Soltero(a)"
        case 2:
            return "Casado(a)"
        case 3:
            return "Unión libre"
        case 4:
            return "Separado(a)"
        case 5:
            return "Divorciado(a)"
        case 6:
            return "Viudo(a)"
        case _:
            return "Estado civil no válido"


# ============================================================
# 17. MATCH - CLASIFICACIÓN DE UN VALOR
# ============================================================

def clasificar_valor(categoria):
    """
    Clasifica un valor.

    1 - Bajo
    2 - Normal
    3 - Alto
    """

    match categoria:
        case 1:
            return "Bajo"
        case 2:
            return "Normal"
        case 3:
            return "Alto"
        case _:
            return "Categoría no válida"


# ============================================================
# 18. EJEMPLO DE USO CON IF / ELSE
# ============================================================

def ejemplo_if_else():
    """
    Ejemplo sencillo utilizando una validación.
    """

    correo = input("Ingrese un correo: ")

    if validar_correo(correo):
        print("Correo válido")
    else:
        print("Correo inválido")


# ============================================================
# 19. EJEMPLO DE USO CON MATCH
# ============================================================

def ejemplo_match():
    """
    Ejemplo sencillo de match-case.
    """

    codigo = int(input("Ingrese el código de escolaridad: "))

    resultado = nivel_escolaridad(codigo)

    print("Nivel:", resultado)


# ============================================================
# 20. EJEMPLO PARA PROCESAR VARIOS DATOS
# ============================================================

def ejemplo_procesamiento():
    """
    Procesa varios correos utilizando la misma función.
    """

    correos = [
        "ana@gmail.com",
        "correo-invalido",
        "juan@universidad.edu.co",
        "usuario@",
        "maria@hotmail.com"
    ]

    validos = 0
    invalidos = 0

    for correo in correos:

        if validar_correo(correo):
            validos += 1
            print(correo, "-> válido")
        else:
            invalidos += 1
            print(correo, "-> inválido")

    print()
    print("Total válidos:", validos)
    print("Total inválidos:", invalidos)


# ============================================================
# 21. EJEMPLO DE REGISTRO
# ============================================================

def validar_registro(nombre, correo, edad, celular):
    """
    Un registro es válido si todos sus campos son válidos.
    """

    nombre_ok = validar_nombre(nombre)
    correo_ok = validar_correo(correo)
    edad_ok = validar_edad(edad)
    celular_ok = validar_celular(celular)

    if nombre_ok and correo_ok and edad_ok and celular_ok:
        return True
    else:
        return False


# ============================================================
# 22. PRUEBAS AUTOMÁTICAS
# ============================================================

def ejecutar_pruebas():
    """
    Ejecuta pruebas de todas las funciones principales.
    """

    print("==========================================")
    print(" PRUEBAS DE VALIDACIONES BÁSICAS")
    print("==========================================")

    print("\n--- Cadenas ---")
    print("Cadena no vacía:", validar_cadena_no_vacia("Hola"))
    print("Cadena vacía:", validar_cadena_no_vacia(""))

    print("\n--- Longitud ---")
    print("Python, 3-10:", validar_longitud("Python", 3, 10))
    print("Python, 10-20:", validar_longitud("Python", 10, 20))

    print("\n--- Correos ---")
    print(
        "estudiante@universidad.edu.co:",
        validar_correo("estudiante@universidad.edu.co")
    )
    print(
        "correo-invalido:",
        validar_correo("correo-invalido")
    )

    print("\n--- Nombres ---")
    print("José Rodríguez:", validar_nombre("José Rodríguez"))
    print("Juan123:", validar_nombre("Juan123"))

    print("\n--- Celulares ---")
    print("3001234567:", validar_celular("3001234567"))
    print("1234567890:", validar_celular("1234567890"))

    print("\n--- Rangos ---")
    print("75 entre 0 y 100:", validar_rango(75, 0, 100))
    print("120 entre 0 y 100:", validar_rango(120, 0, 100))

    print("\n--- Edad ---")
    print("Edad 25:", validar_edad(25))
    print("Edad 150:", validar_edad(150))

    print("\n--- Nota ---")
    print("Nota 4.5:", validar_nota(4.5))
    print("Nota 6.0:", validar_nota(6.0))

    print("\n--- Documento ---")
    print("12345678:", validar_documento("12345678"))
    print("123:", validar_documento("123"))

    print("\n--- Código de producto ---")
    print("ABC123:", validar_codigo_producto("ABC123"))
    print("producto123:", validar_codigo_producto("producto123"))

    print("\n--- Valor permitido ---")
    print(
        "ACTIVO:",
        validar_valor_permitido(
            "ACTIVO",
            ["ACTIVO", "INACTIVO"]
        )
    )

    print("\n--- SI / NO ---")
    print("si:", validar_si_no("si"))
    print("tal vez:", validar_si_no("tal vez"))

    print("\n--- Escolaridad ---")
    print("Código 0:", nivel_escolaridad(0))
    print("Código 4:", nivel_escolaridad(4))
    print("Código 9:", nivel_escolaridad(9))

    print("\n--- Estado de registro ---")
    print("Código 1:", estado_registro(1))
    print("Código 3:", estado_registro(3))
    print("Código 9:", estado_registro(9))

    print("\n--- Tipo de documento ---")
    print("Código 1:", tipo_documento(1))
    print("Código 4:", tipo_documento(4))
    print("Código 9:", tipo_documento(9))

    print("\n--- Tipo de usuario ---")
    print("Código 1:", tipo_usuario(1))
    print("Código 2:", tipo_usuario(2))
    print("Código 9:", tipo_usuario(9))

    print("\n--- Estado civil ---")
    print("Código 1:", estado_civil(1))
    print("Código 3:", estado_civil(3))
    print("Código 9:", estado_civil(9))

    print("\n--- Clasificación ---")
    print("Categoría 1:", clasificar_valor(1))
    print("Categoría 2:", clasificar_valor(2))
    print("Categoría 3:", clasificar_valor(3))
    print("Categoría 9:", clasificar_valor(9))

    print("\n--- Registro completo ---")

    registro1 = validar_registro(
        "José Rodríguez",
        "jose@gmail.com",
        25,
        "3001234567"
    )

    registro2 = validar_registro(
        "Juan123",
        "correo-invalido",
        150,
        "1234567890"
    )

    print("Registro 1:", registro1)
    print("Registro 2:", registro2)

    print("\n--- Procesamiento de varios correos ---")
    ejemplo_procesamiento()

    print("\n==========================================")
    print(" PRUEBAS FINALIZADAS")
    print("==========================================")


# ============================================================
# 23. EJECUCIÓN PRINCIPAL
# ============================================================

if __name__ == "__main__":
    ejecutar_pruebas()
