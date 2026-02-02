""" Los conjuntos son coleeciones desordenadas de elementos, es decir, no tienen un orden establecido y no se repiten los elementos

los diccionarios son coleeciones ordenadas de elementos, es decir, tienen un orden establecido y no se repiten los elementos """

auto= {

"marca":"Renault",
"modelo":"Kwid",
"color":"Rojo",
"año":2022
}

print(auto)
print(auto["marca"])
print(auto.get("modelo"))
print(auto.keys())
print(auto.values()) 

print(auto.items())##Imprime los elementos del diccionario
auto.pop("color")##Elimina el elemento color
auto.popitem()##Elimina el ultimo elemento
auto.clear()##Elimina todos los elementos
print(auto)



##diccionarios anidados, esto es un diccionario dentro de otro y sirve para agrupar datos , un ejemplo es:
familia={
    "padre":"Juan",
    "madre":"Maria",
    "hijo1":{
        "nombre":"Pedro",
        "edad":20
    },
    "hijo2":{
        "nombre":"Juan",
        "edad":15
    }
}

print(familia["hijo1"])



