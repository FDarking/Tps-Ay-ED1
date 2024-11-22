"""
Desarrollar una función que devuelva una subcadena con los últimos N caracteres
de una cadena dada. La cadena y el valor de N se pasan como parámetros.
"""
def obtener_ultimos_caracteres(cadena, n):
    return cadena[-n:]
    
cadena = input("Ingresa una cadena: ")
n = int(input("Ingresa el número de caracteres a obtener: "))
print(obtener_ultimos_caracteres(cadena, n))
