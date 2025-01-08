"""
APRENDIENDO

Ejercicio: Gestor de Contactos con SQLite3

Vamos a crear un programa que gestione una base de datos de contactos. Podrás:
	1.	Agregar un nuevo contacto con un nombre, número de teléfono y correo electrónico.
	2.	Mostrar todos los contactos almacenados en la base de datos.
	3.	Actualizar la información de un contacto existente.
	4.	Eliminar un contacto de la base de datos.

Requisitos
	•	Biblioteca: Usaremos sqlite3, que viene incluida con Python.
	•	Tablas: Crearemos una tabla llamada contactos con las columnas id, nombre, telefono y email.
"""

from colorama import init, Fore, Style
import sqlite3

init()

def connect_db():
    """
    Conecta a la base de datos SQLite3 y crea la tabla de contactos si no existe.
    """
    conn = sqlite3.connect("contacts.db")

    """
    Un cursor es un objeto que nos permite ejecutar comandos SQL en la base de datos.
	•	Aquí, estamos creando un cursor llamado cursor a partir de nuestra conexión conn.
	•	El cursor se usa para enviar consultas SQL a la base de datos y recuperar resultados.
    """
    cursor = conn.cursor()

    """
    cursor.execute( ... ):
    Esto ejecuta una consulta SQL que crea una tabla llamada contactos si no existe previamente.
    """
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS contactos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            telefono TEXT NOT NULL,
            email TEXT NOT NULL
        )
    """)

    """
    conn.commit():
    Esto guarda los cambios realizados en la base de datos.
     •	Aquí asegura que la tabla contactos se cree de forma permanente en el archivo contacts.db.
    """
    conn.commit()
    return conn


def add_contact(conn):
    """
    Agrega un nuevo contacto a la base de datos.
    """
    nombre = input("Ingrese el nombre: ")
    telefono = input("Ingrese el teléfono: ")
    email = input("Ingrese el email: ")
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contactos (nombre, telefono, email)
        VALUES (?, ?, ?)
    """, (nombre, telefono, email))
    conn.commit()
    print(Fore.GREEN + "Contacto añadido con éxito.\n" + Style.RESET_ALL)


def show_contacts(conn):
    """
    Muestra los contactos de la DB
    """
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM contactos")
    contactos = cursor.fetchall()
    """
   	•	Recupera todos los resultados de la consulta y los almacena en la variable contactos.
	•	contactos será una lista de tuplas, donde cada tupla representa un registro (fila) en la tabla.
    """
    if not contactos:
        print(Fore.YELLOW + "No hay contactos en la base de datos.\n" + Style.RESET_ALL)
        return
    print(Fore.BLUE + "\n--- Lista de Contactos ---" + Style.RESET_ALL)
    for contacto in contactos:
        print(f"ID: {contacto[0]}, Nombre: {contacto[1]}, Teléfono: {contacto[2]}, Email: {contacto[3]}")
    print("     ---     ")


def update_contact(conn):
    """
    Actualiza un contacto existente en la base de datos.
    """
    show_contacts(conn)
    # Recuperamos en una lista los id de los contactos existentes en la base de datos
    cursor = conn.cursor()
    cursor.execute("""
                   SELECT id FROM contactos""")
    ids = cursor.fetchall()
    id_list = [id_[0] for id_ in ids]

    id_contacto = input("Ingrese el ID del contacto a actualizar: ")
    # Comprobamos si el id introducido se encuentra en la lista de ids y es un valor numerico
    if not id_contacto.isdigit() or int(id_contacto) not in id_list:
        print(Fore.RED + "El ID introducido no es correcto o no se encuentra. Inténtelo de nuevo.\n" + Style.RESET_ALL)
        return
    
    nuevo_nombre = input(f"Ingrese el nuevo nombre para el ID {id_contacto}: ")
    nuevo_telefono = input(f"Ingrese el nuevo teléfono para ID {id_contacto}: ")
    nuevo_email = input(f"Ingrese el nuevo email para el ID {id_contacto}: ")
    #cursor = conn.cursor()

    """
    Recuperamos los datos existentes con el Id indicado por si el usuario no quiere actualizar alguno de los campos
    para mantener el valor actual
    """
    cursor.execute("SELECT * FROM contactos WHERE id = ?", (id_contacto,))
    contacto_actual = cursor.fetchone()


    nombre = nuevo_nombre if nuevo_nombre else contacto_actual[1]
    telefono = nuevo_telefono if nuevo_telefono else contacto_actual[2]
    email = nuevo_email if nuevo_email else contacto_actual[3]
    cursor.execute("""
                  UPDATE contactos
                  SET nombre = ?, telefono = ?, email = ?
                  WHERE id = ?
                  """, (nombre, telefono, email, id_contacto))
    conn.commit()

    print(Fore.GREEN + "Contacto actualizado con éxito.\n" + Style.RESET_ALL)
    show_contacts(conn)


