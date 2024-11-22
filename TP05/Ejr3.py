"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
"""
def obtener_mes(numero_mes):
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    try:
        return meses[numero_mes - 1]
    except IndexError:
        return ""

numero_mes = int(input("Ingrese un numero de mes (1-12): "))
mes = obtener_mes(numero_mes)
if mes:
    print("El mes es:", mes)
else:
    print("Numero de mes invalido.")
