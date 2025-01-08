from colorama import init, Fore, Style

def get_list_field(conn, field):
    """
    Descripción:
        Guarda en una lista los ids de las tareas que permanecen en la tabla 'tareas' de la base de datos
        'tareas.db'.
    Parámetros:
        - conn: Conexión a la base de datos
    Retorno:
        - ids_list: lista con los ids que permanecen activos
    """

    cursor = conn.cursor()
    query_str = (f"SELECT {field} FROM tareas")
    cursor.execute(query_str)
    returned_data = cursor.fetchall()
    ids_list = [id[0] for id in returned_data]
    #print(ids_list)
    return ids_list


def show_task_sorted(conn, sort_by):
    """
    Descripción:
        Muestra las tareas contenidas en la base de datos ordenandolas segun el valor que recibimos en
        sort_by.
    Parámetros:
        - conn: conexión a la base de datos
        - sort_by. Puede recibir los valores 'prior', 'est' o 'id' segun se vayan a ordernar por prioridad,
            estado o id.
    Retorno:
        - No
    """
    # Asignamos el valor de la columna a ordenar en la variable sorting
    sorting = 'prioridad' if sort_by == 'prior' else 'estado' if sort_by == 'est' else 'id' if sort_by == 'id' else ''
    if not sorting:
        return

    #Generamos la consulta a la base de datos construyendo un string adecuado segun el criterio de ordenación
    cursor = conn.cursor()
    query_str = f"SELECT * FROM tareas ORDER BY {sorting} ASC"
    cursor.execute(query_str)
    data_retrieved = cursor.fetchall()

    # Comprobamos que recibimos datos de la consulta
    if not data_retrieved:
        print(Fore.RED + "\nNo hay tareas en la tabla.\n" + Style.RESET_ALL)
        return

    # Imprimimos
    print(Fore.BLUE + f"\n============== Lista Tareas ordenadas por {sorting.upper()} ==============" + Style.RESET_ALL)
    for task in data_retrieved:
        print(f"ID: {task[0]} -- Desc.: {task[1]} \n\t-- Estado: {task[2]} -- Prioridad: {task[3]}\n")



def show_task_filtered(conn, filter_by):
    """
    Descripción:
        Muestra las tareas contenidas en la base de datos filtrandolas segun el valor que recibimos en
        filter_by.
    Parámetros:
        - conn: conexión a la base de datos
        - filter_by. Puede recibir los valores 'pend', 'comp' o 'h_prior' segun se vayan a filtrar por
        tareas pendientes, completadas o con prioridad alta (1 y 2).
    Retorno:
        - No
    """
    # Asignamos el valor de la columna a ordenar en la variable sorting
    filtering = 'Pendiente' if filter_by == 'pend' else 'Completada' if filter_by == 'comp' else 'Prioridad Alta'\
        if filter_by == 'h_prior' else ''
    if not filter_by:
        return

    #Generamos la consulta a la base de datos construyendo un string adecuado segun el criterio de ordenación
    cursor = conn.cursor()
    query_str = f"SELECT * FROM tareas WHERE estado = '{filtering}' ORDER BY prioridad ASC"
    if filter_by == 'h_prior':
        query_str = f"SELECT * FROM tareas WHERE prioridad = 1 OR prioridad = 2 ORDER BY prioridad ASC"
    cursor.execute(query_str)
    data_retrieved = cursor.fetchall()

    # Comprobamos que recibimos datos de la consulta
    if not data_retrieved:
        print(Fore.RED + "\nNo hay tareas en la tabla.\n" + Style.RESET_ALL)
        return

    # Imprimimos
    print(Fore.BLUE + f"\n============== Lista Tareas filtrada por {filtering.upper()} ==============" + Style.RESET_ALL)
    for task in data_retrieved:
        print(Fore.CYAN + f"ID: {task[0]} -- Desc.: {task[1]}" + Style.RESET_ALL + \
            f"\n\t-- Estado: {task[2]} -- Prioridad: {task[3]}\n")
    print("\n\n")
