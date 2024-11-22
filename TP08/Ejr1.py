"""
Desarrollar las siguientes funciones utilizando tuplas para representar fechas y horarios, y luego escribir un programa que las vincule:
a. Ingresar una fecha desde el teclado, verificando que corresponda a una fecha
válida.
b. Sumar N días a una fecha.
c. Ingresar un horario desde teclado, verificando que sea correcto.
d. Calcular la diferencia entre dos horarios. Si el primer horario fuera mayor al
segundo se considerará que el primero corresponde al día anterior. En ningún
caso la diferencia en horas puede superar las 24 horas.
"""
def ingresar_fecha():
    while True:
        try:
            fecha_str = input("Ingresa una fecha (DD/MM/AAAA): ")
            dia, mes, anio = map(int, fecha_str.split('/'))
            if (1 <= mes <= 12) and (1 <= dia <= dias_en_mes(mes, anio)):
                return (dia, mes, anio)
            else:
                raise ValueError
        except ValueError:
            print("Fecha inválida, intenta nuevamente.")

def dias_en_mes(mes, anio):

    meses_31 = {1, 3, 5, 7, 8, 10, 12}

    meses_30 = {4, 6, 9, 11}
    if mes in meses_31:
        return 31
    elif mes in meses_30:
        return 30
    elif mes == 2:  # Febrero

        if (anio % 4 == 0 and anio % 100 != 0) or (anio % 400 == 0):
            return 29
        else:
            return 28
    return 30

def sumar_dias(fecha, n_dias):
    dia, mes, anio = fecha
    while n_dias > 0:
        dias_restantes = dias_en_mes(mes, anio) - dia + 1
        if n_dias < dias_restantes:
            dia += n_dias
            break
        else:
            n_dias -= dias_restantes
            dia = 1
            mes += 1
            if mes > 12:
                mes = 1
                anio += 1
    return (dia, mes, anio)

def ingresar_horario():
    while True:
        try:
            horario_str = input("Ingresa un horario (HH:MM): ")
            hora, minuto = map(int, horario_str.split(':'))
            if 0 <= hora < 24 and 0 <= minuto < 60:
                return (hora, minuto)
            else:
                raise ValueError
        except ValueError:
            print("Horario inválido, intenta nuevamente.")

def calcular_diferencia_horarios(horario1, horario2):
    hora1, minuto1 = horario1
    hora2, minuto2 = horario2

    minutos_hora1 = hora1 * 60 + minuto1
    minutos_hora2 = hora2 * 60 + minuto2
    
    if minutos_hora1 < minutos_hora2:
        diferencia_minutos = 1440 + minutos_hora1 - minutos_hora2  # 1440 minutos en un día
    else:
        diferencia_minutos = minutos_hora1 - minutos_hora2
    
    horas = diferencia_minutos // 60
    minutos = diferencia_minutos % 60
    return horas, minutos

def main():
    print("Bienvenido al programa de manejo de fechas y horarios.")
    
    fecha = ingresar_fecha()
    print(f"Fecha ingresada: {fecha[0]}/{fecha[1]}/{fecha[2]}")
    
    n_dias = int(input("Ingresa la cantidad de días a sumar: "))
    nueva_fecha = sumar_dias(fecha, n_dias)
    print(f"Nueva fecha después de sumar {n_dias} días: {nueva_fecha[0]}/{nueva_fecha[1]}/{nueva_fecha[2]}")
    
    print("Ingrese el primer horario:")
    horario1 = ingresar_horario()
    print("Ingrese el segundo horario:")
    horario2 = ingresar_horario()
    
    horas, minutos = calcular_diferencia_horarios(horario1, horario2)
    print(f"La diferencia entre los dos horarios es: {horas} horas y {minutos} minutos.")

if __name__ == "__main__":
    main()

