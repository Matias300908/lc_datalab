# Semana 3 de la bitacora
En esta semana se subiran todos los puntos a realizar de la tercera semana de el datalab (Invesigaciones, Pseudocodigo, Diagramas de flujo, Actualizaciones de codigo, ejenmplos y pruebas). *Esto con base a los puntos resueltos en la semana 2.*

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

# Match case nivel de educacion
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