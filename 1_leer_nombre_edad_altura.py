miNombre=""
miEdad=0
miAltura=0.0

miNombre=input("Por favor, ingrese su nombre: ")
miEdad=int(input("Por favor, ingrese su edad: "))
miAltura=float(input("Por favor, ingrese su altura: "))

entero=int(miAltura)
miFloat=int((miAltura-entero)*100)




print("El usuario se llama:", miNombre, "y tiene", miEdad, "años y mide", entero, "metros y", miFloat, "centímetros.")