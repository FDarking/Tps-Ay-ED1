"""
La siguiente función permite averiguar el día de la semana para una fecha determinada. 
La fecha se suministra en forma de tres parámetros enteros y la función devuelve 0 para domingo,
1 para lunes, 2 para martes, etc. Escribir un programa para
imprimir por pantalla el calendario de un mes completo, correspondiente a un mes
y año cualquiera basándose en la función suministrada. Considerar que la semana
comienza en domingo.
"""
from tabulate import tabulate

def diadelasemana(dia, mes, año):
    if mes < 3:
        mes = mes + 10
        año = año - 1
    else:
        mes = mes - 2
    siglo = año // 100
    año2 = año % 100
    diasem = (
        ((26 * mes - 2) // 10) + dia + año2 + (año2 // 4) + (siglo // 4) - (2 * siglo)
    ) % 7
    if diasem < 0:
        diasem = diasem + 7
    return diasem

def dias_en_mes(mes: int, año: int) -> int:
    """Devuelve la cantidad de días que contiene el mes."""
    if mes == 2: 
        return 29 if (año % 4 == 0 and (año % 100 != 0 or año % 400 == 0)) else 28
    return 30 if mes in [4, 6, 9, 11] else 31

def imprimir_calendario(mes: int, año: int) -> None:
    """Imprime el calendario del mes y año especificados."""
    dias_semana = ["Dom", "Lun", "Mar", "Mie", "Jue", "Vie", "Sab"]
    
    primer_dia = diadelasemana(1, mes, año)
    dias_mes = dias_en_mes(mes, año) 

    calendario = []
    semana = [""] * primer_dia 

    for dia in range(1, dias_mes + 1):
        semana.append(dia)
        if len(semana) == 7: 
            calendario.append(semana)
            semana = []

    if semana: 
        calendario.append(semana + [""] * (7 - len(semana)))

    print(f"Calendario del {mes}/{año}")
    print(tabulate(calendario, headers=dias_semana, tablefmt="grid"))

def main():
    while True:
        salir = input("Para continuar ingrese cualquier tecla, 0 para salir: ")
        if salir == "0":
            print("Saliendo..")
            break
        mes_ = int(input("Ingrese el mes (1-12): "))
        año_ = int(input("Ingrese el año: "))
        if 1 <= mes_ <= 12:
            imprimir_calendario(mes_, año_)
        else:
            print("Mes no válido. Intente de nuevo.")
#BP
if __name__ == "__main__":
    main()
