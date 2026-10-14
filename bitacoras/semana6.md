# SEMANA 6
 Contadores, acumuladores y banderas en DataLab v0.6
1. Datos generales
- Proyecto integrador: DataLab.
- Curso: Lógica Computacional.
- Programa: Ingeniería de Datos e Inteligencia Artificial.
- Semana: 6 de 14.
- Modalidad: Trabajo individual.
- Tema: Contadores, acumuladores y banderas o variables de estado.
2. Punto de partida
DataLab ha evolucionado para tomar decisiones, validar entradas, procesar múltiples registros mediante ciclos for y mantener un menú repetitivo mediante while.
En esta semana se busca que el programa no solamente procese datos, sino que también conserve información sobre lo ocurrido durante el procesamiento. Para conseguirlo, se utilizan contadores, acumuladores y banderas, que permiten contar registros, sumar valores y recordar si se presentó una condición determinada.
De esta manera, DataLab puede generar resúmenes más completos y útiles.
3. Procesar y recordar
DataLab debe ser capaz de procesar varios registros y generar un resumen que muestre la cantidad total de registros, cuántos pertenecen a cada clasificación, la suma de sus valores y si se presentó al menos un registro clasificado como ALTO.
Las preguntas principales que se deben resolver son:
- ¿Cuántos registros se procesaron?
- ¿Cuántos registros pertenecen a cada categoría?
- ¿Cuál es la suma de los valores procesados?
- ¿Ocurrió al menos una situación determinada?
- ¿Qué información se debe mantener durante el ciclo?
Para responderlas, se utilizan variables que conservan sus valores entre las iteraciones del ciclo y se actualizan cada vez que se procesa un registro.
4. Contadores
Un contador es una variable que permite registrar cuántas veces ocurre un evento. Generalmente comienza en cero y aumenta en una unidad cada vez que se cumple una condición.
Los contadores permiten conocer la cantidad de registros procesados, cuántos números son positivos o negativos y cuántos elementos pertenecen a una categoría determinada.
Idea clave: un contador responde a la pregunta «¿cuántos ocurrieron?».
5. Acumuladores
Un acumulador es una variable que conserva la suma progresiva de diferentes valores. A diferencia de un contador, no aumenta necesariamente de uno en uno, sino que agrega el valor que se está procesando.
Los acumuladores permiten calcular totales, sumar cantidades por categoría y obtener información estadística de los registros.
Idea clave: un acumulador responde a la pregunta «¿cuál es el total acumulado?».
6. Contador vs. acumulador
Característica	Contador	Acumulador
Propósito	Contar eventos.	Sumar o acumular valores.
Valor inicial	Generalmente cero.	Generalmente cero.
Actualización	Aumenta normalmente en uno.	Agrega el valor procesado.
Pregunta que responde	¿Cuántos ocurrieron?	¿Cuál es el total?
La diferencia principal es que el contador registra la cantidad de veces que ocurre una condición, mientras que el acumulador conserva el resultado de sumar varios valores. Ambos pueden utilizarse simultáneamente para obtener información más completa.
7. Banderas o variables de estado
Una bandera es una variable que permite recordar si ocurrió una situación específica durante la ejecución del programa. Normalmente utiliza valores booleanos: True para indicar que la condición se cumplió y False para indicar que todavía no se ha cumplido.
La bandera se inicializa en False y cambia a True cuando se encuentra la condición buscada. Una vez activada, permanece en True, aunque se procesen otros registros.
Las banderas son útiles para recordar si existe un valor determinado, si se encontró un error o si ocurrió alguna condición importante durante el procesamiento.
8. Diseñar las variables antes de programar
Antes de construir el programa, es necesario identificar qué información se necesita conservar y qué mecanismo permite hacerlo.
Necesidad	Mecanismo
Contar registros procesados	Contador
Contar registros de una categoría	Contador
Sumar los valores procesados	Acumulador
Recordar si ocurrió una condición	Bandera
Las preguntas que se deben resolver antes de programar son:
1. ¿Qué necesito contar? La cantidad de registros y los que pertenecen a cada categoría.
2. ¿Qué necesito sumar? Los valores de los registros procesados.
3. ¿Qué necesito recordar? Si ocurrió una condición específica, como encontrar un registro ALTO.
4. ¿Cuál debe ser el valor inicial? Los contadores y acumuladores comienzan generalmente en cero, mientras que las banderas comienzan en False.
5. ¿Cuándo se actualiza cada variable? Durante el ciclo, cuando se procesa un registro o se cumple la condición correspondiente.
9. Inicialización
La inicialización consiste en asignar un valor inicial a las variables antes de comenzar el ciclo. Es importante hacerlo correctamente para que el programa pueda conservar la información durante todo el procesamiento.
Los contadores y acumuladores generalmente comienzan en cero, mientras que las banderas comienzan en False.
Si las variables se inicializan dentro del ciclo, pueden reiniciarse en cada iteración y perder los resultados obtenidos anteriormente. Por esta razón, deben declararse antes del ciclo, mientras que sus actualizaciones deben realizarse dentro de él.
10. Actualización dentro del ciclo
La actualización ocurre cada vez que el programa procesa un registro. En ese momento, los contadores aumentan, los acumuladores reciben los valores correspondientes y las banderas cambian cuando se cumple una condición.
El flujo de procesamiento es el siguiente:
1. Recibir un registro.
2. Actualizar el contador total.
3. Acumular el valor.
4. Clasificar el registro.
5. Actualizar el contador de su categoría.
6. Activar la bandera si se cumple la condición.
7. Continuar con el siguiente registro hasta terminar.
Este procedimiento permite conservar los resultados de todas las iteraciones y utilizarlos para generar un resumen final.
11. Integración con la clasificación
DataLab debe reutilizar la función de clasificación que ya existe en el proyecto, evitando repetir innecesariamente la lógica para determinar si un valor es ALTO, NORMAL o BAJO.
La función de clasificación recibe un valor y devuelve la categoría correspondiente. Posteriormente, el programa actualiza el contador de esa categoría y activa la bandera cuando encuentra un registro ALTO.
Esta integración facilita el mantenimiento del programa, evita duplicar instrucciones y permite que los resultados del procesamiento sean consistentes con las reglas de clasificación previamente definidas.
12. Resumen del procesamiento
El resumen permite presentar los resultados obtenidos después de procesar todos los registros. Debe mostrar:
- Total de registros procesados.
- Cantidad de registros ALTO.
- Cantidad de registros NORMAL.
- Cantidad de registros BAJO.
- Suma total de los valores.
- Estado de la bandera que indica si existe algún registro ALTO.
Los resultados se calculan durante la ejecución del programa y se muestran al finalizar el ciclo. De esta forma, el resumen representa los datos realmente procesados, en lugar de utilizar cantidades escritas manualmente.
13. Consistencia de resultados
La consistencia permite comprobar que los resultados calculados por el programa sean coherentes. Cuando cada registro pertenece a una sola de las tres categorías, la suma de los contadores de ALTO, NORMAL y BAJO debe coincidir con el total de registros.
La relación es:
ALTO + NORMAL + BAJO = TOTAL
Por ejemplo, si existen tres registros ALTO, cinco NORMAL y dos BAJO, el total debe ser diez.
Esta comprobación permite detectar errores como registros que no fueron clasificados, contadores que se actualizaron incorrectamente o condiciones que no contemplan todos los casos.
14. Ejemplo conceptual completo
El procesamiento de DataLab comienza con la inicialización de los contadores, el acumulador y la bandera. Después, el ciclo recorre todos los valores disponibles, cuenta cada registro y suma su valor.
Posteriormente, cada registro se clasifica como ALTO, NORMAL o BAJO. Según el resultado, se incrementa el contador correspondiente. Si se encuentra un registro ALTO, la bandera cambia a True.
Al finalizar el ciclo, el programa presenta el resumen con el total de registros, las cantidades por categoría, la suma de los valores y el estado de la bandera. Finalmente, comprueba que la suma de los contadores por categoría coincida con el total procesado.
Este procedimiento integra los tres conceptos principales de la semana y permite que DataLab conserve información durante la ejecución.
15. Pruebas
Para comprobar el funcionamiento de DataLab, se deben utilizar diferentes conjuntos de datos y verificar que los contadores, acumuladores y banderas produzcan resultados correctos.
Prueba	Condición	Resultado que se debe verificar
Todos NORMAL	Todos los registros tienen clasificación NORMAL.	El contador NORMAL coincide con el total y la bandera es False.
Un ALTO	Existe un único registro ALTO.	El contador ALTO es uno y la bandera es True.
Varios ALTO	Existen varios registros ALTO.	El contador ALTO registra la cantidad correcta.
Todos BAJO	Todos los registros tienen clasificación BAJO.	El contador BAJO coincide con el total.
Datos mixtos	Existen registros de las tres categorías.	Los contadores suman el total de registros.
Suma conocida	Se procesan valores cuya suma se conoce.	El acumulador coincide con el resultado esperado.
Además, se deben comprobar los siguientes aspectos:
- El conteo total coincide con la cantidad de registros procesados.
- Los contadores por categoría reflejan las clasificaciones reales.
- El acumulador contiene la suma correcta.
- La bandera cambia a True cuando ocurre el evento buscado.
- La suma de los contadores por categoría coincide con el total.
Prueba basada en las imágenes
En las imágenes se utiliza una lista de nueve números: cuatro negativos, cuatro positivos y un cero.
Los resultados obtenidos son:
Operación	Resultado
Cantidad de negativos	4
Cantidad de positivos	4
Suma de negativos	-18
Suma de positivos	26
El número cero no se cuenta como positivo ni negativo porque no cumple ninguna de las dos condiciones.
Tanto el ciclo for como el ciclo while producen los mismos resultados. La diferencia es que for recorre directamente los elementos de la lista, mientras que while utiliza un índice para acceder a cada elemento y necesita incrementarlo para avanzar.
16. Git y GitHub
Git permite registrar los cambios realizados en el proyecto, mientras que GitHub permite almacenar y compartir el repositorio de forma remota.
Antes de comenzar, se debe comprobar el estado del repositorio y actualizar la copia local. Después de implementar el resumen del procesamiento, se pueden registrar los cambios realizados en el archivo principal y en la documentación.
Este proceso permite conservar un historial de modificaciones, identificar los avances realizados y compartir el trabajo con otros integrantes del proyecto cuando corresponda.
17. Pensamiento crítico
1. ¿Cuál es la diferencia entre contar y acumular?
Contar consiste en registrar cuántas veces ocurre un evento, generalmente aumentando una variable en uno. Acumular consiste en sumar progresivamente diferentes valores para obtener un total. Por ejemplo, un contador permite saber cuántos números negativos existen y un acumulador permite conocer la suma de esos números.
2. ¿Por qué las variables deben inicializarse antes del ciclo?
Porque deben comenzar con un valor inicial definido y conservar la información durante todas las iteraciones. Si se inicializan dentro del ciclo, pueden reiniciarse continuamente y perder los resultados anteriores, haciendo que el programa produzca un resumen incorrecto.
3. ¿Qué problema resuelve una bandera?
Una bandera permite recordar si ocurrió una situación específica durante el procesamiento. Por ejemplo, permite determinar si se encontró al menos un registro ALTO sin necesidad de almacenar todos los registros que cumplen esa condición.
4. ¿Qué ocurre si el contador se reinicia dentro del ciclo?
El contador vuelve a su valor inicial en cada iteración y pierde el conteo anterior. Como consecuencia, no registra correctamente la cantidad total de eventos y puede terminar mostrando un resultado incorrecto.
5. ¿Cómo comprobarías que el resumen es correcto?
Compararía el total de registros procesados con la cantidad de elementos de la lista, verificaría que los contadores por categoría sumen el total y comprobaría el acumulador utilizando una suma conocida. También probaría diferentes conjuntos de datos para confirmar que la bandera cambia correctamente.
6. ¿Qué información es útil conservar al procesar muchos registros?
Es útil conservar el total de registros procesados, la cantidad de elementos de cada categoría, la suma de los valores y el estado de condiciones importantes. Esta información facilita el análisis de los datos, la detección de errores y la generación de informes que permitan tomar decisiones.
18. Evolución de DataLab
DataLab v0.6 — Procesamiento con estado y resumen
En esta versión, DataLab incorpora mecanismos para mantener información durante el procesamiento de múltiples registros. Los contadores permiten conocer la cantidad de elementos procesados y clasificados, los acumuladores calculan totales y las banderas recuerdan si ocurrió una situación determinada.
La estructura del proyecto queda organizada conceptualmente de la siguiente manera:
- Clasificación.
- Selección de operaciones.
- Validación de entradas.
- Procesamiento de múltiples registros.
- Menú repetitivo.
- Resumen del procesamiento:
  - Contadores.
  - Acumuladores.
  - Banderas.
Esta evolución permite que DataLab pase de ejecutar operaciones individuales a procesar información y conservar resultados durante la ejecución. De esta manera, el programa puede presentar resúmenes, verificar la consistencia de los datos y recordar las condiciones que se presentaron.
La siguiente etapa consiste en organizar esta lógica mediante funciones, con el propósito de mejorar la modularidad, facilitar el mantenimiento del código y reutilizar las operaciones sin duplicar instrucciones.
Conclusión de la semana 6
Durante esta semana aprendí que los contadores, acumuladores y banderas son fundamentales para procesar y conservar información en un programa. Los contadores permiten registrar cantidades, los acumuladores calculan sumas progresivas y las banderas permiten recordar si se cumple una condición. Al utilizarlos dentro de ciclos for y while, DataLab puede procesar varios registros, clasificar sus valores y generar resúmenes con resultados verificables. También comprendí la importancia de inicializar las variables antes de los ciclos y comprobar la consistencia de los resultados para evitar errores. Estos conceptos representan un avance importante en el desarrollo de DataLab v0.6 y preparan el proyecto para organizar su lógica mediante funciones en las siguientes semanas.