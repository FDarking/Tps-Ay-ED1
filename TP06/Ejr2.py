"""
Escribir un programa que permita dividir un archivo de texto cualquiera en partes
que se puedan enviar por correo electrónico. El tamaño máximo de las partes se
ingresa por teclado. Los nombres de los archivos generados deben respetar el
nombre original con el agregado de un sufijo que indique de qué parte se trata.
Mostrar un mensaje de error si el proceso no
pudiera llevarse a cabo. Recordar que no se permite cargar el archivo completo en
memoria.
"""
def dividir_archivo_texto(nombre_archivo: str, tamanio_parte: int) -> None:
    nombre_base, extension = nombre_archivo.rsplit('.', 1) 
    try:
        with open(nombre_archivo, 'rt', encoding='utf-8') as archivo:
            prefijo = 1

            while True:
                contenido = archivo.read(tamanio_parte)
                if not contenido:
                    break

                nombre_parte = f"{nombre_base}_parte{prefijo}.{extension}"
                with open(nombre_parte, 'wt', encoding='utf-8') as archivo_parte:
                    archivo_parte.write(contenido)
                prefijo += 1

    except FileNotFoundError:
        print(f"Error: No se encontro el archivo '{nombre_archivo}'.")

    except Exception as e:
        print(f"Ocurrio un error al procesar el archivo: {e}")

    else:
        print(f"El archivo se ha dividido exitosamente en {prefijo - 1} partes.")


def main() -> None:
    try:
        nombre_archivo = input("Introduce el nombre del archivo para dividir: ")
        tamano_parte = int(input("Especifica el tamaño maximo de cada parte en caracteres: "))
        dividir_archivo_texto(nombre_archivo, tamano_parte)
    except ValueError:
        print("Error - El tamaño máximo debe ser un número entero válido.")
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")

if __name__ == "__main__":
    main()
