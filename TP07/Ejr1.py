"""
Escribir una función que devuelva la cantidad de dígitos de un número entero, sin
utilizar cadenas de caracteres.
"""
def contar_digitos(numero):
    if numero < 10:
        return 1
    else:
        return 1 + contar_digitos(numero // 10)

numero = int(input("Ingresa un número entero: "))
print(f"La cantidad de dígitos es: {contar_digitos(numero)}")
