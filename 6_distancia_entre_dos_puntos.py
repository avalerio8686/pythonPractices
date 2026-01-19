##Pide al usuario las coordenadas X e Y de dos puntos en el espacio.
##Muestra por pantalla la distancia en línea recta entre esos dos puntos.
##Muestra por pantalla las coordenadas del punto medio exacto de ambos.


from math import sqrt


y1=0.0
x1=0.0
y2=0.0
x2=0.0



y1=float(input("Ingrese Y1: "))
x1=float(input("Ingrese X1: "))
y2=float(input("Ingrese Y2: "))
x2=float(input("Ingrese X2: "))

calculo1=(x2-x1)**2
calculo2=(y2-y1)**2
calculo3=calculo1+calculo2
distancia=sqrt(calculo3)
print("La distancia entre los puntos es: ", distancia)

"""
que aprendi?

Debo importar la libreria y la funcion sqrt para poder usarla
la funcion sqrl me calcula la raiz cuadrada de un numero

"""