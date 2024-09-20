import csv

def crear_csv():
    data = [
        ["Equipo", "Integrante", "DNI"],
        ["Equipo A", "Juan Pérez", "12.345.678"],
        ["Equipo A", "Ana Gómez", "23.456.789"],
        ["Equipo A", "Luis Martínez", "34.567.890"],
        ["Equipo A", "Carmen Díaz", "45.678.901"],
        ["Equipo A", "Ricardo Torres", "56.789.012"],
        ["Equipo B", "Marta López", "67.890.123"],
        ["Equipo B", "Diego Fernández", "78.901.234"],
        ["Equipo B", "Sofía Ramírez", "89.012.345"],
        ["Equipo B", "Pablo Herrera", "90.123.456"],
        ["Equipo B", "Laura Sánchez", "01.234.567"],
        ["Equipo C", "Andrés Morales", "12.345.098"],
        ["Equipo C", "Julia Castro", "23.456.109"],
        ["Equipo C", "César Ruiz", "34.567.210"],
        ["Equipo C", "Isabel Jiménez", "45.678.321"],
        ["Equipo C", "Marco Salazar", "56.789.432"],
        ["Equipo D", "Lucía Ortega", "67.890.543"],
        ["Equipo D", "Andrés Vega", "78.901.654"],
        ["Equipo D", "Patricia Ríos", "89.012.765"],
        ["Equipo D", "Samuel Morales", "90.123.876"],
        ["Equipo D", "Natalia Aguirre", "01.234.987"],
        ["Equipo E", "Julio Méndez", "12.345.679"],
        ["Equipo E", "Clara Torres", "23.456.780"],
        ["Equipo E", "Rafael Silva", "34.567.891"],
        ["Equipo E", "Silvia Ramos", "45.678.902"],
        ["Equipo E", "Tomás Medina", "56.789.013"],
        ["Equipo F", "Verónica Rena", "67.890.124"],
        ["Equipo F", "Roberto Romero", "78.901.235"],
        ["Equipo F", "Daniela Rojas", "89.012.346"],
        ["Equipo F", "Esteban Peña", "90.123.457"],
        ["Equipo F", "Alicia Cordero", "01.234.568"],
        ["Equipo G", "Marco Delgado", "12.345.097"],
        ["Equipo G", "Mónica Villa", "23.456.108"],
        ["Equipo G", "Arturo Vidal", "34.567.219"],
        ["Equipo G", "Teresa Soto", "45.678.320"],
        ["Equipo G", "José Acosta", "56.789.431"],
        ["Equipo H", "Carla Aguayo", "67.890.542"],
        ["Equipo H", "Emilio Salas", "78.901.653"],
        ["Equipo H", "Susana Fuentes", "89.012.764"],
        ["Equipo H", "Nicolás Guerra", "90.123.875"],
        ["Equipo H", "Fabiola Barrio", "01.234.986"],
    ]

    with open('Datos.csv', mode='w', newline='', encoding='UTF-8') as archivo:
        escritor = csv.writer(archivo)
        escritor.writerows(data)

if __name__ == "__main__":
    crear_csv()