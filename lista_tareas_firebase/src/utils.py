import warnings
from colorama import init, Back, Fore, Style
warnings.filterwarnings("ignore", category=UserWarning)

def get_field_values(collection, field):
    """
    - Descripción:
        - Obtiene los valores del campo pasado en el parámetro 'field' de la colección.
    - Parámetros:
        - Collection: Coleccion de datos de Firestore.
        - Field: campo de la colección del que se quieren obtener los valores
    - Retorno:
        - values: lista con los diferentes valores obtenidos.
    """
    values = []
    ids = []
    all_data = collection.stream()
    for data in all_data:
        field_value = data.to_dict().get(field)
        if field_value:
            values.append(field_value)
            ids.append(data.id)
    return ids, list(set(values))   #set() solo almacena valores unicos


def show_all_db_info(collection):
    """
    - Descripción:
        - Muestra todos los valores de la colección FireBase / Firestock
    - Parámetros:
        - Collection: Coleccion de datos de Firestore.
    - Retorno:
        - No
    """
    all_tasks = list(collection.stream())
    if  not all_tasks:
        print(Back.RED + "No hay tareas en la colección.\n" + Style.RESET_ALL)
    #ic(all_tasks)
    for task in sorted(all_tasks, key=lambda x: x.id, reverse=True):
        print(Fore.YELLOW + f"\nID: {task.id}")
        print(f"\nTarea: {task.to_dict()['Tarea']}")
        print(f"Descripción: {task.to_dict()['Descripcion']}")
        print(f"Prioridad: {task.to_dict()['Prioridad']}")
        print(f"Estado: {task.to_dict()['Estado']}")
        print("========================================" + Style.RESET_ALL)


def show_filtered_tasks(collection, filter_field: str, value:str):
    """
    - Descripción:
        - Muestra todos los valores de la colección FireBase / Firestock filtrado por un campo
    - Parámetros:
        - Collection: Coleccion de datos de Firestore.
    - Retorno:
        - No
    """
    if  filter_field == 'Prioridad':
        value = int(value)

    filtered_tasks = list(collection.where(filter_field, '==', value).stream())
    if  not filtered_tasks:
        print(Back.RED + "No hay tareas con la seleccion actual.\n" + Style.RESET_ALL)
    for task in filtered_tasks:
        print(Fore.YELLOW + f"\nTarea: {task.to_dict()['Tarea']}")
        print(f"Descripción: {task.to_dict()['Descripcion']}")
        print(f"Prioridad: {task.to_dict()['Prioridad']}")
        print(f"Estado: {task.to_dict()['Estado']}")
        print("========================================" + Style.RESET_ALL)


def get_collection_fields(collection):
    """
    - Descripción:
        - Obtiene todos los campos de la colección
    - Parámetros:
        - Collection: Coleccion de datos de Firestore.
    - Retorno:
        - No
    """
    field_names = set()  # Usamos set para evitar duplicados
    # Iteramos por todos los documentos
    for doc in collection.stream():
        # Añadimos los campos de cada documento
        field_names.update(doc.to_dict().keys())
    return list(field_names)
