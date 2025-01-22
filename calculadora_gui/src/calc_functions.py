from tkinter.constants import END


def click_button(value, calc_screen):
    """
    - Descripción:
        - Función que maneja los clicks sobre los propios botones de la calculadora.
    - Parámetros:
        - value: el valor del botón clicado en la calculadora.
        - calc_screen: el widget de visor que hemos creado
    - Retorno:
        - No
    """
    if  value == 'C':
        calc_screen.delete(0, 'end')
        """0: Es la posición inicial desde donde queremos empezar a eliminar texto y 'end' hasta donde queremos limpiar"""
    elif    value == '=':
        calculate(calc_screen)
    else:
        current = calc_screen.get()  # Obtener el texto actual de la entrada
        calc_screen.delete(0, 'end')  # Limpiar la entrada.
        calc_screen.insert(0, current + value)  # Agregar el nuevo valor al final


def key_press(event, calc_screen):
    key = event.char    # Capturar la tecla presionada
    if key.isdigit() or key in "+-*/":
        calc_screen.insert(END, key)
    elif key == '\r':   # Si se presiona Enter (tecla "Return")
        calculate(calc_screen)
    elif key == '\x08':
        calc_screen.delete(len(calc_screen.get()) - 1, 'end')



def calculate(calc_screen):
    try:
        result = eval(calc_screen.get())
        """La función eval() es una función incorporada en Python que evalúa una expresión de Python en forma de cadena y devuelve el resultado."""
        calc_screen.delete(0, END)
        calc_screen.insert(0, str(result))
    except Exception as e:
        current = calc_screen.get()  # Obtener el texto actual de la entrada
        calc_screen.delete(0, 'end')  # Limpiar la entrada.
        calc_screen.insert(0, f"Error: {e}")  # Agregar el nuevo valor al final
