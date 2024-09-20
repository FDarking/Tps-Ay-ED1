"""
Escribir una función que reciba una lista de números enteros como parámetro y la
normalice, es decir que todos sus elementos deben sumar 1.0, respetando las proporciones 
relativas que cada elemento tiene en la lista original. Desarrollar también
un programa que permita verificar el comportamiento de la función. Por ejemplo,
normalizar([1, 1, 2]) debe devolver [0.25, 0.25, 0.50].
"""
import random as rn

def cargar_lista() -> list:
    lista = []
    cantidad = rn.randint(1, 10)
    for _ in range(cantidad):
        lista.append(rn.randint(1, 10))
    return lista

def normalizar_lista(lista: list) -> list:
    total = sum(lista)
    if total == 0:
        raise ValueError("La suma de todos los elementos no puede ser 0.")
    return [x / total for x in lista]

def verificacion_lista():
    lista = cargar_lista()
    print("La lista original es:", lista)

    try:
        lista_normalizada = normalizar_lista(lista)
        print("La lista normalizada es:", lista_normalizada)
        print("La suma de los elementos de la lista normalizada es:", sum(lista_normalizada))
    except ValueError:
        print("No se puede normalizar una lista cuya suma total es 0.")

if __name__ == "__main__":
    verificacion_lista()

