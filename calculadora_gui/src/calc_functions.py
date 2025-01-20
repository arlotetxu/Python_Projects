
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
        try:
            result = eval(calc_screen.get())
            """La función eval() es una función incorporada en Python que evalúa una expresión de Python en forma de cadena y devuelve el resultado."""
            calc_screen.delete(0, 'end')
            calc_screen.insert(0, str(result))
        except Exception as e:
            calc_screen.delete(0, 'end')
            calc_screen.insert(0, str(f"Error: {e}"))
    else:
        current = calc_screen.get()  # Obtener el texto actual de la entrada
        calc_screen.delete(0, 'end')  # Limpiar la entrada.
        calc_screen.insert(0, current + value)  # Agregar el nuevo valor al final
