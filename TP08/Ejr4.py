"""
Escribir una función que indique si dos fichas de dominó encajan o no. Las fichas
son recibidas en dos tuplas, por ejemplo: (3, 4) y (5, 4). La función devuelve True
o False. Escribir también un programa para verificar su comportamiento. Considerar
el uso de conjuntos para resolver este ejercicio.
"""
from typing import Tuple

def encajan_fichas(ficha1: Tuple[int, int], ficha2: Tuple[int, int]) -> bool:
    conjunto_ficha1 = set(ficha1)
    conjunto_ficha2 = set(ficha2)
    
    if conjunto_ficha1 & conjunto_ficha2:
        return True
    else:
        return False

def verificar_comportamiento():
    print("Verificador de fichas de dominó")
    
    try:
        ficha1 = tuple(map(int, input("Ingrese la primera ficha (dos números separados por espacio): ").split()))
        ficha2 = tuple(map(int, input("Ingrese la segunda ficha (dos números separados por espacio): ").split()))
        
        if len(ficha1) != 2 or len(ficha2) != 2:
            print("Error: cada ficha debe tener exactamente dos números.")
            return
        
        print(f"Ficha 1: {ficha1}")
        print(f"Ficha 2: {ficha2}")
        
        if encajan_fichas(ficha1, ficha2):
            print("Las fichas encajan.")
        else:
            print("Las fichas no encajan.")
    except ValueError:
        print("Error: Por favor ingrese solo números enteros separados por espacio.")
        
def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Verificar si las fichas encajan")
        print("2. Salir")
        opcion = input("Seleccione una opción (1 o 2): ")

        if opcion == '1':
            verificar_comportamiento()
        elif opcion == '2':
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida, por favor elija 1 o 2.")

menu()
