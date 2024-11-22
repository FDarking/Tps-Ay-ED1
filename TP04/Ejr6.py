"""
Desarrollar una función que extraiga una subcadena de una cadena de caracteres,
indicando la posición y la cantidad de caracteres deseada. Devolver la subcadena
como valor de retorno. Escribir también un programa para verificar el comportamiento 
de la misma. Ejemplo, dada la cadena "El número de teléfono es 4356-
7890" extraer la subcadena que comienza en la posición 25 y tiene 9 caracteres,
resultando la subcadena "4356-7890". Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""

def utiliza_rebanadas(cadena, posicion, cantidad):
    subcadena = cadena[posicion:posicion + cantidad]
    return subcadena

def No_utiliza_rebanadas(cadena, posicion, cantidad):
    subcadena = ""
    i = posicion
    while i < posicion + cantidad and i < len(cadena):
        subcadena += cadena[i]
        i += 1
    return subcadena

cadena_usuario = input("Ingresa la cadena de texto: ")
posicion_usuario = int(input("Ingresa la posición inicial: "))
cantidad_usuario = int(input("Ingresa la cantidad de caracteres a extraer: "))

subcadena_rebanadas = utiliza_rebanadas(cadena_usuario, posicion_usuario, cantidad_usuario)
print("Subcadena usando rebanadas:", subcadena_rebanadas)

subcadena_sin_rebanadas = No_utiliza_rebanadas(cadena_usuario, posicion_usuario, cantidad_usuario)
print("Subcadena sin usar rebanadas:", subcadena_sin_rebanadas)

