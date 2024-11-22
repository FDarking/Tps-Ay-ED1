"""Desarrollar una función que reciba un número binario y lo devuelva convertido a
base decimal"""

def binario_a_decimal(binario, indice=0):
    if binario == 0:
        return 0
    else:
        ultimo_digito = binario % 10
        return ultimo_digito * (2 ** indice) + binario_a_decimal(binario // 10, indice + 1)

binario = int(input("Ingresa un número binario: "))
print(f"El número binario en decimal es: {binario_a_decimal(binario)}")
