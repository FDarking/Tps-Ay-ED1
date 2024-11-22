def ordenar_palabras_por_longitud(cadena):
    palabras = cadena.split()
    
    for i in range(len(palabras)):
        for j in range(i + 1, len(palabras)):
            if len(palabras[i]) > len(palabras[j]):
                temp = palabras[i]
                palabras[i] = palabras[j]
                palabras[j] = temp
    
    resultado = ""
    for palabra in palabras:
        resultado = resultado + palabra + " "
    
    return resultado.strip()

cadena = "la universidad no me deja dormir"
resultado = ordenar_palabras_por_longitud(cadena)
print(resultado)
