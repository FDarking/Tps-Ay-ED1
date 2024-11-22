"""
Generar e imprimir un diccionario donde las claves sean números enteros entre 1 y
20 (ambos incluidos) y los valores asociados sean el cuadrado de las claves.
"""
from typing import Dict

def generar_diccionario() -> Dict[int, int]:
    return {i: i ** 2 for i in range(1, 21)}

def main() -> None:
    for clave, valor in generar_diccionario().items():
        print(f"{clave}: {valor}")

if __name__ == "__main__":
    main()
