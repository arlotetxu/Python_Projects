"""
Ejercicio: Gestor de Tareas con Prioridades
Crea una aplicación en Python que gestione una lista de tareas usando SQLite3. El programa debe:

1.  Crear la base de datos:

    - Una tabla llamada tareas con las siguientes columnas:
        - id (entero, clave primaria, autoincremental)
        - descripcion (texto, no nulo)
        - estado (texto, con valores posibles "Pendiente" o "Completada", por defecto "Pendiente")
        - prioridad (entero, valores del 1 al 5, donde 1 es alta prioridad y 5 es baja)


2.  Opciones del menú:

    - Agregar una nueva tarea con descripción y prioridad.
    - Listar todas las tareas ordenadas por prioridad y luego por estado.
    - Marcar una tarea como completada.
    - Eliminar una tarea por su ID.
    - Mostrar todas las tareas con prioridad alta (prioridad 1 o 2).
    - Salir del programa.


3.  Requisitos adicionales:

    - Validar que los datos ingresados por el usuario sean válidos (por ejemplo, que la prioridad sea un número entre 1 y 5).
    - Confirmar antes de eliminar una tarea.
    - Guardar automáticamente los cambios en la base de datos.


Puntos a considerar:
    - Piensa en cómo manejarás las conexiones y los cursores a la base de datos.
    - Evalúa cómo implementarás las consultas SQL para cumplir con los requisitos.
    - Asegúrate de manejar excepciones para evitar que el programa falle inesperadamente.


4.  Info extra

Al crear una nueva tabla en SQLite3, los campos pueden tener varios atributos que definen su tipo de datos y restricciones. Aquí tienes algunos de los atributos más comunes:

INTEGER: Un número entero.
TEXT: Una cadena de texto.
REAL: Un número de punto flotante.
BLOB: Datos binarios.
NULL: Un valor nulo.
Además de los tipos de datos, puedes aplicar varias restricciones a los campos:

PRIMARY KEY: Define una clave primaria única para la tabla.
AUTOINCREMENT: Incrementa automáticamente el valor de un campo INTEGER.
NOT NULL: Asegura que el campo no puede contener valores nulos.
UNIQUE: Asegura que todos los valores en el campo sean únicos.
DEFAULT: Establece un valor por defecto para el campo si no se proporciona uno.
CHECK: Define una condición que los valores del campo deben cumplir.
Aquí tienes un ejemplo de cómo se vería una declaración de creación de tabla en SQLite3:

CREATE TABLE ejemplo (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    edad INTEGER,
    salario REAL DEFAULT 0.0,
    email TEXT UNIQUE,
    color TEXT CHECK(color IN ('blanco', 'negro'))
);
"""

from colorama import init, Fore, Style
import sqlite3
from utils import *

init()

