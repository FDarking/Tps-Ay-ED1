"""
Desarrollar una función eliminarclaves() que reciba como parámetros un diccionario
y una lista de claves. La función debe eliminar del diccionario todas las claves
contenidas en la lista, devolviendo el diccionario modificado y un número entero
que represente la cantidad de claves eliminadas. Desarrollar también un programa
para verificar su comportamiento.
"""
from typing import Dict, List, Tuple

def eliminarclaves(diccionario: Dict, claves: List) -> Tuple[Dict, int]:
    claves_eliminadas = 0
    for clave in claves:
        if clave in diccionario:
            del diccionario[clave]
            claves_eliminadas += 1
    return diccionario, claves_eliminadas

def main():
    diccionario = {"a": 1, "b": 2, "c": 3, "d": 4}
    claves = ["b", "c", "x"]
    diccionario_modificado, cantidad = eliminarclaves(diccionario, claves)
    print(f"Diccionario modificado: {diccionario_modificado}")
    print(f"Cantidad de claves eliminadas: {cantidad}")

if __name__ == "__main__":
    main()

