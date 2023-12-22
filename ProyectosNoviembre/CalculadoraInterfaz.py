### 1. Calculadora Interactiva

import tkinter as tk

def perform_operation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operator = operator_var.get()

        if operator == "+":
            result.set(num1 + num2)
        elif operator == "-":
            result.set(num1 - num2)
        elif operator == "*":
            result.set(num1 * num2)
        elif operator == "/":
            result.set(num1 / num2)
    except ValueError:
        result.set("Error")

# Crear la ventana principal
window = tk.Tk()
window.title("Calculadora")

# Variables para almacenar números y resultado
entry_num1 = tk.Entry(window)
entry_num2 = tk.Entry(window)
operator_var = tk.StringVar()
result = tk.StringVar()

# Interfaz gráfica
label_num1 = tk.Label(window, text="Número 1:")
label_num2 = tk.Label(window, text="Número 2:")
label_result = tk.Label(window, textvariable=result)
radio_add = tk.Radiobutton(window, text="+", variable=operator_var, value="+")
radio_subtract = tk.Radiobutton(window, text="-", variable=operator_var, value="-")
radio_multiply = tk.Radiobutton(window, text="*", variable=operator_var, value="*")
radio_divide = tk.Radiobutton(window, text="/", variable=operator_var, value="/")
calculate_button = tk.Button(window, text="Calcular", command=perform_operation)

# Colocar elementos en la ventana
label_num1.pack()
entry_num1.pack()
label_num2.pack()
entry_num2.pack()
radio_add.pack()
radio_subtract.pack()
radio_multiply.pack()
radio_divide.pack()
calculate_button.pack()
label_result.pack()

# Iniciar el loop de la interfaz gráfica
window.mainloop()
