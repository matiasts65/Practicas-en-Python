import tkinter as tk

def click(event):
    text = event.widget.cget("text")
    
    if text == "=":
        try:
            result = str(eval(screen.get()))
            screen.set(result)
        except Exception as e:
            screen.set("Error")
    elif text == "C":
        screen.set("")
    else:
        screen.set(screen.get() + text)

root = tk.Tk()
root.title("Calculadora")

screen = tk.StringVar()
entry = tk.Entry(root, textvar=screen, font="Arial 20", bd=10, insertwidth=4, width=14, justify="right")
entry.grid(row=0, column=0, columnspan=4)

button_texts = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]

row_val = 1
col_val = 0

for button_text in button_texts:
    button = tk.Button(root, text=button_text, font="Arial 20", padx=20, pady=20)
    button.grid(row=row_val, column=col_val)
    button.bind("<Button-1>", click)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
