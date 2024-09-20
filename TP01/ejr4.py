"""Un comercio de electrodomésticos necesita para su línea de cajas un programa que
le indique al cajero el cambio que debe entregarle al cliente. Para eso se ingresan
dos números enteros, correspondientes al total de la compra y al dinero recibido.
Informar cuántos billetes de cada denominación deben ser entregados como vuelto,
de tal forma que se minimice la cantidad de billetes. Considerar que existen billetes
de $5000, $1000, $500, $200, $100, $50 y $10. Emitir un mensaje de error si el
dinero recibido fuera insuficiente o si el cambio no pudiera entregarse debido a falta
de billetes con denominaciones adecuadas. Ejemplo: Si la compra es de $3170 y se
abona con $5000, el vuelto debe contener 1 billete de $1000, 1 billete de $500, 1
billete de $200, 1 billete de $100 y 3 billetes de $10."""

def cajero_vuelto(monto_venta, monto_pagado):
    if monto_pagado < monto_venta:
        print("El dinero recibido es insuficiente.")
        return
    
    vuelto = monto_pagado - monto_venta
    if vuelto == 0:
        print("Pago con el dinero justo, no debe dar vuelto.")
        return
    
    denominaciones = [
        [5000, 1000, 500, 200, 100, 50, 10], 
        [0, 0, 0, 0, 0, 0, 0], 
    ]
    
    print("El vuelto que se debe dar es de", vuelto, ".")
    
    for i in range(len(denominaciones[0])):
        while vuelto >= denominaciones[0][i]:
            denominaciones[1][i] += 1
            vuelto -= denominaciones[0][i]

    for i in range(len(denominaciones[0])):
        if denominaciones[1][i] > 0:
            print(denominaciones[1][i], "billete/s de $", denominaciones[0][i], ".")

    if vuelto > 0:
        print("El vuelto no puede entregarse por falta de billetes con denominación adecuada.")

# Bloque principal
monto_venta = int(input("Ingrese el monto de la venta: "))
monto_pagado = int(input("Ingrese el monto que pagó el cliente: "))
calcular_vuelto(monto_venta, monto_pagado)
