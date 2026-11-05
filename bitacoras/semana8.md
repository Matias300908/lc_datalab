# Reto 1

```python
valores = [22.5, 55.1, 72.3, 38.7, 61.4]
print("Lista completa:", valores)
print("Primer elemento:", valores[0])
print("Último elemento:", valores[-1])  # También válido: valores[len(valores) - 1]
print("Cantidad de elementos:", len(valores))
````

### ¿Por qué es más conveniente una lista? 
Permite agrupar un conjunto homogéneo o heterogéneo de datos relacionados bajo una sola variable, facilitando su recorrido mediante ciclos, el paso de parámetros a funciones y la manipulación dinámica sin requerir nombres de variables independientes.

# Reto 2

````python
valores = [22.5, 55.1, 72.3]

print("Primer elemento:", valores[0])
print("Segundo elemento:", valores[1])
print("Tercer elemento:", valores[2])

# El primer índice es 0 porque en Python (y en la arquitectura de la mayoría de lenguajes)
# el índice representa un desplazamiento (offset) exacto en la memoria a partir de la posición inicial de la colección.
````

# Reto 3
````python
valores = [10, 20, 30, 40, 50]

ultimo_indice = len(valores) - 1
print("Último elemento:", valores[ultimo_indice])
`````
### Explicación
len(valores) devuelve la cantidad total de elementos (5), pero los índices empiezan en 0, por lo que las posiciones válidas van de 0 a 4. Restar 1 ajusta el tamaño al índice límite.

# Reto 4
````python
valores = [10, 20, 30]

print("Tamaño inicial:", len(valores))

valores.append(40)
valores.append(50)
valores.append(60)

print("Lista final:", valores)
print("Tamaño final:", len(valores))
````
# Reto 5
````python
valores = [10, 20, 30, 40]

valores[0] = 15  # Modifica el primer elemento
valores[2] = 35  # Modifica el tercer elemento

print(valores)
````

### Diferencias
Modificar un elemento (lista[i] = valor) reemplaza el contenido existente en una posición fija sin alterar el tamaño de la lista. append() agrega un nuevo valor al final de la colección, incrementando su tamaño en 1.

# Reto 6
````python
valores = [22.5, 55.1, 72.3, 38.7]

for valor in valores:
    print(valor)
````

### Respuesta Pregunta
No se necesita conocer el índice porque el bucle for extrae automáticamente cada elemento de la colección uno por uno de forma directa.

# Reto 7
````python
valores = [22.5, 55.1, 72.3, 38.7]

for i in range(len(valores)):
    print(f"Índice: {i} - Valor: {valores[i]}")
````

# Reto 8
````python
valores = [22.5, 55.1, 72.3, 38.7]

print("Recorrido A: por valor")
for valor in valores:
    print(valor)

print("\nRecorrido B: por índice")
for i in range(len(valores)):
    print(f"Índice: {i} - Valor: {valores[i]}")
````

### Respuestas
1. El recorrido A entrega únicamente el valor de cada elemento.
2. El recorrido B entrega la posición numérica (índice) y el valor asociado.
3. Se usaría el recorrido por índice si necesitas modificar elementos directamente en la estructura mediante asignación (valores[i] = ...).

# Reto 9
````python
def calcular_suma(valores):
    suma = 0
    for valor in valores:
        suma += valor
    return suma

prueba = [10, 20, 30, 40]
print(calcular_suma(prueba))
````

# Reto 10
````python
def contar_elementos(valores):
    contador = 0
    for valor in valores:
        contador += 1
    return contador

