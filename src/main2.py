def main():
    print("=== DataLab | Semana 1 ===")
    print("Versión actualizada del procesamiento de un registro.")

    registro_id = input("Ingrese el identificador del registro: ")
    valor = float(input("Ingrese el valor del registro: "))

    # Reglas evaluadas con if, elif y else:
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