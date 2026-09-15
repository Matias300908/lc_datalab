# Bitacora semana 2

## 1. Analizar la regla
Imagina que DataLab es una pequeña máquina inteligente en una fábrica de clasificación de paquetes:

1. La Entrada: Es la información que le entregas al sistema para que empiece a trabajar. Siguiendo la analogía, es un paquete que llega con datos escritos: su peso, su tamaño y su dirección.

2. Las Reglas: Son las preguntas lógicas que la máquina le hace a esos datos para saber qué hacer con ellos. Por ejemplo: "¿El paquete pesa más de 5 kilos? ¿Va para otra ciudad?".

3. La Salida: Es la decisión final o clasificación que obtienes después de que la máquina evalúa las reglas. En este caso, la salida es la etiqueta final que se le pega al paquete: "Envío Express" o "Envío Económico".

En resumen: le das datos, el sistema evalúa preguntas lógicas y te devuelve una clasificación o resultado listo para usar.

## 2. Diseñar la Solucion
### Pseudocodigo
Algoritmo DataLab_Semana1
    Imprimir "=== DataLab | Semana 1 ==="
    Imprimir "Primera versión del procesamiento de un registro."
    
    // 1. ENTRADA DE DATOS
    Imprimir "Ingrese el identificador del registro: "
    Leer registro_id
    
    Imprimir "Ingrese el valor del registro: "
    Leer valor
    
    // 2. REGLAS Y CONDICIONES (Diferentes caminos)
    Si valor >= 50 Entonces
        clasificacion = "ALTO"       // Camino Verdadero
    Sino
        clasificacion = "NORMAL"     // Camino Falso
    Fin Si
    
    // 3. SALIDA DE RESULTADOS
    Imprimir "\nResultado"
    Imprimir "Registro: ", registro_id
    Imprimir "Valor: ", valor
    Imprimir "Clasificación: ", clasificacion
Fin Algoritmo
 ### Diagrama de flujo

[ Inicio ]
           │
           ▼
   ( Imprimir Título )
           │
           ▼
┌───────────────────────┐
│ Leer: registro_id     │  <-- ENTRADA
│ Leer: valor           │
└───────────────────────┘
           │
           ▼
    < ¿valor >= 50? >      <-- CONDICIÓN
     /             \
    / (Sí)          \ (No)
   ▼                 ▼
┌──────────────┐   ┌──────────────┐
│ clasificacion│   │ clasificacion│
│ = "ALTO"     │   │ = "NORMAL"   │
└──────────────┘   └──────────────┘
    \                 /
     \               /
      ►             ◄
           │
           ▼
┌───────────────────────┐
│ Imprimir Resultados   │  <-- SALIDA
│ (ID, Valor, Clase)    │
└───────────────────────┘
           │
           ▼
        [ Fin ]

## 3.Implementar estructuras condicionales

Durante esta semana, el objetivo principal fue evolucionar el script de DataLab. Pasamos de una validación simple de dos caminos (if/else) a un sistema de control de flujo más robusto y detallado utilizando la estructura anidada de if, elif y else.

### ¿Que cambios de implementaron?
Se rediseñó el bloque de decisión para evaluar múltiples escenarios y rangos numéricos con precisión, cumpliendo con las siguientes condiciones:

Valor por debajo del límite: Detecta cuando el registro es inferior al umbral mínimo (valor < 10).

Valor exacto en el límite: Identifica casos frontera exactos (valor == 10 o valor == 50).

Valor dentro del rango esperado: Evalúa los datos que se encuentran en el intervalo normal de operación (10 < valor < 50).

Valor que supera el límite: Clasifica aquellos registros que exceden los parámetros permitidos.

La lógica condicional aplicada en el script para evaluar estas categorías es la siguiente:


    if valor < 10:
        clasificacion = "BAJO (Por debajo del límite)"
    elif valor == 10 or valor == 50:
        clasificacion = "EN LÍMITE"
    elif 10 < valor < 50:
        clasificacion = "NORMAL (Dentro del rango esperado)"
    else:
        clasificacion = "ALTO (Supera el límite establecido)"
Nota: El código fuente completo y actualizado se encuentra ubicado en la carpeta src, específicamente en el archivo main 2.py.

## Realizar pruebas 
Pruebas y Validación de la Lógica (Semana 2)
Para comprobar el correcto funcionamiento de las reglas implementadas con estructuras condicionales avanzadas (if, elif, else), se realizaron pruebas de validación enfocadas especialmente en los casos frontera y los diferentes rangos de valores.

A continuación se documentan dos de las pruebas ejecutadas en el sistema:

1. Prueba de Caso de Límite (Frontera)
Descripción: Se probó el comportamiento del script al introducir un valor que coincide exactamente con uno de los límites establecidos (en este caso, 50).

Ejecución y Resultado: Al ingresar el identificador REG-001 con un valor de 50, el sistema evaluó la condición exacta de frontera (valor == 50) y devolvió de manera correcta la etiqueta EN LÍMITE, demostrando que maneja adecuadamente los puntos de corte numéricos.

2. Prueba de Caso Normal
Descripción: Se validó el comportamiento del script con un valor que se encuentra de forma intermitente dentro de los parámetros esperados, pero sin tocar los extremos.

Ejecución y Resultado: Al ingresar el identificador REG-002 con un valor de 25, el programa determinó que cumplía con la regla de intervalo (10 < valor < 50) y emitió la clasificación NORMAL (Dentro del rango esperado).

*Nota: El ejemplo se encuentrea en la carpeta src, especificamente en ejmeplos.py*

