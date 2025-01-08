from colorama import init, Fore, Style

def get_field_set(collection):
    """
    - Descripción: Obteniendo los distintos campos de la colección
    - Parámetros:
        - collection: conexion a la colección en MongoDB
    - Retorno:
        - field_names. Conjunto con los nombres de los campos de la colección
    """
    # Para posteriormente filtrar, ver linea 111 de fichero principal
    field_names = set()

    first_record = collection.find_one({}, {"_id": 0})
    if first_record:
        field_names.update(first_record.keys())

    return sorted(field_names)


def printing(data: list):
    print(Fore.YELLOW + "Imprimiendo datos seleccionados...\n" + Style.RESET_ALL)
    for reg in data:
        print(reg)
    print(Fore.BLUE + "============================================================\n" + Style.RESET_ALL)


def is_posit_number(num_str):
    try:
        return float(num_str) > 0
    except ValueError:
        return False
