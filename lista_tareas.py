from curses.ascii import isdigit
'''
Ejercicio: Gestión de una lista de tareas

Crea un programa que permita al usuario gestionar una lista de tareas. El programa debe ofrecer las siguientes opciones:
	1.	Agregar una nueva tarea.
	2.	Mostrar todas las tareas.
	3.	Eliminar una tarea por su posición en la lista.
	4.	Salir.

Requisitos:

	•	Usa una lista para almacenar las tareas.
	•	Maneja posibles errores, como intentar eliminar una tarea que no existe.
	•	Asegúrate de que el programa sea interactivo y claro para el usuario.
'''

import sys

def add_task(task_list):
    task = input("Describa la tarea a añadir:\n")
    task_list.append(task)
    print("Tarea añadida.\n")
    print("=====================================\n\n")


def remove_task(task_list):
    if not task_list:
        print("No hay tareas en la lista.\n")
        return
    #Mostramos las tareas
    for index, task in enumerate(task_list):
        print(f"Índice: {index} -- {task}")
    try:
        c_index = int(input("seleccione el indice de la tarea a eliminar:"))
        if 0 <= c_index < len(task_list):
            task_list.pop(c_index)
            print("Tarea eliminada.\n")
        else:
            print("Indice fuera de rango.")
    except ValueError:
        print("Por favor, ingrese un indice válido.\n")
    print("=====================================\n\n")


def show_tasks(task_list):
    if not task_list:
        print("No hay tareas en la lista.\n")
        return
    for index, task in enumerate(task_list):
        print(f"Índice: {index} -- {task}")
    print("=====================================\n\n")


def menu(task_list):
    while True:
        try:
            choice = int(input("\033[92mSeleccionar opción:\n1 - Añadir.\n2 - Eliminar.\n3 - Mostrar.\n4 - Salir\033[0m\n\n"))
            if choice == 1:
                add_task(task_list)
            elif choice == 2:
                remove_task(task_list)
            elif choice == 3:
                show_tasks(task_list)
            elif choice == 4:
                print("Hasta pronto!!.")
                break
            else:
                print("Seleccione una opción válida...\n\n")
        except ValueError:
            print("Intentelo de nuevo...\n\n")


if __name__ == "__main__":
    task_list = []
    menu(task_list)
