from firebase_admin import firestore
from colorama import init, Fore, Style, Back
from utils import get_field_values, show_all_db_info, show_filtered_tasks, get_collection_fields, get_valid_input
from icecream import ic


"""
Recuerda:

Los tipos de datos en Firestore son:
String : Texto.
Number : Número entero o decimal.
Boolean : Valor verdadero o falso.
Timestamp : Fecha y hora.
Geopoint : Coordenadas geográficas.
Array : Lista de elementos del mismo tipo.
Map : Diccionario de pares clave-valor.
Firestore infiere el tipo de datos de un campo basado en el valor que se le asigna. Si le asignas un valor de texto, el campo se convertirá automáticamente en String
    """

def add_task(collection):
    """
    - Descripción:
        - Funcion para añadir una nueva tarea a la colección. Se comprueba si la tarea ya existe ademas
        de otras comprobaciones relacionadas con los valores de prioridad (numerico de 1 a 5) y estado
        (Pendiente, Completada).
    - Parámetros:
        - collection: la colección de la base de datos de firestore.
    - Retorno:
        - No
    """
    # Generamos una lista con todas las descripciones de las tareas y los ids de las mismas.
    _, tasks_list = get_field_values(collection, 'Tarea')
    full_ids, _ = get_field_values(collection, 'Tarea')

    max_id = int(max(full_ids))

    #Solicitamos información y realizamos comprobaciones
    while   True:
        new_task = input("Añada el titulo de la nueva tarea:\n")
        if  new_task in tasks_list:
            print(Fore.RED + "El título especificado ya existe en la base de datos. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break
    new_desc = input("Añada la descripción para la tarea:\n")

    # Solicitamos prioridad y comprobamos con la funcion get_valid_input() en utils.py
    new_prior = get_valid_input("Añada la prioridad (1: alta - 5: baja):\n",
        lambda x: x.isdigit() and 1<= int(x) <= 5,
        "Prioridad incorrecta. Por favor, introduzca un número del 1 (alta) al 5 (baja)\n")

    # Solicitamos estado y comprobamos con la funcion get_valid_input() en utils.py
    new_status = get_valid_input("Añada el estado de la tarea (P: Pendiente, C: Completada):\n",
        lambda x: x in ['P', 'C'],
        "Estado incorrecto. Por favor, seleccione un estado válido\n")

    # Añado un nuevo documento
    collection.document(str(max_id + 1)).set(
        {
            'Tarea': new_task,
            'Descripcion': new_desc,
            'Prioridad': int(new_prior),
            'Estado': new_status,
        }
    )
    print(Fore.GREEN + "Tarea añadida correctamente!!\n\n" + Style.RESET_ALL)


def show_tasks(collection):
    """
    - Descripción:
        - Lista todas las tareas o filtradas por estado o prioridad
    - Parámetros:
        - collection: la colección de la base de datos de firestore
    - Retorno:
        - No
    """

    # Solicitamos tipo de filtro y comprobamos con la funcion get_valid_input() en utils.py
    filter_ind = get_valid_input(
        Fore.BLUE + """Elija el tipo de filtro:
             \t0 - Todas las tareas.
             \t1 - Filtrar por estado.
             \t2 - Filtrar por prioridad.\n""" + Style.RESET_ALL,
             lambda x: x.isdigit() and 0 <= int(x) <= 2,
             "Selección no válida. Inténtelo de nuevo\n")
    if  int(filter_ind) == 0:
        show_all_db_info(collection)

    elif  int(filter_ind) == 1:
        #obtenemos los posibles valores
        _, states = get_field_values(collection, 'Estado')
        # mostramos los valores
        print("\n")
        for index, state in enumerate(states):
            print(Fore.YELLOW + f"Índice: {index} - {state}" + Style.RESET_ALL)

        # Solicitamos valor para filtrar y comprobamos con la funcion get_valid_input() en utils.py
        index = get_valid_input("\nSeleccione el índice del valor a filtrar: ",
            lambda x: x.isdigit() and 0 <= int(x) <= len(states) - 1,
            "Índice incorrecto. Inténtelo de nuevo.\n")
        show_filtered_tasks(collection, 'Estado', states[int(index)])

    elif  int(filter_ind) == 2:
        #obtenemos los posibles valores
        _, prior = get_field_values(collection, 'Prioridad')
        print("\n")

        # Solicitamos prioridad y comprobamos con la funcion get_valid_input() en utils.py
        prior_s = get_valid_input("Seleccione la prioridad a filtrar (1 - 5): ",
            lambda x: x.isdigit() and 1 <= int(x) <= 5,
            "Prioridad incorrecta. Inténtelo de nuevo.\n")
        show_filtered_tasks(collection, 'Prioridad', prior_s)


def update_task(collection):
    """
    - Descripción:
        - Actualiza el valor de un campo de un documento
    - Parámetros:
        - collection: la colección de la base de datos de firestore
    - Retorno:
        - No
    """
    field_list = get_collection_fields(collection)
    full_ids, _ = get_field_values(collection, 'Tarea') #Lista con los IDs de la colección
    while   True:
        print("\n")
        # Mostramos toda la info de la colección
        show_all_db_info(collection)

        # Solicitamos ID de la tarea y comprobamos con la funcion get_valid_input() en utils.py
        id = get_valid_input("\nSeleccione el ID de la tarea que desea modificar: ",
            lambda x: x.isdigit() and x in full_ids,
            "El ID seleccionado no es válido. Inténtelo de nuevo.")

        # Mostramos los campos del documente
        for index, field in enumerate(field_list):
            print(Fore.YELLOW + f"{index} - {field}" + Style.RESET_ALL)

        # Solicitamos indice del campo a modificar y comprobamos con la funcion get_valid_input() en utils.py
        field_chosen = get_valid_input("\nSeleccione el índice del campo que desea modificar: ",
            lambda x: x.isdigit() and 0 <= int(x) <= len(field_list) - 1,
            "Selección no válida. Inténtelo de nuevo.")
        field_name = field_list[int(field_chosen)]

        # Solicitamos el cambio
        if  field_name == 'Estado':
            change = input("Introduzca el nuevo valor (P - Pendiente / C - Completada): ")
        else:
            change = input("Introduzca el nuevo valor: ")
        # Comprobamos
        if  field_list[int(field_chosen)] == 'Prioridad' and (not change.isdigit() or int(change) not in range(1,6)):
            print(Back.RED + "El valor debe ser un número entre 1 (prioridad alta) y 5 (prioridad baja)."+ Style.RESET_ALL)
            continue
        if  field_list[int(field_chosen)] == 'Estado' and change not in ['C', 'P']:
            print(Back.RED + "El valor solo puede ser 'C' (completada) o 'P' (Pendiente)."+ Style.RESET_ALL)
            continue
        break

    try:
        doc_ref = collection.document(id)
        update = doc_ref.update({field_name: change})
        print(Fore.GREEN + "Tarea actualizada correctamente.\n" + Style.RESET_ALL)
    except Exception as e:
        print(Back.RED + f"Error al actualizar la tarea: {e}" + Style.RESET_ALL)


def delete_task(collection):
    """
    - Descripción:
        - Borra la tarea seleccionada acorde al ID
    - Parámetros:
        - collection: la colección de la base de datos de firestore
    - Retorno:
        - No
    """
    full_ids, _ = get_field_values(collection, 'Tarea') #Lista con los IDs de la colección
    while   True:
        print("\n")
        # Mostramos toda la info de la colección
        show_all_db_info(collection)
        id = get_valid_input("\nSeleccione el ID de la tarea que desea eliminar: ",
            lambda x: x.isdigit() and x in full_ids,
            "El ID seleccionado no es válido. Inténtelo de nuevo.")
        break

        # Pedimos confirmación
    doc_ref = collection.document(id).get()
    task = doc_ref.to_dict()["Tarea"]
    confirm = input("Esta seguro de querer eliminar la tarea: " + Fore.YELLOW + f"{task}" + Style.RESET_ALL + " ? (s/n): " )
    if confirm != 's':
        print(Back.RED + "Eliminación cancelada.\n" + Style.RESET_ALL)
        return
    collection.document(id).delete()
    print(Fore.GREEN + "Tarea eliminada correctamente.\n" + Style.RESET_ALL)
