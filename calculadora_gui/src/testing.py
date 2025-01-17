from tkinter import Tk, Entry, Button

# Crear ventana
root = Tk()
root.title("Calculadora")

# Crear entrada que ocupa columnas
screen = Entry(root, width=40)
screen.grid(row=0, column=0, columnspan=4)  # Cambia entre columnspan=2 y columnspan=4

# Agregar botones en filas y columnas
Button(root, text="1").grid(row=1, column=0)
Button(root, text="2").grid(row=1, column=1)
Button(root, text="3").grid(row=1, column=2)
Button(root, text="4").grid(row=1, column=3)

root.mainloop()
