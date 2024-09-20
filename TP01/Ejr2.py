"""Desarrollar una función que reciba tres números enteros positivos correspondientes
al día, mes, año de una fecha y verifique si corresponden a una fecha válida. Debe
tenerse en cuenta la cantidad de días de cada mes, incluyendo los años bisiestos.
Devolver True o False según la fecha sea correcta o no. Realizar también un
programa para verificar el comportamiento de la función"""

def es_bisiesto(anio):
    return anio % 4 == 0 and (anio % 100 != 0 or anio % 400 == 0)

def validacion_fecha(dia, mes, anio):
    # Validacion del año
    if anio < 0:
        print("Introduzca un año que sea después de Cristo")
        return False

    # Validacion de mes
    if mes < 1 or mes > 12:
        print("El mes es invalido")
        return False

    # Determina el numero de dias del mes
    if mes in [1, 3, 5, 7, 8, 10, 12]:  # Meses con 31 dias
        max_dias = 31
    elif mes in [4, 6, 9, 11]:  # Meses con 30 dias
        max_dias = 30
    elif mes == 2:  # Febrero
        if es_bisiesto(anio):
            max_dias = 29  
        else:
            max_dias = 28  

    # Validacion del dia para el mes dado
    if dia < 1 or dia > max_dias:
        print("El día es inválido")
        return False

    return True

# Bloque principal
dia = int(input("Introduzca un día: "))
mes = int(input("Introduzca un mes: "))
anio = int(input("Introduzca un año: "))

if validacion_fecha(dia, mes, anio) == True:
    print("La fecha introducida es válida")
else:
    print("La fecha introducida es inválida")