def delete_contact(conn):
    '''
    Elimina un contacto de la base de datos en funcion de su Id
    '''
    show_contacts(conn)
    id_contacto = input("Ingrese el ID de contacto que desea eliminar: ")

    cursor = conn.cursor()

    # Seleccionamos solo el contacto que coincide con el id introducido y guardamos sus valores en 'contacto_select'
    cursor.execute("""
        SELECT * FROM contactos WHERE id = ?"""
        , (id_contacto,))
    contacto_select = cursor.fetchone()

    if not contacto_select:
        print(Fore.RED + "No se encontró un contacto con ese ID.\n" + Style.RESET_ALL)
        return

    # Solicitamos confirmacion previa antes de eliminar
    confirmacion = input(Fore.RED + f"¿Está seguro de eliminar de la base de datos a {contacto_select[1]}? (s/n): " + Style.RESET_ALL)
    if confirmacion != 's':
        return

    # Ejecutamos la eliminación del contacto
    cursor.execute("""
        DELETE FROM contactos WHERE id = ?
        """, (id_contacto,))
    conn.commit()

    print(Fore.GREEN + "Contacto eliminado con éxito.\n" + Style.RESET_ALL)
    show_contacts(conn)


def menu(conn):
    '''
    Muestra el menú principal del programa al usuario.
    '''
    while True:
        opcion = input("""Seleccione la opción deseada:
              1 - Agregar un nuevo contacto.
              2 - Mostrar contactos.
              3 - Actualizar información de contacto.
              4 - Borrar contacto.
              5 - Salir
              \n""")
        if not opcion.isdigit() or int(opcion) not in range(1, 6):
            print(Fore.RED + "Opción no válida. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue

        if int(opcion) == 1:
            add_contact(conn)
        elif int(opcion) == 2:
            show_contacts(conn)
        elif int(opcion) == 3:
            update_contact(conn)
        elif int(opcion) == 4:
            delete_contact(conn)
        elif int(opcion) == 5:
            print(Fore.CYAN + "Saliendo del programa. ¡Hasta luego!" + Style.RESET_ALL)
            break


if __name__ == "__main__":
    conn = connect_db()
    try:
        menu(conn)
    finally:
        conn.close()


"""
def menu(conn):
    '''
    Muestra el menú principal del programa.
    '''
    while True:
        print('''
Seleccione una opción:
    1 - Agregar contacto
    2 - Mostrar contactos
    3 - Actualizar contacto
    4 - Eliminar contacto
    5 - Salir
        ''')
        opcion = input("Opción: ")
        if opcion == "1":
            add_contact(conn)
        elif opcion == "2":
            show_contacts(conn)
        elif opcion == "3":
            update_contact(conn)
        elif opcion == "4":
            delete_contact(conn)
        elif opcion == "5":
            print(Fore.CYAN + "Saliendo del programa. ¡Hasta luego!" + Style.RESET_ALL)
            break
        else:
            print(Fore.RED + "Opción no válida. Inténtelo de nuevo.\n" + Style.RESET_ALL)

if __name__ == "__main__":
    conn = connect_db()
    try:
        menu(conn)
    finally:
        conn.close()
"""