print(contar_elementos([10, 20, 30, 40, 50]))
`````

### Diferencias con len()
len() es una función interna optimizada implementada en C que accede de manera instantánea ($O(1)$) al metadato de tamaño de la lista, mientras que contar con un bucle realiza un recorrido manual elemento por elemento ($O(n)$).

# Reto 11
````python
def clasificar_valor(valor):
    if valor >= 60:
        return "ALTO"
    elif valor >= 35:
        return "NORMAL"
    return "BAJO"

def procesar_valores(valores):
    for valor in valores:
        clasificacion = clasificar_valor(valor)
        print(f"Valor: {valor} -> Clasificación: {clasificacion}")

procesar_valores([22.5, 55.1, 72.3, 38.7, 61.4])

# Reto 12
````python
def generar_resumen(valores):
    altos = 0
    normales = 0
    bajos = 0

    for valor in valores:
        clasificacion = clasificar_valor(valor)
        if clasificacion == "ALTO":
            altos += 1
        elif clasificacion == "NORMAL":
            normales += 1
        elif clasificacion == "BAJO":
            bajos += 1

    return altos, normales, bajos

print(generar_resumen([22.5, 55.1, 72.3, 38.7, 61.4]))
````
# Reto 12
````python
def generar_resumen(valores):
    altos = 0
    normales = 0
    bajos = 0

    for valor in valores:
        clasificacion = clasificar_valor(valor)
        if clasificacion == "ALTO":
            altos += 1
        elif clasificacion == "NORMAL":
            normales += 1
        elif clasificacion == "BAJO":
            bajos += 1

    return altos, normales, bajos

print(generar_resumen([22.5, 55.1, 72.3, 38.7, 61.4]))
````

# Reto 13
````python
def generar_resumen_completo(valores):
    altos = 0
    normales = 0
    bajos = 0
    suma = 0
    existe_alto = False

    for valor in valores:
        suma += valor
        clasificacion = clasificar_valor(valor)
        if clasificacion == "ALTO":
            altos += 1
            existe_alto = True
        elif clasificacion == "NORMAL":
            normales += 1
        elif clasificacion == "BAJO":
            bajos += 1

    return altos, normales, bajos, suma, existe_alto

print(generar_resumen_completo([22.5, 55.1, 72.3, 38.7, 61.4]))
````

# Reto 14
````python
valores = []

if len(valores) == 0:
    print("La lista está vacía. No hay datos disponibles para procesar.")
else:
    # Lógica de procesamiento normal
    pass

# Decisión de diseño: Se evalúa explícitamente el tamaño antes de ejecutar operaciones analíticas para prevenir errores de ejecución o divisiones por cero en promedios.
````

# Reto 15
````python
def obtener_datos(cantidad):
    valores = []
    for i in range(cantidad):
        valor = float(input(f"Ingrese el valor {i+1}: "))
        valores.append(valor)
    return valores
````
# Reto 16
````python
valores = [10, 20, 30, 40]

for i in range(len(valores)):
    valores[i] = valores[i] * 2

print(valores)
````

# Reto 17 
````python
def calcular_promedio(valores):
    if len(valores) == 0:
        return 0.0  # Retorno seguro ante lista vacía
    
    suma = 0
    for valor in valores:
        suma += valor
    return suma / len(valores)

print(calcular_promedio([10, 20, 30, 40]))
print(calcular_promedio([]))
````

# Reto 18
````python
def mostrar_resumen(altos, normales, bajos, suma, existe_alto):
    print("\n--- Resumen General DataLab v0.8 ---")
    print(f"ALTO: {altos}")
    print(f"NORMAL: {normales}")
    print(f"BAJO: {bajos}")
    print(f"Suma acumulada: {suma}")
    print(f"¿Existe algún ALTO?: {'Sí' if existe_alto else 'No'}")

def ejecutar_procesamiento(valores):
    if len(valores) == 0:
        print("Advertencia: La lista está vacía.")
        return
    altos, normales, bajos, suma, existe_alto = generar_resumen_completo(valores)
    mostrar_resumen(altos, normales, bajos, suma, existe_alto)

ejecutar_procesamiento([22.5, 55.1, 72.3, 38.7, 61.4])
````

# Reto 19
### Caso A
+ Lista [50]
+ Resultado esperado: ALTO: 0, NORMAL: 1, BAJO: 0, Suma: 50.0, Existe ALTO: No
+ Resultado obtenido: 
ALTO: 0, NORMAL: 1, BAJO: 0, Suma: 50.0, Existe ALTO: No
+ ¿Correcto? : Si
 
### Caso B
+ Lista [22.5, 55.1]
+ Resultado esperado: ALTO: 0, NORMAL: 1, BAJO: 1, Suma: 77.6, Existe ALTO: No
+ Resultado obtenido: 
ALTO: 0, NORMAL: 1, BAJO: 1, Suma: 77.6, Existe ALTO: No
+ ¿Correcto? : Si

### Caso C
+ Lista []
+ Resultado esperado: Mensaje de lista vacía / control de excepciones Existe
+ Resultado obtenido: 
Mensaje de lista vacía controlado
+ ¿Correcto? : Si

### Caso D
+ Lista [22.5, 72.3, 40]
+ Resultado esperado: ALTO: 1, NORMAL: 1, BAJO: 1, Suma: 134.8, Existe ALTO: Sí
+ Resultado obtenido: 
ALTO: 1, NORMAL: 1, BAJO: 1, Suma: 134.8, Existe ALTO: Sí
+ ¿Correcto? : Si

### Caso E
+ Lista Valores límite
+ Resultado esperado: Clasificación estricta según umbrales exactos Existe ALTO: Sí
+ Resultado obtenido: 
Verificado en límites
+ ¿Correcto? : Si

# Reto 20
````python
valores = [10, 20, 30]

print(valores[0])
print(valores[1])
print(valores[2])

# Intentar acceder a valores[3] genera una excepción IndexError: list index out of range 
# porque la lista posee una longitud de 3 elementos, abarcando estrictamente los índices 0, 1 y 2.
# print(valores[3])
````

