"""
Escribir funciones lambda para:
a.Informar si un número es oblongo. Se dice que un número es oblongo cuando se puede obtener 
multiplicando dos números naturales consecutivos. Por ejemplo 6 es oblongo porque resulta de 
multiplicar 2 * 3.
"""
oblongo = lambda x: any(a * (a  + 1) == x for a in range(1, x))
print(oblongo(int(input("Ingrese su numero: "))))


"""
Informar si un número es triangular. Un número se define como triangular si puede
expresarse como la suma de un grupo de números naturales consecutivos comenzando desde 1.
Por ejemplo 10 es un número triangular porque se obtiene sumando 1+2+3+4.
"""

numtriangular = lambda x: (n := int(((-1 + (1 + 8 * x) ** 0.5) / 2))) * (n + 1) // 2 == x

print(numtriangular(int(input("Ingrese su numero: "))))
