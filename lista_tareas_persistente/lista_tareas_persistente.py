'''
Ejercicio: Gestor de tareas persistente

Crea un programa que funcione como un gestor de tareas persistente. Las tareas deben guardarse en un archivo de texto (tareas.txt) para que no se pierdan al cerrar el programa. Cada tarea debe tener la siguiente información:
	•	Descripción de la tarea
	•	Estado (Pendiente o Completada)

Opciones del menú:
1.	Agregar tarea:
    Permite al usuario añadir una nueva tarea con estado “Pendiente” por defecto.
2.	Mostrar tareas:
    Muestra todas las tareas numeradas junto con su estado (Pendiente/Completada).
3.	Marcar tarea como completada:
    El usuario seleccionará una tarea por su número para marcarla como “Completada”.
4.	Eliminar tarea:
    Elimina una tarea seleccionada por su número.
5.	Guardar y salir:
    Guarda todas las tareas en el archivo tareas.txt y termina el programa.


Requisitos adicionales:
1.	Al iniciar el programa:
    Si existe un archivo tareas.txt, el programa debe cargar las tareas guardadas previamente.
    Si no existe, debe crear un archivo vacío al cerrar.
2.	Formato del archivo:
    Guarda las tareas en el siguiente formato (una tarea por línea):
    Descripción de la tarea,Estado
    Comprar comida,Pendiente
    Estudiar Python,Completada


3.	Validación de entradas:
	•	El usuario debe ingresar una opción válida en el menú.
	•	Se deben manejar los errores si el archivo no puede leerse/escribirse correctamente.


Ejemplo de flujo:

Seleccione una opción:
1 - Agregar tarea
2 - Mostrar tareas
3 - Marcar tarea como completada
4 - Eliminar tarea
5 - Guardar y salir

Ingrese su elección: 1
Ingrese la descripción de la tarea: Estudiar programación
¡Tarea añadida con éxito!

Ingrese su elección: 2
Tareas actuales:
1. Estudiar programación [Pendiente]

Ingrese su elección: 3
Seleccione el número de la tarea a completar: 1
Tarea marcada como completada.

Ingrese su elección: 5
Guardando tareas... ¡Hasta pronto!
'''

import os
from colorama import init, Fore, Style

init()

def add_task(db_tasks: list) -> list:
    task_desc = input("Ingrese la descripción de la tarea: ")
    for task in db_tasks:
        if task[0].lower() == task_desc.lower():
            print(Fore.RED + "La tarea ya existe. Inténtelo de nuevo\n\n" + Style.RESET_ALL)
            return db_tasks
    db_tasks.append([task_desc, 'Pendiente'])
    #print(db_tasks)
    print(Fore.GREEN + "Tarea añadida con éxito!!\n\n" + Style.RESET_ALL)
    return db_tasks
    clear_screen()


def show_tasks(db_tasks: list) -> None:
    clear_screen()
    if not db_tasks:
        print(Fore.RED + "La lista de tareas está vacía.\n\n" + Style.RESET_ALL)
        return
    print("\n======================== LISTA DE TAREAS ============================\n")
    for id, task in enumerate(db_tasks):
        print(f"{id}. {task[0]} [{task[1]}]")
    print("\n======================================================================\n\n")


def complete_task(db_tasks: list) -> list:
    if not db_tasks:
        print(Fore.RED + "La lista de tareas está vacía.\n\n" + Style.RESET_ALL)
        return db_tasks

    to_complete = input("Seleccione el número de la tarea a completar: ")
    if not to_complete.isdigit() or (int(to_complete) > len(db_tasks) - 1) or (int(to_complete) < 0):
        print(Fore.RED + "Selección no válida\n\n" + Style.RESET_ALL)
        return db_tasks

    if db_tasks[int(to_complete)][1] == 'Completada':
        print(Fore.RED + "La tarea seleccionada ya se encuentra completada.\n\n" + Style.RESET_ALL)
        return db_tasks
    db_tasks[int(to_complete)][1] = 'Completada'
    print(Fore.GREEN + "Tarea completada con éxito\n\n" + Style.RESET_ALL)
    clear_screen()
    return db_tasks


