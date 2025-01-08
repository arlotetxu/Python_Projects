
"""
Ejercicio: Gestor de inventario con MongoDB

Implementa un programa en Python que permita:
	1.	Añadir productos:
	   •	Cada producto debe tener un nombre, categoría, cantidad y precio.
	2.	Listar productos:
	   •	Mostrar todos los productos o filtrar por categoría.
	3.	Actualizar productos:
	   •	Cambiar la cantidad o el precio de un producto dado su nombre.
	4.	Eliminar productos:
	   •	Eliminar un producto de la base de datos.

Detalles adicionales
	1.	Usa pymongo para interactuar con MongoDB.
	2.	Diseña el programa para que tenga un menú interactivo similar al del gestor de contactos.
	3.	Guarda y reutiliza la conexión a la base de datos en todo el programa.


Curso driver Python: https://learn.mongodb.com/learning-paths/using-mongodb-with-python
Docs PyMongo: https://www.mongodb.com/docs/languages/python/pymongo-driver/current/get-started/


A Cluster is the container for the databases.
A collection in MongoDB is a table in a data base.
A document in MongoDB is a record in a collection

"""

from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
import certifi
from colorama import init, Fore, Style
from dotenv import load_dotenv
import os
from pickle import GET
from webbrowser import get
from db_functions import add_record, show_all, show_by_field, update_prod, del_record

init() # Inicia colorama
load_dotenv() # Carga las variables de entorno del archivo .env

MONGO_URI = os.getenv("MONGO_URI")

def start_connection(uri):
    try:
        # Usar certifi para los certificados
        # Crea el cliente de MongoDB
        client = MongoClient(
            uri,
            tlsCAFile=certifi.where()
        )

        # Envía un ping para verificar la conexión
        client.admin.command('ping')
        print(Fore.GREEN + "Conexión exitosa" + Style.RESET_ALL)

        # Opcional: lista las bases de datos disponibles
        # print("Bases de datos disponibles:", client.list_database_names())
        return client
    except ConnectionFailure as e:
        print(Fore.RED + f"Error de conexión: {e}" + Style.RESET_ALL)
        return None


def menu(collection):
    """
    - Descripción:
        - Muestra el menú principal al usuario.
        - Parámetros:
            - collection: conexion a la colección en MongoDB
        - Retorno:
            - No
    """
    while True:
        print(Fore.BLUE + "ACCIONES:" +
            """
            \tIndex 1 - Añadir nuevo registro.
            \tIndex 2 - Mostrar registros.
            \tIndex 3 - Actualizar valor de un registro.
            \tIndex 4 - Borrar registro.
            \tIndex 5 - Salir
            """ + Style.RESET_ALL)
        choice = input("Seleccione el índice de la acción que desea realizar: ")

        # Comprobaciones
        if not choice.isdigit() or not 0 < int(choice) <= 5:
            print(Fore.RED + "El índice seleccionado no es válido. Inténtelo de nuevo.\n\n" + Style.RESET_ALL)
            continue

        # Lanzamos acciones
        if int(choice) == 1:
            add_record(collection)
        elif int(choice) == 2:
            print("\n\n")
            for index, field in enumerate(['Todos los registros', 'Según campo de tabla']):
                print(f"Index {index}: {field}")
            shw_choice = input("\nSeleccione índice deseado: ")

            # Comprobaciones
            if not shw_choice.isdigit() or not 0<= int(shw_choice) <= 1:
                print(Fore.RED + "El índice seleccionado no es válido. Inténtelo de nuevo.\n\n" + Style.RESET_ALL)
                continue

            if int(shw_choice) == 0:
                show_all(collection)
            elif int(shw_choice) == 1:
                show_by_field(collection)
        elif int(choice) == 3:
            update_prod(collection)
        elif int(choice) == 4:
            del_record(collection)
        elif int(choice) == 5:
            print("Saliendo.. ¡Hasta pronto!")
            break


if __name__ == "__main__":
    client = start_connection(MONGO_URI)
    database = client["inventario"]
    collection = database["productos"]

    menu(collection)
    client.close()
