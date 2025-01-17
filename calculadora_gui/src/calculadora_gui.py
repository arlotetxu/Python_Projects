import tkinter as tk
from tkinter import Tk, Entry, Button

# Crear ventana principal
root = tk.Tk()
root.title("Calculadora Básica JMF")

# Establecer dimensiones de la ventana
root.geometry("400x300")  # Ancho x Alto

# Configurar las columnas para que se expandan
for i in range(4):  # Hay 4 columnas
    root.columnconfigure(i, weight=1)

# Crear la pantalla de la calculadora donde se mostraran numeros y resultado
"""
Explicación:

    tk.Entry:
        Es un widget para texto editable.
        Le aplicamos una fuente grande con font=("Arial", 24) para que sea visible.
        justify="right" alinea el texto a la derecha, como en una calculadora real.
        bd=10 define el grosor del borde.

    grid:
        Posiciona el widget en un sistema de cuadrícula.
        row=0 indica la primera fila.
        column=0 indica la primera columna.
        columnspan=4 hace que el widget ocupe las 4 columnas de la fila.
        padx y pady añaden espacio alrededor del widget.
"""
screen = tk.Entry(root, font=("Arial", 17), justify="right", bd=10)
screen.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Botones de la calculadora
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_index = 1  # Comienza en la fila 1 (después de la entrada)
col_index = 0  # Comienza en la columna 0

# Función para manejar los clics en los botones
def click_button(value):
    current = screen.get()  # Obtener el texto actual de la entrada
    screen.delete(0, 'end')  # Limpiar la entrada
    screen.insert(0, current + value)  # Agregar el nuevo valor al final

for button in buttons:
    # Crear un botón con el texto correspondiente
    btn = Button(root, text=button, width=8, height=2,
        command=lambda b=button: click_button(b)) # Asignar la función
    btn.grid(row=row_index, column=col_index)

    # Avanzar a la siguiente posición en el grid
    col_index += 1
    if col_index > 3:  # Si llegamos a la cuarta columna, pasamos a la siguiente fila
        col_index = 0
        row_index += 1

# Ejecutar el bucle principal de la interfaz gráfica
root.mainloop()
