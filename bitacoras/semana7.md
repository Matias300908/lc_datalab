# Reto 1 — Primera función

def mostrar_mensaje():
    print("Bienvenido a DataLab")
 
mostrar_mensaje()

1. La definición es el bloque que comienza con def mostrar_mensaje(): y contiene la instrucción indentada.
2. La invocación es mostrar_mensaje().
3. Su responsabilidad es mostrar el mensaje de bienvenida.

# Reto 2 — Parámetro y argumento

def saludar(nombre):
    print(f"Hola, {nombre}")
 
saludar("Ana")
saludar("Carlos")
saludar("María")

Nombre es el parámetro (nombre local que recibe la función); cada texto pasado, como "Ana", es un argumento. Un parámetro permite reutilizar la función con distintos datos.

# Reto 3 — Función con retorno

def duplicar(valor):
    return valor * 2
 
print(duplicar(5))
print(duplicar(0))
print(duplicar(10))

Recibe valor, calcula su doble y retorna el resultado. Queda disponible en la expresión que llamó a la función; por ejemplo, resultado = duplicar(5) lo guarda en resultado. Salida: 10, 0, 20.

# Reto 4 — print() frente a return
def mostrar_menu():
    """
    Muestra las opciones disponibles en el menú principal.
    """
    pass


def leer_opcion():
    """
    Lee la opción seleccionada por el usuario y la devuelve.
    """
    pass


def clasificar_valor(valor):
    """
    Recibe un valor y devuelve su clasificación correspondiente.
    """
    pass


def procesar_registros(valores):
    """
    Procesa una lista de registros y devuelve los resultados
    del conteo y los cálculos realizados.
    """
    pass


def mostrar_resumen(resultado):
    """
    Recibe los resultados del procesamiento y los presenta
    al usuario.
    """
    pass


def main():
    """
    Coordina el funcionamiento general de DataLab y llama
    a las funciones necesarias.
    """
    pass

def mostrar_resultado(valor):
    print(valor)
 
def obtener_resultado(valor):
    return valor
 
mostrar_resultado(25)
resultado = obtener_resultado(25)
print(resultado + 5)

mostrar_resultado presenta el valor. obtener_resultado lo entrega al programa, por lo que otro bloque puede guardarlo, transformarlo o pasarlo a otra función. return permite reutilizar el resultado.

# Reto 5 — Clasificación

def clasificar_valor(valor):
    if valor >= 70:
        return "ALTO"
    if valor >= 40:
        return "NORMAL"
    return "BAJO"

Los umbrales son demostrativos, pues no aparecen en los documentos fuente. Con ellos, 80 da ALTO, 55 da NORMAL y 20 da BAJO. La clasificación se invoca desde el procesamiento y no se vuelve a escribir allí. Centralizarla evita reglas duplicadas y facilita cambiar o corregir una regla en un solo sitio.

# Reto 6 — Contar registros

def contar_registros(valores):
    contador = 0
    for _ in valores:
        contador += 1
    return contador
 
print(contar_registros([22, 55, 72, 38, 61]))  # 5

El contador se inicializa dentro de la función para que cada llamada empiece desde cero, sea independiente y no dependa de estado global o de llamadas anteriores.

# Reto 7 — Calcular suma

