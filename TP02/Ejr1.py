"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que 
permita verificar su funcionamiento imprimiendo la lista luego de invocar a cada función:

a. Cargar una lista con números al azar de cuatro dígitos. 
La cantidad de elementos también será un número al azar de dos dígitos.
b. Calcular y devolver el producto de todos los elementos de la lista anterior.
c. Eliminar todas las apariciones de un valor en la lista anterior. El valor a eliminar
se ingresa desde el teclado y la función lo recibe como parámetro. No utilizar
listas auxiliares.
d. Determinar si el contenido de una lista cualquiera es capicúa, sin usar listas
auxiliares. Un ejemplo de lista capicúa es [50, 17, 91, 17, 50]
"""

import random

def cargar_lista():
    cantidad = random.randint(10, 99)
    return [random.randint(1000, 9999) for _ in range(cantidad)]

def producto_lista(lista):
    producto = 1
    for num in lista:
        producto *= num
    return producto

def eliminar_valor(lista, valor):
    for i in range(len(lista) - 1, -1, -1):
        if lista[i] == valor:
            del lista[i]

def es_capicua(lista):
    return lista == lista[::-1]

def lista():
    lista_numeros = cargar_lista()
    print("Lista cargada:", lista_numeros)

    producto = producto_lista(lista_numeros)
    print("Producto de los elementos:", producto)

    valor_a_eliminar = int(input("Ingrese un valor a eliminar de la lista: "))
    eliminar_valor(lista_numeros, valor_a_eliminar)
    print("Lista después de eliminar el valor:", lista_numeros)

    if es_capicua(lista_numeros):
        print("La lista es capicúa.")
    else:
        print("La lista no es capicúa.")

if __name__ == "__main__":
#BP
    lista()
