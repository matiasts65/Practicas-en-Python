# Definir una clase Evento para representar eventos en el calendario
class Evento:
    def __init__(self, fecha, titulo, descripcion):
        self.fecha = fecha
        self.titulo = titulo
        self.descripcion = descripcion

# Definir una clase Calendario que almacene eventos
class Calendario:
    def __init__(self):
        self.eventos = []

    def agregar_evento(self, evento):
        self.eventos.append(evento)

    def ver_eventos(self):
        for evento in self.eventos:
            print(f"Fecha: {evento.fecha}")
            print(f"Título: {evento.titulo}")
            print(f"Descripción: {evento.descripcion}")
            print("-" * 30)

# Función principal para interactuar con el calendario
def main():
    calendario = Calendario()

    while True:
        print("Opciones:")
        print("1. Agregar evento")
        print("2. Ver eventos")
        print("3. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            fecha = input("Fecha del evento (DD/MM/YYYY): ")
            titulo = input("Título del evento: ")
            descripcion = input("Descripción del evento: ")
            evento = Evento(fecha, titulo, descripcion)
            calendario.agregar_evento(evento)
            print("Evento agregado correctamente.")
        elif opcion == "2":
            calendario.ver_eventos()
        elif opcion == "3":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
