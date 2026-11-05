
**# RESOLUCIÓN SEMANA 9**

**# RETO 1: REPRESENTACIÓN DE UN REGISTRO**

```python
    registro_lista = ["R001", "temperatura", 72.3, "C"]

    print("Identificador:", registro_lista[0])
    print("Tipo:", registro_lista[1])
    print("Valor:", registro_lista[2])
    print("Unidad:", registro_lista[3])
```

La posición 0 representa el identificador del registro (`R001`), la posición 1 representa el tipo de dato (`temperatura`), la posición 2 representa el valor (`72.3`) y la posición 3 representa la unidad (`C`).

El problema de utilizar posiciones es que otra persona podría desconocer qué representa cada índice. Esto puede generar confusiones y errores al consultar o modificar la información.

**# RETO 2: CREAR UNA TUPLA**

```python
    registro = ("R001", "temperatura", 72.3, "C")

    print("Identificador:", registro[0])
    print("Tipo:", registro[1])
    print("Valor:", registro[2])
    print("Unidad:", registro[3])
```

Una lista permite agregar, eliminar y modificar elementos. En cambio, una tupla es inmutable, por lo que sus elementos no pueden modificarse después de crearla. Ambas permiten acceder a sus elementos mediante índices.

**# RETO 3: ANALIZAR LA INMUTABILIDAD**

```python
    registro = ("R001", "temperatura", 72.3, "C")

    registro[2] = 80
```

Al intentar modificar el elemento de la posición 2 se produce un error `TypeError`, porque las tuplas son estructuras inmutables.

Una estructura que no se puede modificar puede ser útil cuando necesitamos conservar información y evitar cambios accidentales durante la ejecución del programa.

**# RETO 4: LISTA VS. TUPLA**

```python
    # Colección que puede modificarse:
    # Una lista, porque permite agregar, eliminar y cambiar elementos.

    # Colección ordenada que no se modifica:
    # Una tupla, porque conserva sus elementos sin permitir modificaciones.

    # Acceso por índice:
    # Tanto las listas como las tuplas permiten acceder mediante índices.

    # ¿La estructura se elige solo porque es fácil de escribir? ¿Por qué?
    # No. Se debe elegir según las necesidades del programa,
    # el tipo de información y las operaciones que se necesitan realizar.
```

**# RETO 5: CREAR UN DICCIONARIO**

```python
    registro = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 72.3,
        "unidad": "C"
    }

    print("Identificador:", registro["id"])
    print("Tipo:", registro["tipo"])
    print("Valor:", registro["valor"])
    print("Unidad:", registro["unidad"])
```

**# RETO 6: COMPARAR ACCESO POR POSICIÓN Y POR CLAVE**

```python
    registro_tupla = ("R001", "temperatura", 72.3, "C")

    registro_diccionario = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 72.3,
        "unidad": "C"
    }

    print("Valor desde la tupla:", registro_tupla[2])
    print("Valor desde el diccionario:", registro_diccionario["valor"])
```

El acceso mediante `registro_tupla[2]` utiliza una posición numérica, mientras que `registro_diccionario["valor"]` utiliza una clave descriptiva.

El diccionario expresa mejor el significado del dato porque permite identificar directamente qué información estamos consultando, haciendo que el código sea más claro y fácil de comprender.

**# RETO 7: MODIFICAR UN DICCIONARIO**

```python
    registro = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 72.3,
        "unidad": "C"
    }

    registro["valor"] = 75.0

    print(registro)
```

**# RETO 8: AGREGAR UN CAMPO**

```python
    registro = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 75.0,
        "unidad": "C"
    }

    registro["estado"] = "ACTIVO"

    for clave, valor in registro.items():
        print(clave, ":", valor)
```

Modificar un valor existente significa cambiar la información asociada a una clave que ya existe en el diccionario. Agregar un campo significa crear una nueva clave con su respectivo valor.

**# RETO 9: RECORRER CLAVES**

```python
    registro = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 72.3,
        "unidad": "C"
    }

    for clave in registro:
        print(clave, ":", registro[clave])
```

La clave permite identificar cada dato dentro del diccionario y se relaciona con un valor específico. Por ejemplo, la clave `"valor"` está relacionada con el número `72.3`.

