"""
Una institución deportiva necesita clasificar a sus atletas para inscribirlos en los
próximos Juegos Panamericanos. Para eso encargó la realización de un programa
que incluya las siguientes funciones:
GrabarRangoAlturas(): Graba en un archivo las alturas de los atletas de distintas
disciplinas, los que se ingresan desde el teclado. Cada dato se debe grabar en una
línea distinta. Ejemplo:
<Deporte 1>
<altura del atleta 1>
<altura del atleta 2>
< . . . >
<Deporte 2>
<altura del atleta 1>
<altura del atleta 2>

GrabarPromedio(): Graba en un archivo los promedios de las alturas de los atletas, leyendo los datos del archivo generado en el paso anterior. La disciplina y el
promedio deben grabarse en líneas diferentes. Ejemplo:
<Deporte 1>
<Promedio de alturas deporte 1>
<Deporte 2>
<Promedio de alturas deporte 2>
< . . . >

MostrarMasAltos() Muestra por pantalla las disciplinas deportivas cuyos atletas
superan la estatura promedio general. Obtener los datos del segundo archivo.
"""
def grabar_rango_alturas() -> None:
    """
    Precondición: Ninguna.
    Argumentos: Guarda en un archivo las alturas de los atletas separados por el deporte que juegan.
    Postcondición: Guarda las alturas en un archivo 'alturas_atletas.txt'.
    """
    try:
        with open('alturas_atletas.txt', 'w', encoding='utf-8') as archivo:
            while True:
                deporte = input("Ingrese el deporte (o 's' para terminar): ").strip()
                if deporte.lower() == 's':
                    break

                archivo.write(f"{deporte}\n")

                while True:
                    try:
                        altura = int(input(f"Ingrese la altura del atleta en {deporte} (o '-1' para cambiar de deporte): "))
                    except ValueError:
                        print("Debe ingresar un valor numérico válido para la altura.")
                    else:
                        if altura == -1:
                            break

                        if 50 <= altura <= 250:
                            archivo.write(f"{altura}\n")
                        else:
                            print("Dato inválido. La altura debe estar entre 50 y 250 cm.")

    except Exception as e:
        print(f"Hubo un error - {e}")
    else:
        print("Se completó el registro de alturas.")


def grabar_promedio() -> None:
    """
    Precondición: El archivo 'alturas_atletas.txt' debe existir.
    Argumentos: Calcula los promedios de las alturas de los atletas por deporte y los guarda en 'promedios_alturas.txt'.
    Postcondición: Guarda los promedios de las alturas en un archivo 'promedios_alturas.txt'.
    """
    try:
        with open('alturas_atletas.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        promedios = {}
        deporte = ""
        alturas = []

        with open('promedios_alturas.txt', 'w', encoding='utf-8') as archivo_promedios:
            for linea in lineas:
                linea = linea.strip()
                if linea.isalpha():  # Si la línea es un deporte
                    if deporte:  # Si ya tenemos datos de un deporte anterior, calculamos el promedio
                        promedio = sum(alturas) / len(alturas) if alturas else 0
                        archivo_promedios.write(f"{deporte}\n{promedio}\n")
                    deporte = linea
                    alturas = []
                else:  # Si la línea es una altura, la agregamos a la lista
                    try:
                        altura = float(linea)
                        alturas.append(altura)
                    except ValueError:
                        print(f"Error al leer la altura: {linea}")
            # Escribir el promedio del último deporte
            if deporte:
                promedio = sum(alturas) / len(alturas) if alturas else 0
                archivo_promedios.write(f"{deporte}\n{promedio}\n")

    except FileNotFoundError:
        print("El archivo 'alturas_atletas.txt' no se encontró. Asegúrese de haber ejecutado 'grabar_rango_alturas()' primero.")
    except Exception as e:
        print(f"Hubo un error - {e}")
    else:
        print("Se completó el cálculo y registro de promedios.")


def mostrar_mas_altos() -> None:
    """
    Precondición: El archivo 'promedios_alturas.txt' debe existir.
    Argumentos: Muestra los deportes cuyos atletas superan la altura promedio general.
    Postcondición: Muestra los deportes cuyos atletas superan la altura promedio general.
    """
    try:
        with open('promedios_alturas.txt', 'r', encoding='utf-8') as archivo:
            lineas = archivo.readlines()

        promedios = {}
        suma_promedios = 0
        cantidad_deportes = 0

        for i in range(0, len(lineas), 2):
            deporte = lineas[i].strip()
            promedio = float(lineas[i + 1].strip())
            promedios[deporte] = promedio
            suma_promedios += promedio
            cantidad_deportes += 1

        if cantidad_deportes > 0:
            promedio_general = suma_promedios / cantidad_deportes
            print(f"Estatura promedio general: {promedio_general:.2f}")

            print("\nDeportes cuyos atletas superan la estatura promedio general:")
            for deporte, promedio in promedios.items():
                if promedio > promedio_general:
                    print(f"{deporte}: {promedio:.2f}")
        else:
            print("No se encontraron deportes para comparar.")

    except FileNotFoundError:
        print("El archivo 'promedios_alturas.txt' no se encontró. Asegúrese de haber ejecutado 'grabar_promedio()' primero.")
    except Exception as e:
        print(f"Hubo un error - {e}")


def main() -> None:
    """
    Menú principal del programa.
    """
    while True:
        print("\n--- Menú ---")
        print("1. Grabar Rango de Alturas")
        print("2. Grabar Promedio de Alturas")
        print("3. Mostrar Deportes con Alturas Superiores al Promedio General")
        print("4. Salir")
        
        opcion = input("Elija una opción (1-4): ").strip()

        if opcion == '1':
            grabar_rango_alturas()
        elif opcion == '2':
            grabar_promedio()
        elif opcion == '3':
            mostrar_mas_altos()
        elif opcion == '4':
            print("Saliendo del programa...")
            break
        else:
            print("Opción no válida. Por favor, elija una opción entre 1 y 4.")


if __name__ == "__main__":
    main()

