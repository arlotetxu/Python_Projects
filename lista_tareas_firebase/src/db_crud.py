from colorama import init, Fore, Style
from utils import get_field_values

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


    doc_ref = collection_ref.document("tu_documento")
    doc_ref.set({
        "nombre": "Juan",
        "edad": 30,
        "activo": True,
        "fecha_nacimiento": firestore.Timestamp(firestore.datetime.datetime(1990, 1, 1)),
        "ubicacion": firestore.GeoPoint(40.7128, -74.0060),
        "hobbies": ["leer", "correr", "cocinar"],
        "datos_extra": {
            "ciudad": "New York",
            "pais": "Estados Unidos"
        }
    })

Reemplaza "tu_documento" con el ID del documento que quieres crear.

Define los campos y sus valores con los tipos de datos correspondientes.

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
        - collection: la colección de la base de datos de firestock.
    - Retorno:
        - No
    """
    # Generamos una lista con todas las descripciones de las tareas.
    tasks_list = get_field_values(collection, 'Tarea')
    full_ids = get_field_values(collection, '')

    for task in tasks_list:
        print(task)