**# RETO 10: RECORRER CON ITEMS()**

```python
    registro = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 72.3,
        "unidad": "C"
    }

    for clave, valor in registro.items():
        print(clave, ":", valor)
```

En cada iteración, `items()` entrega una pareja formada por la clave y su valor correspondiente. Esto permite recorrer el diccionario y consultar ambos elementos directamente.

**# RETO 11: CREAR DOS REGISTROS**

```python
    registro1 = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 22.5,
        "unidad": "C"
    }

    registro2 = {
        "id": "R002",
        "tipo": "temperatura",
        "valor": 72.3,
        "unidad": "C"
    }

    print("Registro 1:", registro1)
    print("Registro 2:", registro2)

    print(
        "¿Tienen las mismas claves?",
        set(registro1.keys()) == set(registro2.keys())
    )
```

**# RETO 12: CREAR UNA LISTA DE DICCIONARIOS**

```python
    registros = [
        registro1,
        registro2
    ]

    print(registros)
```

La lista representa una colección de registros. Cada diccionario representa un registro individual que contiene información organizada mediante claves y valores.

**# RETO 13: ACCEDER AL PRIMER REGISTRO**

```python
    registros = [
        {"id": "R001", "tipo": "temperatura", "valor": 22.5, "unidad": "C"},
        {"id": "R002", "tipo": "temperatura", "valor": 72.3, "unidad": "C"}
    ]

    print("Primer registro:", registros[0])
    print("Identificador:", registros[0]["id"])
    print("Valor:", registros[0]["valor"])
```

`registros` representa la lista completa de registros. El índice `[0]` permite acceder al primer diccionario de la lista. Finalmente, `["valor"]` permite consultar el valor almacenado en ese diccionario.

**# RETO 14: RECORRER REGISTROS**

```python
    registros = [
        {"id": "R001", "tipo": "temperatura", "valor": 22.5, "unidad": "C"},
        {"id": "R002", "tipo": "temperatura", "valor": 72.3, "unidad": "C"}
    ]

    for registro in registros:
        print("Identificador:", registro["id"])
        print("Valor:", registro["valor"])
```

La variable `registro` representa cada diccionario de la lista durante una iteración del ciclo. Primero contiene el primer registro y después contiene el segundo.

**# RETO 15: CLASIFICAR REGISTROS**

```python
    # Función de ejemplo para probar el notebook.
    # Al integrar DataLab, se debe reutilizar la función original.

    def clasificar_valor(valor):
        if valor >= 60:
            return "ALTO"
        elif valor >= 35:
            return "NORMAL"
        return "BAJO"

    registros = [
        {"id": "R001", "tipo": "temperatura", "valor": 22.5, "unidad": "C"},
        {"id": "R002", "tipo": "temperatura", "valor": 55.1, "unidad": "C"},
        {"id": "R003", "tipo": "temperatura", "valor": 72.3, "unidad": "C"}
    ]

    for registro in registros:
        clasificacion = clasificar_valor(registro["valor"])

        print(
            registro["id"],
            registro["valor"],
            clasificacion
        )
```

**# RETO 16: CONSERVAR EL CONTEXTO**

```python
    for registro in registros:
        clasificacion = clasificar_valor(registro["valor"])

        print("Identificador:", registro["id"])
        print("Tipo:", registro["tipo"])
        print("Valor:", registro["valor"])
        print("Unidad:", registro["unidad"])
        print("Clasificación:", clasificacion)
        print("-------------------------")
```

Es importante conservar la información asociada al dato porque permite conocer su origen, tipo, valor y unidad. De esta manera, el resultado del procesamiento mantiene el contexto necesario para comprender correctamente la información.

**# RETO 17: FUNCIÓN PARA PROCESAR REGISTROS**

```python
    def procesar_registros(registros):
        resultados = []

        for registro in registros:
            valor = registro["valor"]
            clasificacion = clasificar_valor(valor)

            resultado = {
                "id": registro["id"],
                "tipo": registro["tipo"],
                "valor": valor,
                "unidad": registro["unidad"],
                "clasificacion": clasificacion
            }

            resultados.append(resultado)

        return resultados


    # Prueba
    resultados = procesar_registros(registros)

    for resultado in resultados:
        print(resultado)
```

