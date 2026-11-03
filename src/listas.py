def clasificar_valor(valor):
    if valor >= 60:
        return "ALTO"
    elif valor >= 35:
        return "NORMAL"
    return "BAJO"

def obtener_datos(cantidad):
    valores = []
    for i in range(cantidad):
        valor = float(input(f"Ingrese el valor {i+1}: "))
        valores.append(valor)
    return valores

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

def mostrar_resumen(altos, normales, bajos, suma, existe_alto):
    print("\n========= RESUMEN DATALAB v0.8 =========")
    print(f"Total registros clasificados ALTO:   {altos}")
    print(f"Total registros clasificados NORMAL: {normales}")
    print(f"Total registros clasificados BAJO:   {bajoso if 'bajos' in locals() else bajos}") # o la variable correspondiente
    print(f"Suma total acumulada:                {suma}")
    print(f"¿Existe algún valor ALTO?:           {'Sí' if existe_alto else 'No'}")
    print("========================================")

def main():
    print("Bienvenido a DataLab v0.8")
    cantidad = int(input("¿Cuántos valores desea registrar?: "))
    
    if cantidad <= 0:
        print("No hay valores para procesar (lista vacía).")
        return
        
    valores = obtener_datos(cantidad)
    altos, normales, bajos, suma, existe_alto = generar_resumen_completo(valores)
    mostrar_resumen(altos, normales, bajos, suma, existe_alto)

if __name__ == "__main__":
    main()