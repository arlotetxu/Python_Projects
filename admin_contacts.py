'''
Ejercicio: Administrador de contactos

Crea un programa que permita gestionar una agenda de contactos. Cada contacto debe tener la siguiente información:
	•	Nombre
	•	Teléfono
	•	Correo electrónico

El programa debe permitir al usuario realizar las siguientes acciones:
	1.	Agregar un contacto.
	2.	Eliminar un contacto (por nombre).
	3.	Mostrar todos los contactos.
	4.	Buscar un contacto (por nombre).
	5.	Salir.

Requisitos:

	1.	Usa un diccionario para almacenar los contactos, donde el nombre sea la clave y el valor sea un diccionario con teléfono y correo.
	2.	Valida las entradas del usuario:
	•	El número de teléfono debe ser un número válido.
	•	El correo electrónico debe contener @ y un dominio (por ejemplo, @gmail.com).
	3.	Maneja casos en los que:
	•	Se intente agregar un contacto que ya existe.
	•	Se intente eliminar o buscar un contacto que no existe.

Ejemplo de flujo:

Seleccione una acción:
1 - Agregar contacto
2 - Eliminar contacto
3 - Mostrar contactos
4 - Buscar contacto
5 - Salir

Ingrese su elección: 1
Ingrese el nombre del contacto: Juan Pérez
Ingrese el teléfono: 123456789
Ingrese el correo electrónico: juan.perez@gmail.com
Contacto agregado exitosamente.

Ingrese su elección: 3
Lista de contactos:
- Juan Pérez: Teléfono: 123456789, Correo: juan.perez@gmail.com
'''
from email_validator import validate_email, EmailNotValidError
from colorama import init, Fore, Back, Style

init()


def add_contact(db_contact: dict) -> dict:
    name = input("Introduzca un nuevo nombre: ")
    if name in db_contact.keys():
        print(Fore.RED + "\nEl nombre introducido ya existe en la base de datos. Inténtelo de nuevo.\n\n" + Style.RESET_ALL)
        return db_contact
    phone = input("Introduzca el número de teléfono: ")
    if not phone.isdigit():
        print(Fore.RED + "\nEl número de teléfono introducido no es correcto. Inténtelo de nuevo\n\n" +
            Style.RESET_ALL)
        return db_contact
    email = input("Introduzca la dirección de correo electrónico: ")
    try:
        validate_email(email)
    except EmailNotValidError:
        print(Fore.RED + "\nEl email introducido no es correcto. Inténtelo de nuevo.\n\n" + Style.RESET_ALL)
        return db_contact
    print("\n\n")
    new_info = {"Teléfono": phone, "email": email}
    db_contact[name]= new_info
    print(Fore.GREEN + "\nContacto agregado correctamente.\n" + Style.RESET_ALL)
    return db_contact


def del_contact(db_contact: dict) -> dict:
    to_del = input("Introduzca el nombre que desea borrar: ")
    if not to_del in db_contact.keys():
        print(Fore.RED + f"El nombre {to_del} no se encuentra en la lista. Inténtelo de nuevo\n\n" + Style.RESET_ALL)
        return db_contact
    del db_contact[to_del]
    print(Fore.YELLOW + "Contacto eliminado.\n\n" + Style.RESET_ALL)
    return db_contact


def show_contacts(db_contact: dict) -> None:
    if not db_contact:
        print(Fore.YELLOW + "\nLa lista de contactos está vacía.\n\n"+ Style.RESET_ALL)
        return
    print("\n============Contactos=============\n")
    for name, details in db_contact.items():
        print(Fore.LIGHTBLUE_EX + f"Nombre: {name}")
        print(Fore.LIGHTYELLOW_EX + f"Teléfono: {details['Teléfono']}")
        print(Fore.LIGHTMAGENTA_EX + f"Email: {details['email']}\n" + Style.RESET_ALL)
    print("\n==================================\n\n")


def find_contact(db_contact: dict) -> None:
    to_find = input("Introduzca el nombre que desea buscar: ")
    if db_contact:
        if to_find not in db_contact.keys():
            print(Fore.RED + "Contacto no encontrado. Intentelo de nuevo\n\n" + Style.RESET_ALL)
            return

        print("\n============ Contacto encontrado =============\n")
        print(Fore.LIGHTBLUE_EX + f"Nombre: {to_find}")
        print(Fore.LIGHTYELLOW_EX + f"Teléfono: {db_contact[to_find]['Teléfono']}")
        print(Fore.LIGHTMAGENTA_EX + f"Email: {db_contact[to_find]['Email']}\n" + Style.RESET_ALL)
        print("==============================================\n")


def menu(db_contact: dict):
    while True:
        choice = input("""Seleccione un acción:
            \t1 - Agregar contacto.
            \t2 - Eliminar contacto.
            \t3 - Mostrar contacto.
            \t4 - Buscar contacto.
            \t5 - Salir.\n\n""")
        if not choice.isdigit() or int(choice) > 5 or int(choice) < 1:
            print(Back.RED + "Selección no valida. Intentelo de nuevo\n\n" + Style.RESET_ALL)
            continue

        if int(choice) == 1:
            add_contact(db_contact)
        elif int(choice) == 2:
            del_contact(db_contact)
        elif int(choice) == 3:
            show_contacts(db_contact)
        elif int(choice) == 4:
            find_contact(db_contact)
        elif int(choice) == 5:
            print(Fore.GREEN + "¡Gracias por usar el gestor de contactos! Hasta pronto.\n" + Style.RESET_ALL)
            break

if __name__ == "__main__":
    db_contact = {}
    menu(db_contact)
