# Banderas
numeros = [-1, -2, 3, 5 , 8 , 10, 6 , -9, -6, 6, -9, -1, 4, 6, 1, 5, 8, -2, -6]
contarNegativos = 0
contarPositivos = 0
salir = False

for numero in  numeros:
  if(numero < 0):
    contarNegativos += 1
  elif (numero > 0):
    contarPositivos += 1
  else:
    salir = True
    break

print(contarNegativos)
print(contarPositivos)

## Deteccion de numeros negativos y positivos en una lista con ciclo while
numeros = [-1, -2, 3, 5 , 8 , 10, 6 , -9, -6, 6, -9, -1, 4, 6, 1, 5, 8, -2, -6]
numerosBuenos = 0
numerosMalos = 0
i = 0
salir = True

while i < len(numeros) and salir:
  if (numeros[i] > 0):
    numerosBuenos = numerosBuenos + 1
  else:
    numerosMalos = numerosMalos + 1

  if numerosMalos >= 3:
    salir = False
    print("Muchos numeros malos")
    #break
  i += 1

print(contarNegativos)
print(contarPositivos)

print("Buenos:",numerosBuenos)

