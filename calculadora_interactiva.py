'''
Crea un programa que funcione como una calculadora básica interactiva. El programa debe permitir al usuario realizar las siguientes operaciones:
	1.	Suma de dos números.
	2.	Resta de dos números.
	3.	Multiplicación de dos números.
	4.	División de dos números.
	5.	Salir.

Requisitos:

	•	Cada operación debe implementarse en una función separada.
	•	El programa debe manejar los siguientes casos:
	    • División por cero.
		• Entradas no numéricas.
	•	Usa un menú interactivo que permita al usuario seleccionar qué operación desea realizar.
	•	Incluye mensajes claros y amigables para el usuario.


Seleccione una operación:
1 - Sumar
2 - Restar
3 - Multiplicar
4 - Dividir
5 - Salir

Ingrese su elección: 1
Ingrese el primer número: 5
Ingrese el segundo número: 3
El resultado de la suma es: 8
'''
from colorama import init, Fore, Back, Style
from sys import exit

init()

def addition (num_1: float, num_2: float) -> float:
    return num_1 + num_2


def subtract (num_1: float, num_2: float) -> float:
    return num_1 - num_2


def multi (num_1: float, num_2: float) -> float:
    return num_1 * num_2


def division (num_1: float, num_2: float) -> float:
    try:
        return num_1 / num_2
    except ZeroDivisionError:
        print(Fore.RED + "No es posible dividir entre 0!!!\n\n" + Style.RESET_ALL)
        return None


def get_number(prompt: str) -> float:
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print(Fore.RED + "El valor ingresado no es un número. Intente de nuevo.\n" + Style.RESET_ALL)


def menu():
    while True:
        option = input("""Ingrese su eleccion:
            \t1 - Sumar
            \t2 - Restar
            \t3 - Multiplicar
            \t4 - Dividir
            \t5 - Salir\n""")
        if not option.isdigit() or int(option) not in range (1, 6):
            print(Fore.RED + "Selección no válida. Intente de nuevo.\n" + Style.RESET_ALL)
            continue

        if int(option) == 5:
            print("Hasta pronto!!")
            break

        num_1 = get_number("\nIngrese el primer número: ")
        num_2 = get_number("\nIngrese el segundo número: ")

        if int(option) == 1:
            print(Fore.LIGHTYELLOW_EX + f"El resultado: {addition(float(num_1), float(num_2))}\n\n" + Style.RESET_ALL)
        elif int(option) == 2:
            print(Fore.LIGHTYELLOW_EX + f"El resultado: {subtract(float(num_1), float(num_2))}\n\n" + Style.RESET_ALL)
        elif int(option) == 3:
            print(Fore.LIGHTYELLOW_EX + f"El resultado: {multi(float(num_1), float(num_2))}\n\n" + Style.RESET_ALL)
        elif int(option) == 4:
            res = division(num_1, num_2)
            if res is not None:
                print(Fore.LIGHTYELLOW_EX + f"El resultado: {res}\n\n" + Style.RESET_ALL)

if __name__ == "__main__":
    menu()
