def num_mayorstr(a, b, c):
    if a > b:
        if a > c:
            return a
        elif a < c:
            return c
    elif b > a:
        if b > c:
            return b
        elif b < c:
            return c
    elif c > a:
        if c > b:
            return c
        elif c < b:
            return b
    return -1


def numeros():
    a = int(input("Ingrese el primer valor: "))
    b = int(input("Ingrese el segundo valor: "))
    c = int(input("Ingrese el tercer valor: "))
    mayor = num_mayorstr(a, b, c)
    if mayor != -1:
        print(f"El número mayor es {mayor}")
    else:
        print("No existe un número mayor estricto.")

numeros()