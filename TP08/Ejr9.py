"""
Escribir un programa que permita ingresar un número entero N y genere un
diccionario por comprensión con la tabla de multiplicar de N del 1 al 12. Mostrar la
tabla de multiplicar con el formato apropiado.
"""
from typing import Dict

def generar_tabla_multiplicar(n: int) -> Dict[int, int]:
    return {i: n * i for i in range(1, 13)}

def mostrar_tabla(tabla: Dict[int, int], n: int):
    print(f"Tabla de multiplicar del {n}:")
    for k, v in tabla.items():
        print(f"{n} x {k} = {v}")

def main():
    n = int(input("Ingresa un número entero: "))
    tabla = generar_tabla_multiplicar(n)
    mostrar_tabla(tabla, n)

if __name__ == "__main__":
    main()
