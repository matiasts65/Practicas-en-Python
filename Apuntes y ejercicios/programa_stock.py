# Este programa permite llevar un registro del stock de mercaderías de un negocio.

class Mercaderia:
  def __init__(self, codigo, nombre, cantidad):
    self.codigo = codigo
    self.nombre = nombre
    self.cantidad = cantidad

  def agregar(self, cantidad):
    self.cantidad += cantidad

  def retirar(self, cantidad):
    if cantidad > self.cantidad:
      print("No hay suficiente cantidad de", self.nombre)
    else:
      self.cantidad -= cantidad

mercaderias = []

while True:
  print("\n1. Agregar mercadería")
  print("2. Retirar mercadería")
  print("3. Mostrar stock")
  print("4. Salir")
  opcion = input("Ingrese una opción: ")

  if opcion == "1":
    codigo = input("Ingrese el código de la mercadería: ")
    nombre = input("Ingrese el nombre de la mercadería: ")
    cantidad = int(input("Ingrese la cantidad de la mercadería: "))
    mercaderia = Mercaderia(codigo, nombre, cantidad)
    mercaderias.append(mercaderia)
    print("Mercadería agregada con éxito.")

  elif opcion == "2":
    codigo = input("Ingrese el código de la mercadería: ")
    for mercaderia in mercaderias:
      if mercaderia.codigo == codigo:
        cantidad = int(input("Ingrese la cantidad a retirar: "))
        mercaderia.retirar(cantidad)
        break
    else:
      print("Mercadería no encontrada.")

  elif opcion == "3":
    print("Código  Nombre          Cantidad")
    print("----------------------------------")
    for mercaderia in mercaderias:
      print(f"{mercaderia.codigo}      {mercaderia.nombre:14} {mercaderia.cantidad}")
    print("----------------------------------")

  elif opcion == "4":
    break

  else:
    print("Opción inválida. Intente de nuevo.")
