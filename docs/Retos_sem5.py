# Reto 1

def contar_edades_validas():

    contador = 0

    
    print("--- Registro de Edades DataLab ---")
    print("Ingresa las edades una por una. Escribe un número negativo para finalizar.\n")
    
    while True:
      
        edad = int(input("Ingresa una edad: "))
        
      
        if edad < 0:
            print("\n¡Captura finalizada!")
            break
            
        
        contador += 1
        
   
    print(f"Total de edades válidas ingresadas: {contador}")
    return contador


contar_edades_validas()

# Reto 2    

for sensor in range(1, 11):
    print(f"Sensor {sensor}: Temperatura procesada")

print("Lote completo")

# Reto 3

while True:
    contraseña = input("Ingrese la contraseña: ")

    if contraseña == "Data2026":
        print("Acceso concedido")
        break
    else:
        print("Acceso denegado, intente de nuevo")

# Reto 4

valores = [10, 55, 2, 80, 15, 100, 40]

for valor in valores:
    if valor > 50:
        print(valor)
    else:
        print("Valor descartado")