"""
Resolver el siguiente problema utilizando funciones:
Un productor frutihortícola desea contabilizar sus cajones de naranjas según el peso
para poder cargar los camiones de reparto. La empresa cuenta con N camiones, y
cada uno puede transportar hasta media tonelada (500 kilogramos). En un cajón
caben 100 naranjas con un peso de entre 200 y 300 gramos cada una. Si el peso
de alguna naranja se encuentra fuera del rango indicado se la clasifica para
procesar como jugo. Desarrollar un programa para ingresar la cantidad de naranjas
cosechadas e informar cuántos cajones se pueden llenar, cuántas naranjas son para
jugo y si hay algún sobrante de naranjas que deba considerarse para el siguiente
reparto. Simular el peso de cada unidad generando un número entero al azar entre
150 y 350.
Además, se desea saber cuántos camiones se necesitan para transportar la cosecha, considerando 
que la ocupación del camión no debe ser inferior al 80%; en caso contrario el camión no serán 
despachado por su alto costo.
"""
import random

def generar_peso_naranja():
    return random.randint(150, 350)

def clasificar_naranjas(cantidad_naranjas):
    cajones = 0
    jugo = 0
    naranjas_en_cajon = 0  # Contador de naranjas en el cajón

    for _ in range(cantidad_naranjas):
        peso = generar_peso_naranja()
        
        if 200 <= peso <= 300:
            naranjas_en_cajon += 1
            if naranjas_en_cajon == 100:
                cajones += 1
                naranjas_en_cajon = 0  
            jugo += 1

    sobrantes = naranjas_en_cajon
    return cajones, jugo, sobrantes

def calcular_camiones(cajones):
    peso_por_cajon = 100 * 250 
    total_peso = cajones * peso_por_cajon
    peso_por_camion = 500 

    camiones_necesarios = total_peso // peso_por_camion
    if total_peso % peso_por_camion > 0:
        camiones_necesarios += 1

    if total_peso / camiones_necesarios < 0.8 * peso_por_camion:
        return 0

    return camiones_necesarios

def main():
    cantidad_naranjas = int(input("Ingrese la cantidad de naranjas cosechadas: "))
    cajones, jugo, sobrantes = clasificar_naranjas(cantidad_naranjas)

    print(f"Cajones llenos: {cajones}")
    print(f"Naranjas para jugo: {jugo}")
    print(f"Sobrantes: {sobrantes}")

    camiones_necesarios = calcular_camiones(cajones)
    if camiones_necesarios > 0:
        print(f"Camiones necesarios para el transporte: {camiones_necesarios}")
    else:
        print("No se necesitan camiones para el transporte, no se cumple la ocupación mínima.")
        
if __name__ == "__main__":
    #BP
    main()