def delete_task(db_tasks: list) -> list:
    if not db_tasks:
        print(Fore.RED + "La lista de tareas está vacía.\n\n" + Style.RESET_ALL)
        return db_tasks

    to_delete = input("Seleccione el nùmero de la tarea a eliminar: ")
    if not to_delete.isdigit() or (int(to_delete) > len(db_tasks)) or (int(to_delete) < 0):
        print(Fore.RED + "Selección no válida\n\n" + Style.RESET_ALL)
        return db_tasks
    #Adding a confirmation prior to delete the task
    confirm = input(f"¿Está seguro de que desea eliminar la tarea {db_tasks[int(to_delete)]}? (s/n): ")
    if confirm.lower() != 's':
        print(Fore.YELLOW + "Operación cancelada.\n\n" + Style.RESET_ALL)
        return db_tasks
    db_tasks.pop(int(to_delete))
    print(Fore.GREEN + "Tarea eliminada con éxito\n\n" + Style.RESET_ALL)
    return db_tasks


def open_prog(db_tasks: list, filename: str) -> list:
    #filename = 'tareas.txt'
    try:
        with open(filename) as f_o:
            for line in f_o:
                task, status = [item.strip() for item in line.split(",")]
                #Check if the status value is correct. If not, change to 'Pendiente'
                if status not in ['Pendiente', 'Completado']:
                    status = 'Pendiente'
                db_tasks.append([task, status])
    except FileNotFoundError:
        print(Fore.RED + "Archivo de tareas no encontrado. Generando 'tareas.txt'..." + Style.RESET_ALL)
        with open(filename, 'w') as f_o:
            pass
        print(Fore.GREEN + "Archivo creado correctamente.\n\n" + Style.RESET_ALL)
    clear_screen()
    return(db_tasks)


def close_prog(db_tasks: list, filename: str) -> None:
    try:
        with open(filename, 'w') as f_o:
            for task in db_tasks:
                f_o.write(f"{task[0]}, {task[1]}\n")
    except FileNotFoundError:
        print(Fore.RED + "Archivo de tareas no encontrado. Generando 'tareas.txt'..." + Style.RESET_ALL)
        with open(filename, 'w') as f_o:
            pass
        print(Fore.GREEN + "Archivo creado correctamente.\n\n" + Style.RESET_ALL)
        close_prog(db_tasks, filename)


def clear_screen():
    # Para Windows
    if os.name == 'nt':
        os.system('cls')
    # Para Mac y Linux (os.name es 'posix')
    else:
        os.system('clear')


def	menu(db_tasks: list, filename: str) -> None:
    while True:
        choice = input("""Seleccione un opción:
            \t1 - Agregar tarea
            \t2 - Mostrar tareas
            \t3 - Marcar tarea como completada
            \t4 - Eliminar tarea
            \t5 - Guardar y salir\n""")

        if not choice.isdigit() or not 1 <= int(choice) <= 5:
            print(Fore.RED + "Selección no válida. Inténtelo de nuevo.\n\n" + Style.RESET_ALL)
            continue
        if int(choice) == 1:
            add_task(db_tasks)
        elif int(choice) == 2:
            show_tasks(db_tasks)
        elif int(choice) == 3:
            complete_task(db_tasks)
        elif int(choice) == 4:
            delete_task(db_tasks)
        elif int(choice) == 5:
            close_prog(db_tasks, filename)
            print("Guardando tareas... ¡Hasta pronto!")
            break


if __name__ == "__main__":
    db_tasks = []
    filename = "tareas.txt"
    open_prog(db_tasks, filename)
    menu(db_tasks, filename)