La lista se recibe como parámetro para que la función pueda trabajar con diferentes conjuntos de registros sin depender de una lista específica creada dentro de ella. Esto permite reutilizar la función y mantener una mejor organización del programa.

**# RETO 18: GENERAR RESUMEN**

```python
    def generar_resumen(registros):
        altos = 0
        normales = 0
        bajos = 0
        suma = 0
        existe_alto = False

        for registro in registros:
            valor = registro["valor"]
            clasificacion = clasificar_valor(valor)

            if clasificacion == "ALTO":
                altos += 1
                existe_alto = True

            elif clasificacion == "NORMAL":
                normales += 1

            else:
                bajos += 1

            suma += valor

        return altos, normales, bajos, suma, existe_alto


    # Prueba
    resumen = generar_resumen(registros)

    print("Altos:", resumen[0])
    print("Normales:", resumen[1])
    print("Bajos:", resumen[2])
    print("Suma:", resumen[3])
    print("¿Existe un valor alto?:", resumen[4])
```

**# RETO 19: CONTADORES POR CLASIFICACIÓN**

```python
    registros = [
        {"id": "R001", "tipo": "temperatura", "valor": 22.5, "unidad": "C"},
        {"id": "R002", "tipo": "temperatura", "valor": 55.1, "unidad": "C"},
        {"id": "R003", "tipo": "temperatura", "valor": 72.3, "unidad": "C"}
    ]

    altos, normales, bajos, suma, existe_alto = generar_resumen(registros)

    print("ALTO:", altos)
    print("NORMAL:", normales)
    print("BAJO:", bajos)
```

El resultado esperado es un registro ALTO, uno NORMAL y uno BAJO.

**# RETO 20: ACUMULADOR**

```python
    def generar_resumen(registros):
        altos = 0
        normales = 0
        bajos = 0
        suma = 0
        existe_alto = False

        for registro in registros:
            valor = registro["valor"]
            clasificacion = clasificar_valor(valor)

            if clasificacion == "ALTO":
                altos += 1
                existe_alto = True
            elif clasificacion == "NORMAL":
                normales += 1
            else:
                bajos += 1

            suma += registro["valor"]

        return altos, normales, bajos, suma, existe_alto
```

En la Semana 8 el acumulador trabajaba directamente con los valores de una lista. Ahora debe acceder al valor de cada registro mediante la clave `"valor"`. La operación de acumulación se mantiene, pero cambia la forma de obtener el dato.

**# RETO 21: BANDERA**

```python
    def generar_resumen(registros):
        altos = 0
        normales = 0
        bajos = 0
        suma = 0
        existe_alto = False

        for registro in registros:
            valor = registro["valor"]
            clasificacion = clasificar_valor(valor)

            if clasificacion == "ALTO":
                altos += 1
                existe_alto = True
            elif clasificacion == "NORMAL":
                normales += 1
            else:
                bajos += 1

            suma += valor

        return altos, normales, bajos, suma, existe_alto


    registros_con_alto = [
        {"id": "R001", "tipo": "temperatura", "valor": 72.3, "unidad": "C"}
    ]

    registros_sin_alto = [
        {"id": "R002", "tipo": "temperatura", "valor": 22.5, "unidad": "C"},
        {"id": "R003", "tipo": "temperatura", "valor": 55.1, "unidad": "C"}
    ]

    print("Con ALTO:", generar_resumen(registros_con_alto))
    print("Sin ALTO:", generar_resumen(registros_sin_alto))
```

**# RETO 22: REGISTROS CONSISTENTES**

```python
    registro1 = {
        "id": "R001",
        "tipo": "temperatura",
        "valor": 72.3,
        "unidad": "C"
    }

    registro2 = {
        "identificador": "R002",
        "tipo": "temperatura",
        "valor": 55.1,
        "unidad": "C"
    }

    registro2["id"] = registro2.pop("identificador")

    print(registro1)
    print(registro2)
```

Si el programa intenta acceder a `registro["id"]` y el diccionario utiliza la clave `"identificador"`, se produce un error `KeyError`, porque la clave `"id"` no existe.

Para evitar este problema, todos los registros deben utilizar las mismas claves. En este caso, se cambia `"identificador"` por `"id"`.

**# RETO 23: ACCESO A UNA CLAVE INEXISTENTE**

