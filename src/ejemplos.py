PI = 3.1416
radio = 4

## EJEMPLO SEMANA 2

def main():
    print("=== DataLab | Semana 2 ===")
    print("Procesamiento de un registro con múltiples condiciones.")

    registro_id = input("Ingrese el identificador del registro: ")
    valor = float(input("Ingrese el valor del registro: "))

    # Reglas evaluadas con if, elif y else para todos los casos (Bajo, Límite, Normal, Alto):
    if valor < 10:
        clasificacion = "BAJO (Por debajo del límite)"
    elif valor == 10 or valor == 50:
        clasificacion = "EN LÍMITE"
    elif 10 < valor < 50:
        clasificacion = "NORMAL (Dentro del rango esperado)"
    else:
        clasificacion = "ALTO (Supera el límite establecido)"

    print("\nResultado")
    print(f"Registro: {registro_id}")
    print(f"Valor: {valor}")
    print(f"Clasificación: {clasificacion}")


if __name__ == "__main__":
    main()

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
