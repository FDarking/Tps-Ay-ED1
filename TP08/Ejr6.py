"""
Ingresar una frase desde el teclado y usar un conjunto para eliminar las palabras
repetidas, dejando un solo ejemplar de cada una. Finalmente mostrar las palabras
ordenadas según su longitud. Los signos de puntuación no deben afectar el
proceso.
"""
from typing import Tuple

def encajan_fichas(ficha1: Tuple[int, int], ficha2: Tuple[int, int]) -> bool:
    if ficha1[0] == ficha2[0] or ficha1[0] == ficha2[1] or ficha1[1] == ficha2[0] or ficha1[1] == ficha2[1]:
        return True
    else:
        return False

def verificar_comportamiento():
    ficha1 = input("Ingrese la primera ficha (dos números separados por espacio): ").split()
    ficha2 = input("Ingrese la segunda ficha (dos números separados por espacio): ").split()
    
    ficha1 = (int(ficha1[0]), int(ficha1[1]))
    ficha2 = (int(ficha2[0]), int(ficha2[1]))
    
    if encajan_fichas(ficha1, ficha2):
        print("Las fichas encajan.")
    else:
        print("Las fichas no encajan.")

verificar_comportamiento()
