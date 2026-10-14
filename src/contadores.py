# Ciclo for para contar números positivos y negativos en una lista
numeros = [-1, -2, 3, 5 , 8 , 10, 0 , -9, -6]
contarNegativos = 0
contarPositivos = 0

for numero in  numeros:
  if(numero < 0):
    contarNegativos += 1
  elif (numero > 0):
    contarPositivos += 1

print(contarNegativos)
print(contarPositivos)

## Ciclo while para contar números positivos y negativos en una lista
numeros = [-1, -2, 3, 5 , 8 , 10, 0 , -9, -6]
contarNegativos = 0
contarPositivos = 0
i = 0

while i < len(numeros):
  numero = numeros[i]
  if numero < 0:
    contarNegativos += 1
  elif numero > 0:
    contarPositivos += 1
  i += 1

print(contarNegativos)
print(contarPositivos)