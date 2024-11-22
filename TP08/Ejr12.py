"""
Una librería almacena su lista de precios en un diccionario. Diseñar un programa
para crearlo, incrementar los precios de los cuadernos en un 15%, imprimir un
listado con todos los elementos de la lista de precios e indicar cuál es el ítem más
costoso que venden en el comercio
"""
from typing import Dict

def incrementar_precios(diccionario: Dict[str, int], porcentaje: int) -> Dict[str, int]:
    for producto in diccionario:
        if "cuaderno" in producto.lower():
            diccionario[producto] += diccionario[producto] * porcentaje // 100
    return diccionario

def item_mas_costoso(diccionario: Dict[str, int]) -> str:
    item = max(diccionario, key=diccionario.get)
    return item

def main():
    precios = {
        "Cuaderno hojas rayadas": 100,
        "Cuaderno hojas cuadriculadas": 50,
        "Lapiz": 10,
        "Goma": 5,
        "Lapicera": 30,
    }

    print("Lista de precios original:")
    for item, precio in precios.items():
        print(f"{item}: ${precio}")

    precios = incrementar_precios(precios, 15)
    
    print("\nLista de precios después de incrementar los cuadernos en un 15%:")
    for item, precio in precios.items():
        print(f"{item}: ${precio}")

    costoso = item_mas_costoso(precios)
    print(f"\nEl ítem más costoso es: {costoso} con un precio de ${precios[costoso]}")

if __name__ == "__main__":
    main()
