# Este programa permite llevar un registro de personas, incluyendo su nombre, edad y correo electrónico.

class Persona:
  def __init__(self, nombre, edad, correo):
    self.nombre = nombre
    self.edad = edad
    self.correo = correo

personas = []

while True:
  print("\n1. Registrar persona")
  print("2. Mostrar lista de personas")
  print("3. Salir")
  opcion = input("Ingrese una opción: ")

  if opcion == "1":
    nombre = input("Ingrese el nombre de la persona: ")
    edad = input("Ingrese la edad de la persona: ")
    correo = input("Ingrese el correo electrónico de la persona: ")
    persona = Persona(nombre, edad, correo)
    personas.append(persona)
    print("Persona registrada con éxito.")

  elif opcion == "2":
    print("Nombre                Edad  Correo electrónico")
    print("-------------------------------------------------")
    for persona in personas:
      print(f"{persona.nombre:20} {persona.edad:4}  {persona.correo}")
    print("-------------------------------------------------")

  elif opcion == "3":
    break

  else:
    print("Opción inválida. Intente de nuevo.")