def calcular_suma(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma
 
print(calcular_suma([10, 20, 30, 40]))  # 100

 suma es un acumulador local: empieza en cero, incorpora cada elemento y se retorna.

# Reto 8 — Clasificación y resumen

def resumir_clasificaciones(valores):
    altos = normales = bajos = 0
    for valor in valores:
        categoria = clasificar_valor(valor)
        if categoria == "ALTO":
            altos += 1
        elif categoria == "NORMAL":
            normales += 1
        else:
            bajos += 1
    return altos, normales, bajos
 
print(resumir_clasificaciones([20, 55, 80, 40, 70]))

Con los umbrales demostrativos se obtiene (2, 2, 1): dos altos, dos normales y un bajo. Al cambiar a las reglas reales, los contadores se ajustan sin duplicar la clasificación.

# Reto 9 — Separar el menú

mostrar_menu() se limita a imprimir las opciones. No procesa registros ni calcula el resumen. main() queda a cargo de coordinar llamadas y el ciclo de ejecución.

# Reto 10 — Leer opción

def leer_opcion():
    return input("Seleccione una opción: ").strip()
 
opcion = leer_opcion()

La función no recibe datos explícitos; obtiene la opción del usuario y la produce como texto. return la entrega a main() o a ejecutar_opcion() para validarla y utilizarla.

# Reto 11 — Ejecutar opción

def ejecutar_opcion(opcion):
    if opcion == "1":
        resultados = procesar_registros([20, 55, 80, 40, 70])
        mostrar_resumen(*resultados)
    elif opcion == "2":
        mostrar_informacion()
    elif opcion == "3":
        print("Hasta pronto.")
        return False
    else:
        print("Opción inválida.")
    return True

Esta función dirige la opción a la operación apropiada. El procesamiento y la presentación del resumen permanecen separados.

# Reto 12 — Procesar registros
procesar_registros(valores) recibe los datos que procesará. Para cada valor incrementa total, actualiza la suma, llama a clasificar_valor(), actualiza el contador correspondiente y activa existe_alto si aplica. Retorna la tupla (total, altos, normales, bajos, suma, existe_alto). Los resultados viajan por retorno, no por globales.

# Reto 13 — Mostrar resumen
mostrar_resumen(total, altos, normales, bajos, suma, existe_alto) recibe las métricas y solo las imprime. Separar cálculo de presentación permite revisar cada parte con claridad y cambiar el formato del reporte sin tocar el cálculo.

# Reto 14 — Reducir main()
La estructura final es: main() llama a mostrar_mensaje(), luego repite mostrar_menu(), obtiene opcion con leer_opcion() y delega a ejecutar_opcion(). Para la opción 1, esta coordina procesar_registros() y mostrar_resumen(), y el procesamiento reutiliza clasificar_valor(). main() conserva el control del ciclo y la coordinación; presentación del menú, entrada, clasificación, procesamiento y resumen quedan en funciones específicas.

# Reto 15 — Variables globales
Variable: total / contador_total ¿Es global?: No, es local a procesar_registros. ¿Puede ser parámetro?: No es necesario; es estado interno. ¿Puede retornarse?: Sí, como parte del resultado.

Variable: altos ¿Es global?: No, es local. ¿Puede ser parámetro?: No es necesario; es estado interno. ¿Puede retornarse?: Sí.

Variable: normales ¿Es global?: No, es local. ¿Puede ser parámetro?: No es necesario; es estado interno. ¿Puede retornarse?: Sí.

Variable: bajos ¿Es global?: No, es local. ¿Puede ser parámetro?: No es necesario; es estado interno. ¿Puede retornarse?: Sí.

Variable: suma / suma_valores ¿Es global?: No, es local. ¿Puede ser parámetro?: No es necesario; es estado interno. ¿Puede retornarse?: Sí.

Variable: existe_alto ¿Es global?: No, es local. ¿Puede ser parámetro?: No es necesario; es estado interno. ¿Puede retornarse?: Sí.

Variable: valores ¿Es global?: No, se crea en la opción 1. ¿Puede ser parámetro?: Sí, se pasa a procesar_registros. ¿Puede retornarse?: No es necesario retornarla.

# Reto 16 — Refactorizar sin cambiar el comportamiento
Objetivo: reorganizar el código de DataLab mediante funciones, manteniendo el mismo comportamiento.

Procedimiento realizado
Ejecutar DataLab y comprobar su funcionamiento.

Registrar los resultados iniciales del programa.

Crear un commit de línea base para guardar la versión original.

Identificar responsabilidades que pueden separarse en funciones.

Crear funciones para mostrar el menú, leer opciones, clasificar valores, procesar registros y mostrar el resumen.

Pasar información mediante parámetros y argumentos.

Utilizar return para devolver los resultados del procesamiento.

Ejecutar nuevamente las pruebas.

Comparar los resultados anteriores y posteriores a la refactorización.

Ejemplo de refactorización
Antes, el programa podría tener todo el procesamiento dentro de una sola función o bloque de código. Después, se organiza en funciones independientes:


python
def clasificar_valor(valor):
    if valor >= 70:
        return "alto"
    elif valor >= 40:
        return "normal"
    else:
        return "bajo"


def procesar_registros(valores):
    total = len(valores)
    altos = 0
    normales = 0
    bajos = 0
    suma = 0
    existe_alto = False

    for valor in valores:
        clasificacion = clasificar_valor(valor)
        suma += valor

        if clasificacion == "alto":
            altos += 1
            existe_alto = True
        elif clasificacion == "normal":
            normales += 1
        else:
            bajos += 1

    return {
        "total": total,
        "altos": altos,
        "normales": normales,
        "bajos": bajos,
        "suma": suma,
        "existe_alto": existe_alto
    }


def mostrar_resumen(resultado):
    print("Total de registros:", resultado["total"])
    print("Valores altos:", resultado["altos"])
    print("Valores normales:", resultado["normales"])
    print("Valores bajos:", resultado["bajos"])
    print("Suma:", resultado["suma"])
    print("Existe un valor alto:", resultado["existe_alto"])


def main():
    valores = [20, 45, 75, 30, 80]
    resultado = procesar_registros(valores)
    mostrar_resumen(resultado)


if __name__ == "__main__":
    main()

#  Reto 17 — Pruebas antes y después
Objetivo: comprobar que el programa conserva su comportamiento después de la refactorización.

La siguiente tabla es un modelo de registro que debes contrastar con las ejecuciones reales.

Prueba

Antes

Después

¿Coincide?

Clasificación

Clasifica los valores

Clasifica los valores

Sí, si los resultados son iguales

Procesamiento

Procesa los registros

Procesa los registros

Sí, si los resultados son iguales

Resumen

Muestra el resumen

Muestra el resumen

Sí, si la información es igual

Opción válida

Ejecuta la opción seleccionada

Ejecuta la misma opción

Sí, si el resultado es igual

Opción inválida

Informa del error

Informa del error

Sí, si el mensaje y el flujo se conservan

Salida

Finaliza el programa

Finaliza el programa

Sí, si se mantiene el comportamiento

# Reto 18 — Pruebas de funciones
Objetivo: comprobar el funcionamiento de tres funciones mediante diferentes entradas.

Para los siguientes ejemplos se utiliza una clasificación ilustrativa: alto desde 70, normal desde 40 hasta menos de 70 y bajo por debajo de 40.

Función

Entrada

Resultado esperado

Resultado obtenido

clasificar_valor(55)

55

"normal"

"normal" en el ejemplo

duplicar(5)

5

10

10 en el ejemplo

contar_registros([10, 20, 30])

[10, 20, 30]

3

3 en el ejemplo

## Código de las funciones de prueba

python
def clasificar_valor(valor):
    if valor >= 70:
        return "alto"
    elif valor >= 40:
        return "normal"
    else:
        return "bajo"


def duplicar(numero):
    return numero * 2


def contar_registros(registros):
    return len(registros)


print(clasificar_valor(55))
print(duplicar(5))
print(contar_registros([10, 20, 30]))

# Reto 19 — Análisis de responsabilidad
Objetivo: identificar qué recibe, qué hace y qué retorna cada función principal de DataLab.

Función

¿Qué recibe?

¿Qué hace?

¿Qué retorna?

mostrar_menu()

No necesita parámetros, si el menú es fijo

Muestra las opciones disponibles

Normalmente nada (None)

leer_opcion()

Entrada del usuario

Lee la opción seleccionada

La opción ingresada

clasificar_valor()

Un valor numérico

Determina su clasificación

La categoría correspondiente

procesar_registros()

Una lista de valores o los registros que se procesarán

Clasifica, cuenta y calcula resultados

Un conjunto de resultados

mostrar_resumen()

Los resultados del procesamiento

Presenta los datos calculados

Normalmente nada (None)

main()

Normalmente no recibe parámetros

Coordina la ejecución del programa

Normalmente nada (None)

Pregunta: ¿Existe alguna función que esté realizando demasiadas responsabilidades?
Sí. Si una función se encarga de mostrar el menú, leer las opciones, validar entradas, procesar registros, calcular estadísticas y presentar los resultados, está realizando demasiadas responsabilidades.

Para mejorar el diseño, conviene dividirla en funciones pequeñas, cada una con un propósito definido. De esta manera, el código resulta más fácil de comprender, probar y mantener.

# Reto 20 — Documentar las funciones
def mostrar_menu():
    """
    Muestra las opciones disponibles en el menú principal.
    """
    pass


def leer_opcion():
    """
    Lee la opción seleccionada por el usuario y la devuelve.
    """
    pass


def clasificar_valor(valor):
    """
    Recibe un valor y devuelve su clasificación correspondiente.
    """
    pass


def procesar_registros(valores):
    """
    Procesa una lista de registros y devuelve los resultados
    del conteo y los cálculos realizados.
    """
    pass


def mostrar_resumen(resultado):
    """
    Recibe los resultados del procesamiento y los presenta
    al usuario.
    """
    pass


def main():
    """
    Coordina el funcionamiento general de DataLab y llama
    a las funciones necesarias.
    """
    pass

# RETO FINAL

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







