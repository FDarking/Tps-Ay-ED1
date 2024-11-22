"""
Realizar una función que reciba como parámetros dos cadenas de caracteres 
conteniendo números reales, sume ambos valores y devuelva el resultado como un
número real. Devolver -1 si alguna de las cadenas no contiene un número válido,
utilizando manejo de excepciones para detectar el error.
"""
def sumar_numeros():
    cadena1 = input("Ingrese el primer numero real: ")
    cadena2 = input("Ingrese el segundo número real: ")

    try:
        num1 = float(cadena1)
        num2 = float(cadena2)
        return num1 + num2
    except ValueError:
        print("Error: Una de las cadenas no es un número valido.")
        return -1

resultado = sumar_numeros()
if resultado != -1:
    print("La suma es:", resultado)
else:
    print("Por favor ingrese números validos.")