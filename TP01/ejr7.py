"""7. Escribir una función diasiguiente(dia, mes año) que reciba como parámetro una
fecha cualquiera expresada por tres enteros y calcule y devuelva otros tres enteros
correspondientes el día siguiente al dado. Utilizando esta función sin modificaciones
ni agregados, desarrollar programas que permitan:
a. Sumar N días a una fecha.
b. Calcular la cantidad de días existentes entre dos fechas cualesquiera.
"""
def es_bisiesto(anio: int):
    # Verifica si el año es bisiesto
    return anio % 4 == 0 and (anio % 400 == 0 or anio % 100 != 0)

def fecha_valida(dia: int, mes: int, anio: int):
    # Verifica que la fecha sea válida
    dias_al_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if mes < 1 or mes > 12:
        return False
    if es_bisiesto(anio):
        dias_al_mes[1] = 29
    if dia < 1 or dia > dias_al_mes[mes - 1]:
        return False
    return True

def siguiente_dia(dia: int, mes: int, anio: int):
    # Devuelve la fecha del día siguiente
    dias_al_mes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if es_bisiesto(anio):
        dias_al_mes[1] = 29

    if dia == dias_al_mes[mes - 1]:
        dia = 1
        if mes == 12:
            mes = 1
            anio += 1
        else:
            mes += 1
    else:
        dia += 1
    return dia, mes, anio

def agregar_dias(dia: int, mes: int, anio: int, n: int):
    # Retorna otra fecha "n" días después
    for _ in range(n):
        dia, mes, anio = siguiente_dia(dia, mes, anio)
    return dia, mes, anio

def calcular_diferencia_fechas(dia1: int, mes1: int, anio1: int, dia2: int, mes2: int, anio2: int):
    # Cuenta cuántos días hay entre dos fechas
    dias = 0
    while (dia1, mes1, anio1) != (dia2, mes2, anio2):
        dia1, mes1, anio1 = siguiente_dia(dia1, mes1, anio1)
        dias += 1
    return dias

def mostrar_opciones():
    print("1: Día siguiente")
    print("2: Sumar días a una fecha")
    print("3: Días entre dos fechas")

def ejecutar_programa():
    while True:
        mostrar_opciones()
        opcion = input("Ingrese una opción (0 para salir): ")
        if opcion == "1":
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))
            if fecha_valida(dia, mes, anio):
                nuevo_dia, nuevo_mes, nuevo_anio = siguiente_dia(dia, mes, anio)
                print("El día siguiente es:", nuevo_dia, "/", nuevo_mes, "/", nuevo_anio)
            else:
                print("La fecha es inválida.")
        elif opcion == "2":
            dia = int(input("Ingrese el día: "))
            mes = int(input("Ingrese el mes: "))
            anio = int(input("Ingrese el año: "))
            suma = int(input("Ingrese la cantidad de días que desea sumar: "))
            if fecha_valida(dia, mes, anio):
                nuevo_dia, nuevo_mes, nuevo_anio = agregar_dias(dia, mes, anio, suma)
                print("La nueva fecha es:", nuevo_dia, "/", nuevo_mes, "/", nuevo_anio)
            else:
                print("La fecha es inválida.")
        elif opcion == "3":
            print("Datos de la primera fecha:")
            dia_a = int(input("Ingrese el día: "))
            mes_a = int(input("Ingrese el mes: "))
            anio_a = int(input("Ingrese el año: "))
            print("Datos de la segunda fecha:")
            dia_b = int(input("Ingrese el día: "))
            mes_b = int(input("Ingrese el mes: "))
            anio_b = int(input("Ingrese el año: "))
            diferencia = calcular_diferencia_fechas(dia_a, mes_a, anio_a, dia_b, mes_b, anio_b)
            print(f"La diferencia es de {diferencia} días.")
        elif opcion == "0":
            print("Saliendo...")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    ejecutar_programa()
