"""
Escribir una función para eliminar una subcadena de una cadena de caracteres, a
partir de una posición y cantidad de caracteres dadas, devolviendo la cadena resultante. 
Escribir también un programa para verificar el comportamiento de la misma.
Escribir una función para cada uno de los siguientes casos:
a. Utilizando rebanadas
b. Sin utilizar rebanadas
"""
def eliminar_subcadena_rebanada(cadena, posicion, cantidad):
    return cadena[:posicion] + cadena[posicion + cantidad:]

def eliminar_subcadena_sin_rebanadas(cadena, posicion, cantidad):
    nueva_cadena = ''
    for i in range(len(cadena)):
        if i < posicion or i >= posicion + cantidad:
            nueva_cadena += cadena[i]
    return nueva_cadena

cadena = input("Ingresa una cadena de caracteres: ")
posicion = int(input("Ingresa la posición desde donde comenzar a eliminar: "))
cantidad = int(input("Ingresa la cantidad de caracteres a eliminar: "))

resultado_rebanada = eliminar_subcadena_rebanada(cadena, posicion, cantidad)
print("Cadena resultante (usando rebanadas):", resultado_rebanada)

resultado_sin_rebanada = eliminar_subcadena_sin_rebanadas(cadena, posicion, cantidad)
print("Cadena resultante (sin usar rebanadas):", resultado_sin_rebanada)