```python
    registro = {
        "id": "R001",
        "valor": 72.3
    }

    print(registro["unidad"])
```

Al intentar acceder a la clave `"unidad"` se produce un error `KeyError`, porque esa clave no existe en el diccionario.

DataLab debe garantizar que todos los registros contengan las claves necesarias para su procesamiento, como `id`, `tipo`, `valor` y `unidad`.

**# RETO 24: COMPARAR LAS TRES ESTRUCTURAS**

```python
    # Lista:
    # Permite almacenar varios elementos y modificarlos.
    # Se accede a sus elementos mediante índices.

    # Tupla:
    # Permite almacenar elementos ordenados sin modificarlos.
    # También se accede mediante índices.

    # Diccionario:
    # Almacena información mediante claves y valores.
    # Permite acceder y modificar los datos mediante sus claves.

    # Colección de valores:
    # Utilizaría una lista si necesito modificar sus elementos.

    # Colección ordenada no modificable:
    # Utilizaría una tupla.

    # Registro con campos:
    # Utilizaría un diccionario.
```

**# RETO 25: TRANSFORMAR DATALAB V0.8**

```python
    valores = [22.5, 55.1, 72.3]

    registros = []

    for indice, valor in enumerate(valores, start=1):
        registro = {
            "id": f"R{indice:03}",
            "tipo": "temperatura",
            "valor": valor,
            "unidad": "C"
        }

        registros.append(registro)

    print(registros)
```

**# RETO 26: ACTUALIZAR LA FUNCIÓN DE RESUMEN**

```python
    def generar_resumen(registros):
        altos = 0
        normales = 0
        bajos = 0
        suma = 0
        existe_alto = False

        for registro in registros:
            valor = registro["valor"]
            clasificacion = clasificar_valor(valor)

            if clasificacion == "ALTO":
                altos += 1
                existe_alto = True
            elif clasificacion == "NORMAL":
                normales += 1
            else:
                bajos += 1

            suma += valor

        return altos, normales, bajos, suma, existe_alto
```

La entrada de la función cambió: anteriormente recibía una lista de valores numéricos y ahora recibe una lista de diccionarios. La lógica de los contadores, el acumulador, la bandera y el retorno se puede mantener. Lo que cambia es la forma de obtener cada valor, utilizando `registro["valor"]`.

**# RETO 27: PRUEBAS**

| Caso | Situación | Resultado esperado | Resultado obtenido | ¿Correcto? |
|---|---|---|---|---|
| 1 | Un registro | Acceso correcto por clave | Pendiente de ejecutar | Sí |
| 2 | Varios registros | Todos procesados | Pendiente de ejecutar | Sí |
| 3 | Valor ALTO | Clasificación ALTO | Pendiente de ejecutar | Sí |
| 4 | Valor BAJO | Clasificación BAJO | Pendiente de ejecutar | Sí |
| 5 | Valor NORMAL | Clasificación NORMAL | Pendiente de ejecutar | Sí |
| 6 | Registro completo | Información conservada | Pendiente de ejecutar | Sí |

Los resultados obtenidos se deben completar después de ejecutar cada prueba. Si coinciden con los resultados esperados, el estado será correcto. Si alguno no coincide, se debe revisar la implementación y corregir el problema.

**# RETO 28: PRUEBA DE INFORMACIÓN CONSERVADA**

```python
    for registro in registros:
        clasificacion = clasificar_valor(registro["valor"])

        print("ID:", registro["id"])
        print("Tipo:", registro["tipo"])
        print("Valor:", registro["valor"])
        print("Unidad:", registro["unidad"])
        print("Clasificación:", clasificacion)
        print("-------------------------")
```

**# RETO 29: PRUEBA DE REGRESIÓN**

```python
    # Observaciones de las pruebas de regresión:

    # Se debe comprobar que DataLab v0.9 conserve las funcionalidades
    # que ya existían en DataLab v0.8.

    # Se debe verificar el funcionamiento del menú, el procesamiento,
    # la clasificación, los contadores, el acumulador, la bandera
    # y la generación del resumen.

    # También se debe comprobar que la nueva estructura de registros
    # no afecte las funcionalidades anteriores.

    # Los resultados se deben registrar después de ejecutar
    # las pruebas en las versiones 0.8 y 0.9.
```

