import random

# Definimos dos listas vacías para almacenar las personas y los puestos.
personas = []
puestos = []

# Pedimos al usuario que ingrese las personas y los puestos, y los agregamos a las listas correspondientes.
while True:
    persona = input("Ingresa el nombre de una persona (o presiona enter para terminar): ")
    if not persona:
        break
    personas.append(persona)

while True:
    puesto = input("Ingresa el nombre de un puesto (o presiona enter para terminar): ")
    if not puesto:
        break
    puestos.append(puesto)

# Asignamos aleatoriamente a cada persona un puesto.
asignaciones = random.sample(puestos, len(personas))

# Mostramos los resultados.
for i in range(len(personas)):
    print(f"{personas[i]} ha sido asignado/a al puesto de {asignaciones[i]}.")
