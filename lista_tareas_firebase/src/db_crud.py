from colorama import init, Fore, Style, Back
from utils import get_field_values
#from inspect import getfile
from icecream import ic

def add_task(collection):
    """
    Descripción:
        Añadimos una nueva tarea a la coleccion. Se realizan comprobaciones en los datos introducidos.
        TODO: Generar un documento tipo json para guardar el id que vamos generando. Utils.py
        TODO: Comprobar si la tarea añadida ya existe en la tabla de la BD
    Parámetros:
        - colection: conexión a la base de datos.
    Retorno:
        - No

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
    #ic(type(max_id))

    #Solicitamos información y realizamos comprobaciones
    while   True:
        new_task = input("Añada el titulo de la nueva tarea:\n")
        if  new_task in tasks_list:
            print(Fore.RED + "El título especificado ya existe en la base de datos. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break
    new_desc = input("Añada la descripción para la tarea:\n")
    while   True:
        new_prior = input("Añada la prioridad (1: alta - 5: baja):\n")
        if  not new_prior.isdigit() or not 1 <= int(new_prior) <= 5:
            print(Back.RED + "Prioridad incorrecta. Por favor, introduzca un número del 1 (alta) al 5 (baja)\n" + Style.RESET_ALL)
            continue
        break
    while   True:
        new_status = input("Añada el estado de la tarea (P: Pendiente, C: Completada):\n")
        if  new_status not in ['P', 'C']:
            print(Back.RED + "Estado incorrecto. Por favor, seleccione un estado válido\n" + Style.RESET_ALL)
            continue
        break

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
    2.	Listar tareas:
	   •	Mostrar todas las tareas con opción de filtrar por estado o prioridad.
    """
    while   True:
        filter_ind = input("""Elija el tipo de filtro:
            \t0 - Todas las tareas.
            \t1 - Filtrar por estado.
            \t2 - Filtrar por prioridad.\n""")

        if  not filter_ind.isdigit() or not 0 <= int(filter_ind) <= 2:
            print(Back.RED + "Selección no válida. Inténtelo de nuevo\n" + Style.RESET_ALL)
            continue
        break
    if  int(filter_ind) == 0:
        all_task = list(collection.stream())
        ic(all_task)
        for task in sorted(all_task, key=lambda x: x.id, reverse=True):
            print(f"Tarea: {task.to_dict()['Tarea']}")
            print(f"Descripción: {task.to_dict()['Descripcion']}")
            for key, value in task.to_dict().items():
                if  key not in ['Tarea', 'Descripcion']:
                    print(f"{key}: {value}")
            print("========================================")
