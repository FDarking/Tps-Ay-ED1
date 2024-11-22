"""
Definir un conjunto con números enteros entre 0 y 9. Luego solicitar valores al
usuario y eliminarlos del conjunto mediante el método remove, mostrando el contenido 
del conjunto luego de cada eliminación. Finalizar el proceso al ingresar -1.
Utilizar manejo de excepciones para evitar errores al intentar quitar elementos
inexistentes.
"""
def eliminar_elementos():
    conjunto = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
    
    while True:
        print(f"Conjunto actual: {conjunto}")
        try:
            numero = int(input("Ingrese un número para eliminar (o -1 para finalizar): "))
            
            if numero == -1:
                print("Proceso finalizado.")
                break
            
            conjunto.remove(numero)
            print(f"Se eliminó el número {numero}.")
        except KeyError:
            print("Error: El número no está en el conjunto.")
        except ValueError:
            print("Error: Por favor ingrese un número entero.")
        
eliminar_elementos()
