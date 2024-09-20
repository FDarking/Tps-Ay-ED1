"""
Desarrollar una función que determine si una cadena de caracteres es capicúa, sin
utilizar cadenas auxiliares ni rebanadas. Escribir además un programa que permita
verificar su funcionamiento.
"""
def es_capicua(cadena):
    inicio = 0
    fin = len(cadena) - 1
    
    while inicio < fin:
        if cadena[inicio] != cadena[fin]:
            return False
        inicio += 1
        fin -= 1
    
    return True

# Programa para verificar el funcionamiento
if __name__ == "__main__":
    cadena = input("Ingrese una cadena de caracteres: ")
    if es_capicua(cadena):
        print(f"La cadena '{cadena}' es capicúa.")
    else:
        print(f"La cadena '{cadena}' no es capicúa.")