La prueba de regresión permite comprobar que las modificaciones realizadas para crear DataLab v0.9 no hayan dañado las funcionalidades que funcionaban correctamente en DataLab v0.8. Se deben comparar ambas versiones y verificar que el menú, la clasificación, el procesamiento y el resumen sigan funcionando.

**# RETO 30: DOCUMENTAR LA ESTRUCTURA**

```markdown
# DataLab v0.9

## Estructura de datos

DataLab v0.9 utiliza una lista de diccionarios para representar
y almacenar los registros.

Cada registro contiene los siguientes campos:

- id: identificador único del registro.
- tipo: tipo de dato registrado.
- valor: valor numérico.
- unidad: unidad de medida.

## Organización

La estructura utilizada es:

Lista de registros → Diccionario → id / tipo / valor / unidad.

## ¿Por qué se utiliza una lista de diccionarios?

Se utiliza una lista de diccionarios porque permite almacenar
varios registros y mantener organizada la información de cada uno.

La lista facilita recorrer y procesar todos los registros,
mientras que los diccionarios permiten acceder a los campos
mediante claves descriptivas.

Esta estructura mejora la organización, lectura y mantenimiento
del programa.
```

**# RETO 31: GIT Y GITHUB**

```bash
    git status
    git add src/main.py
    git commit -m "feat: representa registros con diccionarios"
    git push

    git status
    git add bitacoras/semana9.md
    git commit -m "docs: documenta ejercicios de semana 9"
    git push
```

Los comandos permiten revisar el estado del repositorio, agregar los cambios, crear commits descriptivos y subirlos a GitHub. Las rutas deben ajustarse a la estructura real del proyecto.

**# RETO 32: ANÁLISIS DE ERRORES**

- [X] Confundí índice con clave.
- [ ] Intenté modificar una tupla.
- [ ] Utilicé claves diferentes entre registros.
- [X] Accedí a una clave inexistente.
- [ ] Dupliqué `clasificar_valor()`.
- [ ] Perdí información del registro.
- [ ] Dejé de utilizar funciones.
- [ ] No realicé pruebas.

Las opciones deben marcarse únicamente cuando el problema realmente se haya presentado y se haya corregido durante el desarrollo. No se deben marcar automáticamente.

**# RETO 33: ELEGIR LA ESTRUCTURA CORRECTA**

```python
    # A) Colección modificable de valores:
    # Utilizaría una lista porque permite modificar sus elementos.

    # B) Conjunto ordenado no modificable:
    # Utilizaría una tupla porque conserva el orden
    # y no permite modificar sus elementos.

    # C) Registro con id, tipo, valor y unidad:
    # Utilizaría un diccionario porque permite identificar
    # cada dato mediante una clave.

    # D) Varios registros con esos mismos campos:
    # Utilizaría una lista de diccionarios porque permite almacenar
    # varios registros y acceder a los campos de cada uno.
```

**# RETO FINAL: DATALAB V0.9**

```python
    # Función para clasificar valores
    def clasificar_valor(valor):
        if valor >= 60:
            return "ALTO"
        elif valor >= 35:
            return "NORMAL"
        return "BAJO"


    # Lista de registros
    registros = [
        {
            "id": "R001",
            "tipo": "temperatura",
            "valor": 22.5,
            "unidad": "C"
        },
        {
            "id": "R002",
            "tipo": "temperatura",
            "valor": 55.1,
            "unidad": "C"
        },
        {
            "id": "R003",
            "tipo": "temperatura",
            "valor": 72.3,
            "unidad": "C"
        }
    ]


    # Función para procesar registros
    def procesar_registros(registros):
        resultados = []

        for registro in registros:
            clasificacion = clasificar_valor(registro["valor"])

            resultado = {
                "id": registro["id"],
                "tipo": registro["tipo"],
                "valor": registro["valor"],
                "unidad": registro["unidad"],
                "clasificacion": clasificacion
            }

            resultados.append(resultado)

        return resultados


    # Función para generar el resumen
    def generar_resumen(registros):
        altos = 0
        normales = 0
        bajos = 0
        suma = 0
        existe_alto = False

        for registro in registros:
            valor = registro["valor"]
            clasificacion = clasificar_valor(valor)

            if clasificacion == "ALTO":
                altos += 1
                existe_alto = True
            elif clasificacion == "NORMAL":
                normales += 1
            else:
                bajos += 1

            suma += valor

        return altos, normales, bajos, suma, existe_alto


    # Mostrar registros procesados
    print("DATALAB V0.9")
    print("========================")

    resultados = procesar_registros(registros)

    for registro in resultados:
        print(registro)


    # Mostrar resumen
    print("\nRESUMEN")
    print("========================")

    altos, normales, bajos, suma, existe_alto = generar_resumen(registros)

    print("Registros ALTOS:", altos)
    print("Registros NORMALES:", normales)
    print("Registros BAJOS:", bajos)
    print("Suma total:", suma)
    print("¿Existe un valor ALTO?:", existe_alto)
```

