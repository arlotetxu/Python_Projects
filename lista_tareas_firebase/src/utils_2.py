from colorama import Fore, Back, Style

def printing_tasks(task):
    print(Fore.YELLOW + f"\nID: {task.id}")
    print(f"\nTarea: {task.to_dict()['Tarea']}")
    print(f"Descripción: {task.to_dict()['Descripcion']}")
    print(f"Prioridad: {task.to_dict()['Prioridad']}")
    print(f"Estado: {task.to_dict()['Estado']}")
    print("========================================" + Style.RESET_ALL)
