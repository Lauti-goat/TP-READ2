# Ejercicio 6 - POO: catálogo de dispositivos de red


class DispositivoRed:

    def __init__(self, codigo, tipo, marca, velocidad_mbps, precio, stock):
        self.codigo = codigo
        self.tipo = tipo
        self.marca = marca
        self.velocidad_mbps = velocidad_mbps
        self.precio = precio
        self.stock = stock

    def mostrar_datos(self):
        print("\nCódigo:", self.codigo)
        print("Tipo:", self.tipo)
        print("Marca:", self.marca)
        print("Velocidad:", self.velocidad_mbps, "Mbps")
        print("Precio: $", self.precio)
        print("Stock:", self.stock)

    def hay_stock(self):
        return self.stock > 0


# Crear objetos

dispositivos = [
    DispositivoRed("R001", "Router", "TP-Link", 1200, 85000, 4),
    DispositivoRed("R002", "Router", "Mercusys", 300, 45000, 0),
    DispositivoRed("S001", "Switch", "TP-Link", 1000, 60000, 5),
    DispositivoRed("S002", "Switch", "D-Link", 100, 35000, 3),
    DispositivoRed("A001", "Access Point", "Ubiquiti", 1200, 150000, 2),
    DispositivoRed("A002", "Access Point", "TP-Link", 300, 50000, 0)
]


def buscar_por_velocidad(velocidad_minima):

    encontrados = 0

    print("\n--- DISPOSITIVOS CON VELOCIDAD SUFICIENTE Y STOCK ---")

    for dispositivo in dispositivos:

        if dispositivo.velocidad_mbps >= velocidad_minima and dispositivo.hay_stock():
            dispositivo.mostrar_datos()
            encontrados += 1

    if encontrados == 0:
        print("No existen dispositivos que cumplan las condiciones.")


def buscar_por_codigo(codigo):

    for dispositivo in dispositivos:

        if dispositivo.codigo.lower() == codigo.lower():
            return dispositivo

    return None


def buscar_por_presupuesto(presupuesto):

    encontrados = 0

    print("\n--- DISPOSITIVOS DENTRO DEL PRESUPUESTO ---")

    for dispositivo in dispositivos:

        if dispositivo.hay_stock() and dispositivo.precio <= presupuesto:
            dispositivo.mostrar_datos()
            encontrados += 1

    if encontrados == 0:
        print("No existen dispositivos con stock que entren en el presupuesto.")


# Mostrar todos los dispositivos

print("========== CATÁLOGO DE DISPOSITIVOS ==========")

for dispositivo in dispositivos:
    dispositivo.mostrar_datos()


# Consulta por velocidad

velocidad = int(input("\nIngrese la velocidad mínima en Mbps: "))
buscar_por_velocidad(velocidad)


# Consulta por código

codigo = input("\nIngrese el código de un dispositivo para buscarlo: ")

dispositivo_encontrado = buscar_por_codigo(codigo)

if dispositivo_encontrado is not None:
    print("\nDispositivo encontrado:")
    dispositivo_encontrado.mostrar_datos()
else:
    print("No se encontró ningún dispositivo con ese código.")


# Consulta por presupuesto

presupuesto = float(input("\nIngrese el presupuesto máximo: "))
buscar_por_presupuesto(presupuesto)


# Explicación final

print("\n--- Ventaja de utilizar POO ---")
print("Representar cada dispositivo como un objeto permite agrupar sus")
print("datos y comportamientos en una misma estructura. Además, cada")
print("objeto puede utilizar métodos como mostrar_datos() y hay_stock(),")
print("haciendo que el código sea más organizado y fácil de reutilizar.")