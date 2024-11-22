"""
Escribir una función que reciba como parámetro una tupla conteniendo una fecha
(día,mes,año) y devuelva una cadena de caracteres con la misma fecha expresada
en formato extendido. La función debe contemplarse que el año se ingrese en dos
dígitos, los que serán interpretados según un año de corte definido dentro del
programa. Cualquier año mayor que éste se considerará del siglo pasado. Por
ejemplo, si el año de corte fuera 30, la función devuelve "12 de Octubre de 2030"
para (12,10,30). Pero si la tupla fuera (25, 12, 31) devolverá "25 de Diciembre de
1931". Si el año se ingresa en cuatro dígitos el año de corte no será tenido en
cuenta. Escribir también un programa para ingresar los datos, invocar a la función y
mostrar el resultado.
"""
from typing import Tuple

def fecha_extendida(fecha: Tuple[int, int, int]) -> str:
    
    anio_corte = 30
    
    dia, mes, anio = fecha
    
    if anio < 100:

        if anio > anio_corte:
            anio += 2000

        else:
            anio += 1900
    
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", 
             "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]
    
    mes_nombre = meses[mes - 1]
    
    return f"{dia} de {mes_nombre} de {anio}"

def obtener_fecha():
    # Pedir al usuario la fecha
    dia = int(input("Ingrese el día: "))
    mes = int(input("Ingrese el mes: "))
    anio = int(input("Ingrese el año (puede ser en dos o cuatro dígitos): "))
    
    fecha = (dia, mes, anio)
    resultado = fecha_extendida(fecha)
    print("Fecha en formato extendido:", resultado)

obtener_fecha()
