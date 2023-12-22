# Inicializar el diccionario de puestos y funciones
puestos_funciones = {}

# Función para ingresar un puesto y sus funciones asociadas
def ingresar_puesto():
    puesto = input("Ingrese el nombre del puesto: ")
    funciones = input("Ingrese las funciones del puesto, separadas por comas: ")
    puestos_funciones[puesto] = funciones.split(",")
    
# Función para asignar una persona a un puesto
def asignar_persona():
    persona = input("Ingrese el nombre de la persona: ")
    puesto = input("Ingrese el nombre del puesto: ")
    if puesto in puestos_funciones:
        if puestos_funciones[puesto] != []:
            print("El puesto ya está ocupado")
        else:
            puestos_funciones[puesto] = [persona]
    else:
        print("El puesto no existe")

# Función para mostrar la lista de puestos y personas asignadas
def mostrar_puestos():
    print("Lista de puestos y personas asignadas:")
    persona: asignar_persona()
    for puesto, funciones in puestos_funciones.items():
        print(f"- {puesto}: {', '.join(funciones)(persona)}")
        

# Menú principal
while True:
    print("1. Ingresar un puesto y sus funciones")
    print("2. Asignar una persona a un puesto")
    print("3. Mostrar la lista de puestos y personas asignadas")
    print("4. Salir")
    opcion = input("Ingrese su opción: ")
    
    if opcion == "1":
        ingresar_puesto()
    elif opcion == "2":
        asignar_persona()
    elif opcion == "3":
        mostrar_puestos()
    elif opcion == "4":
        break
    else:
        print("Opción inválida")
