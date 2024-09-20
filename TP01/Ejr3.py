"""Una persona desea llevar el control de los gastos realizados al viajar en el subterráneo dentro 
de un mes. Sabiendo que dicho medio de transporte utiliza un esquema de tarifas decrecientes 
(detalladas en la tabla de abajo)  se solicita desarrollar una función que reciba como parámetro 
la cantidad de viajes realizados en un determinado mes y devuelva el total gastado en viajes. 
Realizar también un programa para verificar  el comportamiento de la función. 
Cantidad de viajes          Valor del pasaje
1 a 20                      Averiguar en Internet el valor actualizado  ($650-.)
21 a 30                     20% de descuento sobre tarifa máxima
31 a 40                     30% de descuento sobre tarifa máxima
Más de 40                   40% de descuento sobre tarifa máxima
"""
def calcular_gastos(cantidad_viajes):
    total = 0
    precio = 650  # Precio del viaje

    # Aplicar descuentos según la cantidad de viajes
    for viaje in range(1, cantidad_viajes + 1):
        if viaje <= 20:
            total += precio
        elif viaje <= 30:
            total += precio * 0.8
        elif viaje <= 40:
            total += precio * 0.7
        else:
            total += precio * 0.6
            
    return total


def verificar_funcion():
    # Prueba de la función con diferentes cantidades de viajes.
    viajes_de_prueba = [2, 10, 20, 25, 30, 35, 40, 45, 50]
    
    print("Resultados de los viajes de prueba:")
    for viajes in viajes_de_prueba:
        gasto = calcular_gastos(viajes)
        print(f"Por {viajes} viajes, gastó ${gasto:.2f}.")


def solicitar_viajes():
    # Solicitar al usuario la cantidad de viajes y calcular el gasto
    while True:
        viajes = int(input("Ingrese la cantidad de viajes que realizó (0 para salir): "))
        if viajes == 0:
            break
        total = calcular_gastos(viajes)
        print(f"Usted gastó ${total:.2f}.")


#Bloque principal
verificar_funcion()
solicitar_viajes()