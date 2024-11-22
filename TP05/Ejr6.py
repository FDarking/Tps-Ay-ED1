"""
El método index permite buscar un elemento dentro de una lista, devolviendo la
posición que éste ocupa. Sin embargo, si el elemento no pertenece a la lista se
produce una excepción de tipo ValueError. Desarrollar un programa que cargue
una lista con números enteros ingresados a través del teclado (terminando con -1)
y permita que el usuario ingrese el valor de algunos elementos para visualizar la
posición que ocupan, utilizando el método index. Si el número no pertenece a la
lista se imprimirá un mensaje de error y se solicitará otro para buscar. Abortar el
proceso al tercer error detectado. No utilizar el operador in durante la búsqueda
"""
def buscar_numero():
    lista = []
    intentos_fallidos = 0

    while True:
        try:
            numero = int(input("Ingrese un numero entero (o -1 para terminar): "))
            if numero == -1:
                break
            lista.append(numero)
        except ValueError:
            print("Error: Debe ingresar un numero entero valido.")

    while intentos_fallidos < 3:
        try:
            numero_buscar = int(input("Ingrese un numero para buscar su posicion: "))
            posicion = lista.index(numero_buscar)
            print(f"El numero {numero_buscar} esta en la posicion {posicion}.")
            break
        except ValueError:
            print("Error: El numero no se encuentra en la lista.")
            intentos_fallidos += 1
            if intentos_fallidos < 3:
                print(f"Intentos fallidos: {intentos_fallidos}. Quedan {3 - intentos_fallidos} intentos")
            else:
                print("Se alcanzaron 3 intentos fallidos. El programa se detendra")

buscar_numero()
