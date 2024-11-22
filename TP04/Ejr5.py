"""
Escribir una función filtrar_palabras() que reciba una cadena de caracteres conteniendo 
una frase y un entero N, y devuelva otra cadena con las palabras que tengan N o más caracteres 
de la cadena original. 
Escribir también un programa para verificar el comportamiento de la misma. Hacer tres 
versiones de la función, para cada uno de los siguientes casos:
a. Utilizando sólo ciclos normales
b. Utilizando listas por comprensión
c. Utilizando la función filter
"""

def filtrar_palabras_ciclo(frase: str, n: int) -> str:
    palabras = frase.split()
    resultado = []
    for palabra in palabras:
        if len(palabra) >= n:
            resultado.append(palabra)
    return " ".join(resultado)


def filtrar_palabras_comprension(frase: str, n: int) -> str:  # Función B: listas por comprensión
    return " ".join([palabra for palabra in frase.split() if len(palabra) >= n])


def filtrar_palabras_filter(frase: str, n: int) -> str: 
    return " ".join(filter(lambda palabra: len(palabra) >= n, frase.split()))


def main() -> None:
    frases_filtrar = input("Ingrese la frase a filtrar: ")
    while True:  # Validar que el número ingresado sea positivo
        try:
            largo_string = int(input("Ingrese el largo mínimo de las palabras: "))
            if largo_string > 0:
                break
            else:
                print("El número debe ser positivo, intente nuevamente.")
        except ValueError:
            print("Ingresó un valor no válido. Intente nuevamente con un número entero positivo.")

    print(f"\nResultado utilizando ciclos normales:\n{filtrar_palabras_ciclo(frases_filtrar, largo_string)}")
    print(f"\nResultado utilizando listas por comprensión:\n{filtrar_palabras_comprension(frases_filtrar, largo_string)}")
    print(f"\nResultado utilizando la función filter:\n{filtrar_palabras_filter(frases_filtrar, largo_string)}")


if __name__ == "__main__":
    main()
