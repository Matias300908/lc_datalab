# RETO FINAL SEMANA 7

# ==========================================
# DATALAB v0.7
# Reto final: Refactorizar sin cambiar
# el comportamiento esperado
# ==========================================


# Reto 1: Mostrar mensaje de bienvenida
def mostrar_mensaje():
    """Muestra el mensaje de bienvenida."""
    print("\nBienvenido a DataLab v0.7")


# Reto 5: Clasificar un valor
def clasificar_valor(valor):
    """
    Recibe un valor y devuelve su clasificación.
    Los umbrales siguen los ejemplos de los retos.
    """
    if valor >= 70:
        return "ALTO"
    elif valor >= 40:
        return "NORMAL"
    else:
        return "BAJO"


# Reto 6: Contar registros
def contar_registros(valores):
    """Retorna la cantidad de registros."""
    return len(valores)


# Reto 7: Calcular suma
def calcular_suma(valores):
    """Calcula y retorna la suma de los valores."""
    suma = 0

    for valor in valores:
        suma += valor

    return suma


# Reto 8 y Reto 12: Procesar registros
def procesar_registros(valores):
    """
    Procesa los registros y retorna:
    total, altos, normales, bajos, suma y existe_alto.
    """
    total = contar_registros(valores)
    altos = 0
    normales = 0
    bajos = 0
    suma = calcular_suma(valores)
    existe_alto = False

    for valor in valores:
        categoria = clasificar_valor(valor)

        if categoria == "ALTO":
            altos += 1
            existe_alto = True
        elif categoria == "NORMAL":
            normales += 1
        else:
            bajos += 1

    return (
        total,
        altos,
        normales,
        bajos,
        suma,
        existe_alto
    )


# Reto 13: Mostrar resumen
def mostrar_resumen(
    total,
    altos,
    normales,
    bajos,
    suma,
    existe_alto
):
    """Muestra los resultados del procesamiento."""
    print("\n========== RESUMEN ==========")
    print("Total de registros:", total)
    print("Valores altos:", altos)
    print("Valores normales:", normales)
    print("Valores bajos:", bajos)
    print("Suma de valores:", suma)
    print("Existe un valor alto:", "Sí" if existe_alto else "No")
    print("=============================")


# Leer y validar valores numéricos
def leer_valor(mensaje):
    """Solicita un número y valida la entrada."""
    while True:
        try:
            valor = float(input(mensaje))
            return valor
        except ValueError:
            print("Entrada inválida. Debes ingresar un número.")


# Leer una cantidad de registros
def leer_registros():
    """Solicita la cantidad y los valores que se procesarán."""
    while True:
        try:
            cantidad = int(
                input("¿Cuántos registros deseas ingresar? ")
            )

            if cantidad > 0:
                break

            print("La cantidad debe ser mayor que cero.")

        except ValueError:
            print("Entrada inválida. Ingresa un número entero.")

    valores = []

    for i in range(cantidad):
        valor = leer_valor(
            f"Ingresa el valor del registro {i + 1}: "
        )
        valores.append(valor)

    return valores


# Reto 9: Mostrar menú
def mostrar_menu():
    """Presenta las opciones principales de DataLab."""
    print("\n========== DATALAB v0.7 ==========")
    print("1. Procesar registros")
    print("2. Mostrar información del programa")
    print("3. Salir")
    print("==================================")


# Reto 10: Leer opción
def leer_opcion():
    """Lee y retorna la opción seleccionada."""
    return input("Selecciona una opción: ").strip()


# Mostrar información del programa
def mostrar_informacion():
    """Presenta información general de DataLab."""
    print("\nDataLab v0.7")
    print("Programa de clasificación y procesamiento de registros.")
    print("Utiliza funciones, parámetros, argumentos y return.")
    print("Las categorías son ALTO, NORMAL y BAJO.")


# Reto 11: Ejecutar opción
def ejecutar_opcion(opcion):
    """
    Ejecuta la opción seleccionada.
    Retorna False para finalizar y True para continuar.
    """
    if opcion == "1":
        valores = leer_registros()

        resultado = procesar_registros(valores)

        mostrar_resumen(*resultado)

    elif opcion == "2":
        mostrar_informacion()

    elif opcion == "3":
        print("\nGracias por utilizar DataLab. ¡Hasta pronto!")
        return False

    else:
        print("\nOpción inválida. Selecciona 1, 2 o 3.")

    return True


# Reto 14: Función principal
def main():
    """
    Coordina el programa.
    El menú, la entrada, el procesamiento y la presentación
    están separados en funciones.
    """
    mostrar_mensaje()

    continuar = True

    while continuar:
        mostrar_menu()
        opcion = leer_opcion()
        continuar = ejecutar_opcion(opcion)


# Punto de entrada del programa
if __name__ == "__main__":
    main()
