"""
Crear una función contarvocales(), que reciba una palabra y cuente cuántas vocales
contiene, identificando la cantidad de cada una. Devolver un diccionario con los
resultados. Luego desarrollar un programa para leer una frase e invocar a la
función por cada palabra que contenga la misma. Imprimir las palabras y la
cantidad de vocales hallada.
"""
from typing import Dict

def contarvocales(palabra: str) -> Dict[str, int]:
    vocales = 'aeiou'
    conteo = {v: 0 for v in vocales}
    
    for letra in palabra.lower():
        if letra in vocales:
            conteo[letra] += 1
            
    return conteo

def procesar_frase(frase: str) -> None:
    palabras = frase.split()
    
    for palabra in palabras:
        conteo_vocales = contarvocales(palabra)
        print(f"Palabra: {palabra} -> {conteo_vocales}")

def main() -> None:
    frase = input("Ingrese una frase: ")
    procesar_frase(frase)

if __name__ == "__main__":
    main()
