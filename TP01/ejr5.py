#Informa si el numero ingresado es oblongo , retorna True o False
oblongo = lambda x: any(a * (a  + 1) == x for a in range(1, x))
print(oblongo(int(input("Ingrese su numero: "))))


