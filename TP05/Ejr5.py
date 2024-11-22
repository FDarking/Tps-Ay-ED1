"""
La raíz cuadrada de un número puede obtenerse mediante la función sqrt() del
módulo math. Escribir un programa que utilice esta función para calcular la raíz
cuadrada de un número cualquiera ingresado a través del teclado. El programa
debe utilizar manejo de excepciones para evitar errores si se ingresa un número
negativo.
"""

import math

def calcular_raiz():
    try:
        numero = float(input("Ingrese un numero para calcular su raiz cuadrada: "))
        if numero < 0:
            raise ValueError("No se puede calcular la raiz cuadrada de un numero negativo.")
        return math.sqrt(numero)
    except ValueError as e:
        print(f"Error: {e}")
        return None

resultado = calcular_raiz()
if resultado is not None:
    print("La raiz cuadrada es:", resultado)
else:
    print("Por favor ingrese un número valido.")
