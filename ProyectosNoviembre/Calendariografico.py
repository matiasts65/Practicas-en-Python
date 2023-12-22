import tkinter as tk
from tkinter import tkcalendar

def save_event():
    date = cal.selection_get()
    event = event_entry.get()
    if date and event:
        with open('calendario.txt', 'a') as f:
            f.write(f"{date}: {event}\n")
        event_entry.delete(0, tk.END)

def load_events():
    event_list.delete(0, tk.END)
    try:
        with open('calendario.txt', 'r') as f:
            events = f.readlines()
            for event in events:
                event_list.insert(tk.END, event)
    except FileNotFoundError:
        pass

def clear_events():
    event_list.delete(0, tk.END)
    with open('calendario.txt', 'w') as f:
        pass

app = tk.Tk()
app.title("Calendario de Organización")

cal = tkcalendar.Calendar(app)
cal.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

event_label = tk.Label(app, text="Evento:")
event_label.grid(row=1, column=0, padx=10, pady=10, sticky=tk.E)

event_entry = tk.Entry(app)
event_entry.grid(row=1, column=1, padx=10, pady=10)

add_event_button = tk.Button(app, text="Agregar Evento", command=save_event)
add_event_button.grid(row=2, column=0, padx=10, pady=10, columnspan=2)

load_events_button = tk.Button(app, text="Cargar Eventos", command=load_events)
load_events_button.grid(row=3, column=0, padx=10, pady=10)

clear_events_button = tk.Button(app, text="Limpiar Eventos", command=clear_events)
clear_events_button.grid(row=3, column=1, padx=10, pady=10)

event_list = tk.Listbox(app, selectmode=tk.SINGLE, height=10, width=40)
event_list.grid(row=4, column=0, padx=10, pady=10, columnspan=2)

app.mainloop()
