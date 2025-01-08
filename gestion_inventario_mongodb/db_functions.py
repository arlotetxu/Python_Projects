from utils import is_posit_number, printing, get_field_set, is_posit_number
from colorama import init, Fore, Style

init()


def add_record(collection):
    """
    - Descripcion:
        - Inserta un registro o colleccion en la tabla 'productos' de la coleccion 'inventario'. Si no
        se especifica un campo llamado '_id', mongodb genera automáticamente un identificador por cada registro.
    - Parámetros:
        - collection: recibe la coleccion a la que añadir los registros
    - Retorno:
        - No
    """
    #database = client["inventario"]
    #collection = database["productos"]
    while True:
        new_product = input("Indique el nombre del nuevo producto: ")
        if new_product in collection.distinct("Nombre"):
            print(Fore.RED + "El nombre de producto ya existe en la Base de datos.\n" + Style.RESET_ALL)
            continue
        new_category = input("Agregue la categoría: ")
        new_quantity = input("Cantidad?: ")
        new_price = input("Precio?: ")
        #if not new_quantity.isdigit() or not new_price.isdigit():
        if not is_posit_number(new_quantity):
            print(Fore. RED + "Alguno de los valores es incorrecto. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break

    try:
        adding_list = [
            {"Nombre": new_product.lower(), "Categoria": new_category.lower(), "Cantidad": int(new_quantity),
                "Precio Eur": float(new_price)},
        ]
        collection.insert_many(adding_list) # Para añadir un valor a un campo: .insert_one()
        # Esto es similar pero añadiendo solo un campo a la tabla:
        #MongoClient(MONGO_URI,tlsCAFile=certifi.where()).inventario.productos.insert_one({"Nombre": new_product})

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return

    print(Fore.GREEN + "Registro guardado.\n\n" + Style.RESET_ALL)


def show_all(collection):
    """
    - Descripción:
        - Muestra todos los registros de la colección 'productos'. Evita imprimir el campo '_id'.
    - Parámetros:
        - collection: conexion a la colección en MongoDB
    - Retorno:
        - No
    """
    try:
        print(Fore.BLUE + f"\n================== INFO EN TABLA: {collection.name} ==================\n" + Style.RESET_ALL)
        result = collection.find({}, {"_id": 0}) # No imprime el campo '_id'
        #result = collection.find({}) # Imprime todos los campo de la colección
        printing(result)

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")
        return


def show_by_field(collection):
    """
    - Descripción:
        - Muestra los datos filtrados por el campo.
    - Parámetros:
        - collection: conexion a la colección en MongoDB
    - Retorno:
        - No
    """
    # PRIMERO solicitamos el campo sobre el que filtrar
    field_list = list(get_field_set(collection))
    while True:
        for index, field in enumerate(field_list):
            print(f"Index: {index} -- {field}")
        field_ind_choice = input("\nSeleccione el índice del campo que desea filtrar: ")

        # Comprobaciones
        if not field_ind_choice.isdigit() or not 0 <= int(field_ind_choice) <= (len(field_list) - 1):
            print(Fore.RED + "Indice incorrecto. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break
    field_selected = field_list[int(field_ind_choice)]
    print("Campo seleccionado: " + Fore.BLUE + f"{field_selected}. " + Style.RESET_ALL + "Posibles valores:\n")

    # SEGUNDO solicitamos que valor del campo usar para filtrar
    values = collection.distinct(field_selected)
    while True:
        for index, field_value in enumerate(values):
            print(f"Index: {index} -- {field_value}")
        field_val_id_choice = input("\nSeleccione el índice del valor que desea filtrar: ")

        # Comprobaciones
        if not field_val_id_choice.isdigit() or int(field_val_id_choice) < 0 or int(field_val_id_choice) > len(values) - 1:
            print(Fore.RED + "Indice incorrecto. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break
    value_selected = values[int(field_val_id_choice)]
    print("Valor seleccionado: " + Fore.BLUE + f"{value_selected}\n" + Style.RESET_ALL)

    # Aplicando el filtro una vez tenemos el campo y el valor
    result = collection.find({field_selected: value_selected})
    printing(result) #TODO retornar la lista y lanzar la impresion desde la funcion menu


def update_prod(collection):
    """
    - Descripción:
        - Actualiza el valor de cantidad o precio segun el nombre indicado.
    - Parámetros:
        - collection: conexion a la colección en MongoDB
    - Retorno:
        - No
    """
    names = collection.distinct('Nombre')

    # PRIMERO solicitamos el nombre para actualizar sus datos y comprobamos
    while True:
        for index, name in enumerate(names):
            print(f"Index: {index} -- {name}")
        ind_choice = input("\nSeleccione el índice del nombre que desea modificar: ")

        #comprobaciones
        if not ind_choice.isdigit() or not (0 <= int(ind_choice) <= (len(names) - 1)):
            print(Fore.RED + "Indice incorrecto. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break

    # SEGUNDO solicitamos que valor se desea actualizar 'Cantidad' o 'Precio Eur'
    valid_fields = ['Cantidad', 'Precio Eur']
    while True:
        print(Fore.BLUE + "\n --- Posibles campos para actualizar ---" + Style.RESET_ALL)
        for index, field in enumerate(valid_fields):
            print(f"Index: {index} -- {field}")
        ind_field_choice = input("\nSeleccione el índice del campo que desea actualizar:\n")

        #comprobaciones
        if not ind_field_choice.isdigit() or not (0 <= int(ind_field_choice) <= (len(valid_fields) - 1)):
            print(Fore.RED + "Indice incorrecto. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break

    while True:
        new_value = input(f"Indique el nuevo valor para el campo {valid_fields[int(ind_field_choice)]}: ")
        #if not new_value.isdigit():
        if not is_posit_number(new_value):
            print(Fore.RED + "El valor introducido no es correcto. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break

    query_filter = {'Nombre' : names[int(ind_choice)]}
    update_operation = { '$set' :
        { valid_fields[int(ind_field_choice)] : float(new_value) }
    }
    result = collection.update_one(query_filter, update_operation)
    print(Fore.GREEN + "Registro modificado.\n\n" + Style.RESET_ALL)


def del_record(collection):
    """
    - Descripción:
        - Borra un registro de la colección segun su nombre.
    - Parámetros:
        - collection: conexion a la colección en MongoDB
    - Retorno:
        - No
    """
    names = collection.distinct('Nombre')

    # PRIMERO solicitamos el nombre que se desea borrar y comprobamos
    while True:
        for index, name in enumerate(names):
            print(f"Index: {index} -- {name}")
        ind_choice = input("\nSeleccione el índice del nombre que desea borrar:\n")

        #comprobaciones
        if not ind_choice.isdigit() or not (0 <= int(ind_choice) <= (len(names) - 1)):
            print(Fore.RED + "Indice incorrecto. Inténtelo de nuevo.\n" + Style.RESET_ALL)
            continue
        break

    collection.delete_one({"Nombre": names[int(ind_choice)]})
    print(Fore.GREEN + "Registro borrado.\n\n" + Style.RESET_ALL)
