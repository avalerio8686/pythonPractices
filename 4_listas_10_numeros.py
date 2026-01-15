lista = []
cont = 0

for i in range(10):
    valor = int(input("Digite un numero: "))
    lista.append(valor)
    if valor < 0:
        cont += 1

print("Los numeros ingresados son:")
for valor in lista:
    print(valor)

print("La cantidad de numeros negativos es:", cont, "y son los siguientes:")
for valor in lista:
    if valor < 0:
        print(valor)