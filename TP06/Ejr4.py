def eliminar_comentarios(codigo):
    resultado = []
    i = 0
    dentro_comentario = False
    
    while i < len(codigo):

        if codigo[i] == "#" and not dentro_comentario:
            dentro_comentario = True
            while i < len(codigo) and codigo[i] != "\n":
                i += 1
            dentro_comentario = False
            continue
        
        resultado.append(codigo[i])
        i += 1
    
    return ''.join(resultado)

codigo_programa = """
"""

codigo_limpio = eliminar_comentarios(codigo_programa)
print(codigo_limpio)
