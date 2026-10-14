"# Acumuladores"
numeros = [-1, -2, 3, 5 , 8 , 10, 0 , -9, -6]
contarNegativos = 0
contarPositivos = 0
sumaNegativos = 0
sumaPositivos = 0

for numero in  numeros:
  if(numero < 0):
    sumaNegativos = sumaNegativos + numero
    contarNegativos += 1
  elif (numero > 0):
    sumaPositivos = sumaPositivos + numero
    contarPositivos += 1

print(contarNegativos)
print(contarPositivos)
print(sumaNegativos)
print(sumaPositivos)