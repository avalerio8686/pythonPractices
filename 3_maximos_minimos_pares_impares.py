numero1=""
numero2=""
numero3=""

numero1=int(input("Ingrese el primer numero: "))
numero2=int(input("Ingrese el segundo numero: "))
numero3=int(input("Ingrese el tercer numero: "))

if (numero1>numero2) and (numero1>numero3):
    print("El numero mayor es: ", numero1)
elif (numero2>numero1) and (numero2>numero3):
    print("El numero mayor es: ", numero2)
else:
    print("El numero mayor es: ", numero3)

if (numero1<numero2) and (numero1<numero3):
    print("El numero menor es: ", numero1)
elif (numero2<numero1) and (numero2<numero3):
    print("El numero menor es: ", numero2)
else:
    print("El numero menor es: ", numero3)

if(numero1%2==0):
    print("El numero ", numero1, " es par")
else:
    print("El numero ", numero1, " es impar")

if(numero2%2==0):
    print("El numero ", numero2, " es par")
else:
    print("El numero ", numero2, " es impar")

if(numero3%2==0):
    print("El numero ", numero3, " es par")
else:
    print("El numero ", numero3, " es impar")