"""
Desarrollar un programa que utilice una función que reciba como parámetro una
cadena de caracteres conteniendo una dirección de correo electrónico y devuelva
una tupla con las distintas partes que componen dicha dirección. Ejemplo:
alguien@uade.edu.ar -> (alguien, uade, edu, ar). La función debe detectar
formatos de fecha inválidos y devolver una tupla vacía.
"""
from typing import Tuple

def descomponer_correo(correo: str) -> Tuple[str, str, str, str]:
    if correo.count('@') != 1 or correo.count('.') < 1:
        return ()
    
    usuario, dominio_completo = correo.split('@')
    
    if '.' not in dominio_completo:
        return ()
    
    partes_dominio = dominio_completo.split('.')
    
    if len(partes_dominio) != 3:
        return ()
    
    return (usuario, partes_dominio[0], partes_dominio[1], partes_dominio[2])

def obtener_correo():
    correo = input("Ingrese una dirección de correo electrónico: ")
    
    resultado = descomponer_correo(correo)
    
    if resultado:
        print(f"Las partes del correo son: {resultado}")
    else:
        print("La dirección de correo electrónico es inválida.")

obtener_correo()

