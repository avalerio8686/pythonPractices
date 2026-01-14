numeroEntero=""

numeroEntero=int(input("Ingrese un numero entero: "))
print("numeros existentes entre 1 y ", numeroEntero)
for i in range(1,numeroEntero+1):
    print( "x:",i)


print("numeros existentes entre ", numeroEntero, " y 30")
for j in range(30,numeroEntero-1,-1):
    print( "y:",j)