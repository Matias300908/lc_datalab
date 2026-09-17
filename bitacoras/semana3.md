# Semana 3 de la bitacora
En esta semana se subiran todos los puntos a realizar de la tercera semana de el datalab (Invesigaciones, Pseudocodigo, Diagramas de flujo, Actualizaciones de codigo, ejenmplos y pruebas). *Esto con base a los puntos resueltos en la semana 2.*
## Punto 1
Aqui se subiran las respectivas investigaciones de este primer punto.
## Punto 2
En este punto se encontraran el pseudocodigo y el diagrama de flujo.
## Punto 3
Aqui se subiran las actualizaciones del codigo del DataLab junto a sus explicaciones respectivas de poque se realizo dicho cambio.
## Punto 4
En este ultimo punto se subiran los resultados, ejemplos y productos obtenidos despues de testear el codigo (Concluir los resultados obtenidos).

# Regla de numero de telefono:
telefono = ""
cantidad_digitos = 0

while cantidad_digitos != 10:
  telefono = input("Ingrese su número de telefono: ")
  print ("Tu número de telefono es:", telefono)
  cantidad_digitos = len(telefono)

  if cantidad_digitos == 10:
    print("Número de telefono correcto.")
  elif cantidad_digitos < 10:
    print(f"Su número de teléfono no es válido. Tiene {cantidad_digitos} dígitos. Por favor, ingrese un número de 10 dígitos.")
  else:
    print(f"El número de teléfono es incorrecto. Tiene {cantidad_digitos} dígitos. Por favor, ingrese un número de 10 dígitos.")