def db_connect():
    """
    Descripción:
        Crea la conexion con la base de datos y genera la tabla "tareas" si no existe.
    Parámetros:
        - No
    Retorno:
        - conn: conexión a la base de datos. Este obejeto con la conexión será el parámetro para muchas de las
            funciones posteriores.
    """
    conn = sqlite3.connect('tareas.db')

    # Creamos el cursor para ejecutar las sentencias SQL
    cursor = conn.cursor()

    # Generamos la sentencia SQL para crear la tabla "tareas"
    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS tareas (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   descripcion TEXT NOT NULL,
                   estado TEXT DEFAULT 'Pendiente' CHECK(estado IN ('Pendiente', 'Completada')),
                   prioridad INTEGER CHECK(prioridad IN (1, 2, 3, 4, 5))
                   )
                """)

    # Guardamos los cambios
    conn.commit()
    return conn


def add_task(conn):
    """
    Descripción:
        Añadimos una nueva tarea a la tabla. Se realizan comprobaciones en los datos introducidos.
        TODO: Comprobar si la tarea añadida ya existe en la tabla de la BD
    Parámetros:
        - conn: conexión a la base de datos.
    Retorno:
        - No
    """
    # Generamos una lista con todas las descripciones de las tareas.
    task_desc_list = get_list_field(conn, 'descripcion')

    # Solicitamos la información al usuario
    while True:
        new_task = input("Añada la descripción para la nueva tarea:\n")
        if not new_task or new_task in task_desc_list:
            print(Fore.RED + "No es posible añadir una tarea en blanco o repetida. Intentelo de nuevo...\n\n" + Style.RESET_ALL)
            continue
        break
    while True:
        prior = input("Agregue una prioridad a la tarea (1-5): ")
        if not prior.isdigit() or not 1 <= int(prior) <= 5:
            print(Fore.RED + "Prioridad incorrecta. Solo valores de 1 (alta) a 5 (baja).\n\n" + Style.RESET_ALL)
            continue
        break

    # Creamos la sentencia SQL para añadir los datos a la tabla mediante un cursor
    cursor = conn.cursor()
    cursor.execute("""
                   INSERT INTO tareas(descripcion, prioridad)
                   VALUES (?, ?)
                   """, (new_task, prior))

    # Guardamos
    conn.commit()
    print(Fore.GREEN + "Tarea añadida correctamente!!" + Style.RESET_ALL)


def complete_task(conn):
    """
    Descripción:
        - Marca una tarea pendiente como completada. Para ello mostraremos solo las tareas pendientes.
    Parámetros:
        - conn: conexión a la base de datos
    Retorno:
        - No
    """
    cursor = conn.cursor()

    # Mostramos las tareas con estado 'Pendiente'
    show_task_filtered(conn, 'pend')

    # Añadimos a una lista los ids las tareas con estado 'Pendiente'
    cursor.execute("""
        SELECT id FROM tareas WHERE estado = 'Pendiente'
        """)
    ids_pend = cursor.fetchall()
    ids_pend_list = [id[0] for id in ids_pend]

    # Solicitamos el id al usuario
    while True:
        choice = input("Seleccione el ID de la tarea que desea marcar como 'Completada': ")

        if not choice.isdigit() or int(choice) not in ids_pend_list:
            print(Fore.RED + "El ID seleccionado no es correcto. Inténtelo de nuevo...\n" + Style.RESET_ALL)
            continue

        # Cambiamos el estado de la tarea seleccionada
        cursor.execute("""UPDATE tareas
            SET ESTADO = 'Completada'
            WHERE id = ?""", (int(choice), ))

        # Guardamos cambios
        conn.commit()
        break
    print(Fore.GREEN + "Tarea Completada!!\n" + Style.RESET_ALL)


def delete_task(conn):
    """
    Descripción:
        Muestra las tareas activas y elimina una tarea de la base de datos en funcion al id seleccionado
        por el usuario.
    Parámetros:
        - conn: Conexión a la base de datos.
    Retorno:
        - No
    """

    # Mostramos la lista de las tareas
    show_task_sorted(conn, 'id')

    cursor = conn.cursor()

    # Solicitamos el id a borrar y comprobamos input
    active_ids = get_list_field(conn, 'id') #Lista con los ids activos
    while True:
        to_delete_id = input("Seleccione el ID que desea eliminar: ")
        if not to_delete_id.isdigit() or int(to_delete_id) not in active_ids:
            print(Fore.RED + "El ID seleccionado no es correcto. Inténtelo de nuevo...\n" + Style.RESET_ALL)
            continue
        break
    cursor.execute("""
        SELECT * FROM tareas WHERE id = ?""", (to_delete_id, ))
    selected_id = cursor.fetchone()

    # Solicitamos confirmación para proceder con el borrado
    confirmation = input(f"¿Está seguro de querer borrar el ID: {selected_id[0]}? (s/n): ")
    if confirmation != 's':
        return

    # Procedemos con el borrado
    cursor.execute("""
        DELETE FROM tareas WHERE id = ?
        """, (to_delete_id, ))

    # Guardamos cambios
    conn.commit()
    print(Fore.GREEN + "Tarea eliminada con éxito!!\n" + Style.RESET_ALL)
    #show_tasks(conn, '')


def main_menu(conn):
    """
    Descripción:
        - Muestra el menú principal al usuario.
    Parámetros:
        - conn. La conexión a la base de datos
    Retorno:
        - No
    """
    while True:
        choice = input("""\nSeleccione la opción deseada:
        1- Agregar nueva tarea.
        2- Listar tareas ordenadas (prioridad y estado).
        3- Marcar tarea como completada.
        4- Eliminar tarea.
        5- Mostrar tareas de alta prioridad (1 o 2).
        6- Salir.\n""")

        if not choice.isdigit() or int(choice) < 1 or int(choice) > 6:
            print(Fore.RED + "Selección no válida. Intentelo de nuevo...\n\n" + Style.RESET_ALL)
            continue

        if int(choice) == 1:
            add_task(conn)
        elif int(choice) == 2:
            show_task_sorted(conn, 'prior')
            show_task_sorted(conn, 'est')
        elif int(choice) == 3:
            complete_task(conn)
        elif int(choice) == 4:
            delete_task(conn)
        elif int(choice) == 5:
            show_task_filtered(conn, 'h_prior')
        elif int(choice) == 6:
            print(Fore.CYAN + "Saliendo del programa. ¡Hasta luego!" + Style.RESET_ALL)
            break



if __name__ == '__main__':
    conn = db_connect()
    main_menu(conn)
