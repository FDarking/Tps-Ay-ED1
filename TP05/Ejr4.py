"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo 
una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres 
de la cadena original. 
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres 
versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""
def imprimir_numeros():
    try:
        for i in range(1, 100001):
            print(i)
    except KeyboardInterrupt:
        respuesta = input("\n¿Estas seguro de que deseas detener el programa? (s/n): ")
        if respuesta.lower() == 's':
            print("Programa detenido.")
        else:
            print("Continuando...")

imprimir_numeros()

