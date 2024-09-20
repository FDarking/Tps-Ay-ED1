"""
Escribir funciones para:
a. Generar una lista de N números aleatorios del 1 al 100. El valor de N se ingresa
a través del teclado.
b. Recibir una lista como parámetro y devolver True si la misma contiene algún
elemento repetido. La función no debe modificar la lista.
c. Recibir una lista como parámetro y devolver una nueva lista con los elementos
únicos de la lista original, sin importar el orden.
Combinar estas tres funciones en un mismo programa.
"""


import random

def generar_lista(n):
    return [random.randint(1, 100) for _ in range(n)]

def tiene_elementos_repetidos(lista):
    return len(lista) != len(set(lista))

def elementos_unicos(lista):
    return list(set(lista))

def lista():
    n = int(input("Ingrese la cantidad de números aleatorios a generar: "))
    lista_numeros = generar_lista(n)
    print("Lista generada:", lista_numeros)

    if tiene_elementos_repetidos(lista_numeros):
        print("La lista contiene elementos repetidos.")
    else:
        print("La lista no contiene elementos repetidos.")

    lista_unicos = elementos_unicos(lista_numeros)
    print("Lista con elementos únicos:", lista_unicos)

if __name__ == "__main__":
    #BP
    lista()
