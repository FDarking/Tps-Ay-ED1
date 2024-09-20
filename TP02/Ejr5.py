"""
Escribir una función que reciba una lista como parámetro y devuelva True si la lista
está ordenada en forma ascendente o False en caso contrario. Por ejemplo,
ordenada([1, 2, 3]) retorna True y ordenada(['b', 'a']) retorna False. Desarrollar
además un programa para verificar el comportamiento de la función. 
"""
def ordenada(lista):
    for i in range(len(lista) - 1):
        if lista[i] > lista[i + 1]:
            return False
    return True

def lista_ordenada():
    lista1 = [1, 2, 3]
    lista2 = [3, 2, 1]
    lista3 = ['b', 'a']
    lista4 = ['a', 'b', 'c']
    lista5 = [1, 2, 2, 3]
    lista6 = [10, 20, 30, 40, 50]
    
    print("Probando listas para ver si están ordenadas:")
    
    print("Lista 1:", lista1)
    print("¿Está ordenada?", ordenada(lista1))
    
    print("Lista 2:", lista2)
    print("¿Está ordenada?", ordenada(lista2))
    
    print("Lista 3:", lista3)
    print("¿Está ordenada?", ordenada(lista3))
    
    print("Lista 4:", lista4)
    print("¿Está ordenada?", ordenada(lista4))
    
    print("Lista 5:", lista5)
    print("¿Está ordenada?", ordenada(lista5))
    
    print("Lista 6:", lista6)
    print("¿Está ordenada?", ordenada(lista6))

if __name__ == "__main__":
    lista_ordenada()