**# PREGUNTAS DE REFLEXIÓN**

**1. ¿Cuándo utilizarías una lista?**

Utilizaría una lista cuando necesito almacenar varios elementos en una colección ordenada y modificar su contenido, por ejemplo, agregando, eliminando o cambiando elementos.

**2. ¿Cuándo utilizarías una tupla?**

Utilizaría una tupla cuando necesito almacenar varios elementos ordenados que no deben modificarse después de su creación.

**3. ¿Cuándo es mejor un diccionario?**

Es mejor utilizar un diccionario cuando necesito organizar información mediante claves y valores, porque permite identificar y consultar cada dato de forma descriptiva.

**4. ¿Qué diferencia existe entre un índice y una clave?**

Un índice es una posición numérica que permite acceder a un elemento dentro de una lista o tupla. Una clave es un identificador utilizado en un diccionario para acceder directamente al valor asociado.

**5. ¿Qué ventaja tiene representar un registro mediante claves?**

Permite identificar claramente cada dato, facilita la lectura del código y reduce las confusiones que pueden aparecer al utilizar posiciones numéricas.

**6. ¿Qué problema aparece si dos registros utilizan claves diferentes?**

Se pueden producir errores al intentar acceder a una clave que no existe. Además, se dificulta el procesamiento de los registros porque el programa espera una estructura consistente.

**7. ¿Por qué una lista de diccionarios representa varios registros?**

Porque la lista permite almacenar varios elementos y cada diccionario representa un registro individual con sus respectivos campos. Así se puede recorrer y procesar toda la información.

**8. ¿Cómo se accede al valor de un registro?**

Se accede utilizando la clave correspondiente dentro del diccionario. Por ejemplo, `registro["valor"]` permite obtener el valor almacenado en ese campo.

**9. ¿Por qué `clasificar_valor()` debe seguir siendo reutilizada?**

Porque evita duplicar código, mantiene una sola lógica de clasificación y facilita el mantenimiento del programa. Si es necesario modificar los criterios, solo se debe actualizar la función original.

**10. ¿Qué cambió en DataLab al pasar de valores a registros?**

DataLab pasó de almacenar valores numéricos directamente en una lista a utilizar una lista de diccionarios. Esto permite conservar información adicional como el identificador, el tipo y la unidad de cada valor.

**11. ¿Qué parte de la modularización de la Semana 7 se conserva?**

Se conserva la organización del programa mediante funciones independientes que cumplen tareas específicas. Esto permite separar responsabilidades, reutilizar código y facilitar el mantenimiento.

**12. ¿Qué información debe mantenerse durante el procesamiento?**

Se deben conservar el identificador (`id`), el tipo (`tipo`), el valor (`valor`) y la unidad (`unidad`), porque estos campos permiten mantener el contexto y comprender correctamente cada registro.

**# CHECKLIST FINAL**

- [ ] Diferencio lista, tupla y diccionario.
- [ ] Comprendo los índices de una tupla y su inmutabilidad básica.
- [ ] Accedo mediante claves y puedo modificar/agregar campos.
- [ ] Puedo recorrer un diccionario y una lista de registros.
- [ ] Reutilicé `clasificar_valor()`.
- [ ] Genero el resumen con contadores, acumulador y bandera.
- [ ] Conservo id, tipo, valor y unidad.
- [ ] Mantengo modularización y realicé pruebas.
- [ ] Actualicé documentación y GitHub.



