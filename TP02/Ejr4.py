"""
Eliminar de una lista de números enteros aquellos valores que se encuentren en
una segunda lista. Imprimir la lista original, la lista de valores a eliminar y la lista
resultante. La función debe modificar la lista original sin crear una copia modificada.
"""
def eliminar_valores(lista_original, lista_eliminar):
    for valor in lista_eliminar:
        while valor in lista_original:
            lista_original.remove(valor)

def lista():

    lista_original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    print("Lista original:", lista_original)

    # Crear la lista de valores que queremos eliminar
    lista_eliminar = [2, 4, 6, 8]
    print("Lista de valores a eliminar:", lista_eliminar)

    # Llamar a la función para eliminar los valores
    eliminar_valores(lista_original, lista_eliminar)

    # Mostrar la lista resultante después de las eliminaciones
    print("Lista resultante:", lista_original)

if __name__ == "__main__":
    lista()
