"""
Escribir una función que reciba como parámetro un número entero entre 0 y 3999 y
lo convierta en un número romano, devolviéndolo en una cadena de caracteres. ¿En
qué cambiaría la función si el rango de valores fuese diferente?
"""
def convertir_a_romano(numero):
    
    if numero < 1 or numero > 3999:
        return "El número debe estar entre 1 y 3999"
    
    # Listas de valores y símbolos romanos
    valores = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
    simbolos = ["M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"]

    resultado = ""
    for i in range(len(valores)):

        while numero >= valores[i]:
            resultado += simbolos[i]
            numero -= valores[i] 

    return resultado


if __name__ == "__main__":

    numero = int(input("Ingrese un número entre 1 y 3999: "))
    
    numero_romano = convertir_a_romano(numero)
    print(f"El número en romano es: {numero_romano}")

