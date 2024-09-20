"""
1. Desarrollar cada una de las siguientes funciones y escribir un programa que permita verificar
su funcionamiento, imprimiendo la matriz luego de invocar a cada función:

a. Cargar números enteros en una matriz de N x N, ingresando los datos desde
teclado.
b. Ordenar en forma ascendente cada una de las filas de la matriz.
c. Intercambiar dos filas, cuyos números se reciben como parámetro.
d. Intercambiar dos columnas dadas, cuyos números se reciben como parámetro.
e. Trasponer la matriz sobre si misma. (intercambiar cada elemento Aij por Aji)
f. Calcular el promedio de los elementos de una fila, cuyo número se recibe como
parámetro.
g. Calcular el porcentaje de elementos con valor impar en una columna, cuyo número se recibe como parámetro.
h. Determinar si la matriz es simétrica con respecto a su diagonal principal.
i. Determinar si la matriz es simétrica con respecto a su diagonal secundaria.
j. Determinar qué columnas de la matriz son palíndromos (capicúas), devolviendo
una lista con los números de las mismas.

NOTA: El valor de N debe leerse por teclado. Las funciones deben servir cualquiera
sea el valor ingresado.
"""
def cargar_matriz() -> list[list[int]]:
    n = int(input("Ingrese el tamaño de la matriz (La lista interna comparte el mismo tamaño): "))
    matriz = [
        [int(input(f"Fila {i + 1}, ingrese el elemento {j + 1}: ")) for j in range(n)]
        for i in range(n)
    ]
    return matriz


def ordenar_filas(matriz: list[list[int]]) -> None:
    for fila in matriz:
        fila.sort()


def intercambiar_filas(matriz: list[list[int]], fila1: int, fila2: int) -> None:
    fila1 -= 1
    fila2 -= 1
    if not (0 <= fila1 < len(matriz) and 0 <= fila2 < len(matriz)):
        print("Error: Uno o ambos números de fila son inválidos.")
    else:
        matriz[fila1], matriz[fila2] = matriz[fila2], matriz[fila1]


def intercambiar_columnas(matriz: list[list[int]], col1: int, col2: int) -> None:
    col1 -= 1
    col2 -= 1
    if not (0 <= col1 < len(matriz[0]) and 0 <= col2 < len(matriz[0])):
        print("Error: Uno o ambos números de columna son inválidos.")
    else:
        for fila in matriz:
            fila[col1], fila[col2] = fila[col2], fila[col1]


def transponer_matriz(matriz: list[list[int]]) -> list[list[int]]:
    largo = len(matriz)
    return [[matriz[j][i] for j in range(largo)] for i in range(largo)]


def promedio_fila(matriz: list[list[int]], numero_fila: int) -> float:
    numero_fila -= 1
    if numero_fila < 0 or numero_fila >= len(matriz):
        raise IndexError("El número de fila está fuera del rango.")
    return sum(matriz[numero_fila]) / len(matriz[numero_fila])


def porcentaje_impares_columna(matriz: list[list[int]], columna: int) -> float:
    columna -= 1
    if columna < 0 or columna >= len(matriz[0]):
        raise IndexError("El número de columna está fuera de rango.")
    impares = sum(1 for i in range(len(matriz)) if matriz[i][columna] % 2 != 0)
    return (impares / len(matriz)) * 100


def es_simetrica_principal(matriz: list[list[int]]) -> bool:
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[j][i]:
                return False
    return True


def es_simetrica_secundaria(matriz: list[list[int]]) -> bool:
    n = len(matriz)
    for i in range(n):
        for j in range(n):
            if matriz[i][j] != matriz[n - j - 1][n - i - 1]:
                return False
    return True


def columnas_capicuas(matriz: list[list[int]]) -> list[int]:
    capicuas = []
    n = len(matriz)
    for j in range(n):
        columna = [matriz[i][j] for i in range(n)]
        if columna == columna[::-1]:
            capicuas.append(j + 1)  # Devolver índice 1-based
    return capicuas


def menu():
    opciones = [
        "Cargar una matriz de NxN",
        "Ordenar listas de manera ascendente",
        "Intercambiar filas de la matriz",
        "Intercambiar columnas de la matriz",
        "Trasponer matriz",
        "Calcular promedio de una fila",
        "Calcular porcentaje de elementos impares en una columna",
        "Determinar si la matriz es simétrica respecto a su diagonal principal",
        "Determinar si la matriz es simétrica respecto a su diagonal secundaria",
        "Determinar qué columnas de la matriz son capicúas",
        "Salir",
    ]
    matrix = []

    while True:
        print("Menú de opciones:")
        for num, opcion in enumerate(opciones):
            print(f"{num + 1}. {opcion}.")
        op = input("Ingrese una opción: ")
        if op == "1":
            try:
                matrix = cargar_matriz()
                imprimir_matriz(matrix)
            except ValueError:
                print("El valor ingresado no es válido.")
        elif op == "2":
            if matrix:
                ordenar_filas(matrix)
                print("Matriz con filas ordenadas de forma ascendente:")
                imprimir_matriz(matrix)
            else:
                print("La matriz está vacía.")
        elif op == "3":
            if matrix:
                fila1 = int(input("Ingrese el número de la primera fila: "))
                fila2 = int(input("Ingrese el número de la segunda fila: "))
                intercambiar_filas(matrix, fila1, fila2)
                imprimir_matriz(matrix)
            else:
                print("La matriz está vacía.")
        elif op == "4":
            if matrix:
                col1 = int(input("Ingrese el número de la primera columna: "))
                col2 = int(input("Ingrese el número de la segunda columna: "))
                intercambiar_columnas(matrix, col1, col2)
                imprimir_matriz(matrix)
            else:
                print("La matriz está vacía.")
        elif op == "5":
            if matrix:
                matrix = transponer_matriz(matrix)
                print("Matriz traspuesta:")
                imprimir_matriz(matrix)
            else:
                print("La matriz está vacía.")
        elif op == "6":
            if matrix:
                fila = int(input("Ingrese el número de la fila para calcular su promedio: "))
                promedio = promedio_fila(matrix, fila)
                print(f"El promedio de la fila {fila} es: {promedio}")
            else:
                print("La matriz está vacía.")
        elif op == "7":
            if matrix:
                columna = int(input("Ingrese el número de la columna: "))
                porcentaje = porcentaje_impares_columna(matrix, columna)
                print(f"El porcentaje de elementos impares en la columna {columna} es: {porcentaje}%")
            else:
                print("La matriz está vacía.")
        elif op == "8":
            if matrix:
                simetrica_principal = es_simetrica_principal(matrix)
                print(f"La matriz es simétrica respecto a su diagonal principal: {simetrica_principal}")
            else:
                print("La matriz está vacía.")
        elif op == "9":
            if matrix:
                simetrica_secundaria = es_simetrica_secundaria(matrix)
                print(f"La matriz es simétrica respecto a su diagonal secundaria: {simetrica_secundaria}")
            else:
                print("La matriz está vacía.")
        elif op == "10":
            if matrix:
                capicuas = columnas_capicuas(matrix)
                print(f"Columnas capicúas: {capicuas}")
            else:
                print("La matriz está vacía.")
        elif op == "11":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")


def imprimir_matriz(matriz: list[list[int]]) -> None:
    for fila in matriz:
        print(fila)


if __name__ == "__main__":
    menu()
