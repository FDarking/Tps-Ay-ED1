"""
Escribir un programa que lea un archivo de texto conteniendo un conjunto de 
apellidos y nombres en formato "Apellido, Nombre" y guarde en el archivo
ARMENIA.TXT los registros de aquellas personas cuyo apellido termina con 
la cadena "IAN", en el archivo ITALIA.TXT los terminados en "INI" y en ESPAÑA.TXT los
terminados en "EZ". Descartar el resto. Ejemplo:
Arslanian, Gustavo –> ARMENIA.TXT
Rossini, Giuseppe –> ITALIA.TXT
Pérez, Juan –> ESPAÑA.TXT
Smith, John –> descartar
El archivo puede ser creado mediante el Block de Notas o el cualquier otro editor. 
"""
def origen_apellido(last_name: str, person: str, countries: dict) -> None:
    last_name = last_name.lower()
    for key, value in countries.items():
        if last_name.endswith(key):
            try:
                with open(value, 'a', encoding='utf-8') as archivo:
                    archivo.write(person.strip() + '\n')
                print(f"Se ha agregado '{person.strip()}' al archivo '{value}'.")
                return
            except Exception as e:
                print(f"Error al escribir en el archivo '{value}': {e}")
                return

def main() -> None:
    paises = {
        'ian': 'armenia.txt',
        'ini': 'italia.txt',
        'ez': 'españa.txt'
    }

    try:
        with open('personas.txt', 'r', encoding='utf-8') as archivo:
            for persona in archivo:
                persona = persona.strip()
                if not persona:
                    continue
                apellido = persona.split(',')[0].strip()
                origen_apellido(apellido, persona, paises)

    except FileNotFoundError:
        print("El archivo 'personas.txt' no se encontró.")
    except Exception as e:
        print(f"Hubo un error: {e}")

if __name__ == "__main__":
    main()