""" PORCIONES DE UNA LISTA 

SE DEBE PEDIR  AL USUARIO  QUE INGRESE NUMEROS  A UNA LISTA 

***********PARAMETROS*********
1.-LA LISTA NO TIENE TAMAÑO DEFINIDO (while)---LISTO
2.-SE DEBE PEDIR AL USUARIO QUE INGRESE UN NUMERO---LISTO
3.-SE DEBE DEJAR DE PEDIR NUMEROS CUANDO EL USUARIO INGRESE EL NUJMERO 0---LISTO
4.-SE DEBE MOSTRAR LA LISTA SEGUN POSICION ---LISTO
5.- SE DEBE MOSTRAR LA LISTA EN ORDEN INVERSO ---LISTO
6.- SE DEBE PARTIR LA LISTA EN 2 Y MOSTRAR AMBAS PARTES ---LISTO
7.- MUESTRA LOS ELEMENTOS DE LA PRIMERA MITAD EXCEPTUANDO EL PRIMERO Y EL ULTIMO
8.- MUESTRA EN PANTALLA DE LA SEGUNDA MITAD EL MAXIMO Y EL MINIMO


"""

## se declara la lista vacia, usamos el while para pedirle al usuario que ingrese numeros
## el while se declara con true para que se ejecute indefinidamente y se coloca la condicion con un if para romper el ciclo
lista = []
while True:
    numero = int(input("Ingrese un numero: "))
    lista.append(numero)
    if numero == 0:
        break

print("la lista ingresada es:",lista)

## se muestra la lista en orden inverso, para ello se utiliza el slicing (el slicing es una tecnica que se utiliza para obtener una porcion de una lista) con un paso de -1
print("la lista en orden inverso es:",lista[::-1])

tamaño_lista=len (lista)
print("el tamaño de la lista es:",tamaño_lista)

mitad_lista=tamaño_lista/2
print("la mitad de la lista es:",mitad_lista)

mitad_lista_redondeada=round(mitad_lista,0)
print("la mitad de la lista redondeada es:",mitad_lista_redondeada)
print("la primera mitad de la lista es:")
for i in range(int(mitad_lista_redondeada)):
    print(lista[i])
print("la segunda mitad de la lista es:")
for i in range(int(mitad_lista_redondeada),tamaño_lista):
    print(lista[i])

print("primera lista sin el primer y el ultimo elemento:")
for i in range(1,int(mitad_lista_redondeada)-1):
    print(lista[i])

# Se obtiene la segunda mitad de la lista usando slicing, desde el índice calculado hasta el final
segunda_mitad = lista[int(mitad_lista_redondeada):]

# Se verifica si la segunda mitad tiene elementos para evitar errores
if segunda_mitad:
    maximo = max(segunda_mitad)
    minimo = min(segunda_mitad)
    print("El máximo de la segunda mitad es:", maximo)
    print("El mínimo de la segunda mitad es:", minimo)
else:
    print("La segunda mitad está vacía, no hay máximo ni mínimo.")

    


