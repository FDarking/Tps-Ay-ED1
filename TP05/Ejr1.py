"""
Desarrollar una función para ingresar a través del teclado un número natural. La
función rechazará cualquier ingreso inválido de datos utilizando excepciones y
mostrará la razón exacta del error. Controlar que se ingrese un número, que ese
número sea entero y que sea mayor que 0, mostrando un mensaje con la razón
exacta del error en caso necesario. Devolver el valor ingresado cuando éste sea
correcto. Escribir también un programa que permita probar el correcto funcionamiento de la misma.
"""

def ingresar_numero():
    while True:
        numero = input("Ingrese un numero natural: ")
        try:
            numero = int(numero)
            if numero <= 0:
                raise ValueError("El numero debe ser mayor que 0.")
            return numero
        except ValueError as e:
            print(f"Error: {e}. Por favor ingrese un número valido.")

print("Numero ingresado:", ingresar_numero())
