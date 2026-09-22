from validaciones_basicas import validar_nombre

for i in range(5):
    nombre = input(f"Ingrese el nombre {i + 1}: ")

    if validar_nombre(nombre):
        print("Nombre válido")
    else:
        print("Nombre inválido")