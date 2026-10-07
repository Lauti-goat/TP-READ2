# Ejercicio 5 - Sistema de consultas de órdenes de reparación

ordenes = [
    {
        "numero": 1001,
        "cliente": "Juan Pérez",
        "equipo": "Notebook Lenovo",
        "falla": "No enciende",
        "estado": "Pendiente",
        "costo": 45000
    },
    {
        "numero": 1002,
        "cliente": "María López",
        "equipo": "PC Dell",
        "falla": "Problemas de temperatura",
        "estado": "En reparación",
        "costo": 60000
    },
    {
        "numero": 1003,
        "cliente": "Carlos Gómez",
        "equipo": "Notebook HP",
        "falla": "Pantalla dañada",
        "estado": "Finalizada",
        "costo": 90000
    },
    {
        "numero": 1004,
        "cliente": "Sofía Ruiz",
        "equipo": "PC Lenovo",
        "falla": "No inicia Windows",
        "estado": "Pendiente",
        "costo": 50000
    },
    {
        "numero": 1005,
        "cliente": "Martín Díaz",
        "equipo": "Notebook Asus",
        "falla": "Teclado defectuoso",
        "estado": "En reparación",
        "costo": 35000
    },
    {
        "numero": 1006,
        "cliente": "Lucía Torres",
        "equipo": "PC HP",
        "falla": "Disco rígido dañado",
        "estado": "Finalizada",
        "costo": 75000
    },
    {
        "numero": 1007,
        "cliente": "Pedro Sánchez",
        "equipo": "Notebook Dell",
        "falla": "Batería agotada",
        "estado": "Pendiente",
        "costo": 30000
    },
    {
        "numero": 1008,
        "cliente": "Ana Fernández",
        "equipo": "PC Gamer",
        "falla": "Problemas de placa de video",
        "estado": "En reparación",
        "costo": 120000
    }
]


def mostrar_orden(orden):
    print("\nNúmero:", orden["numero"])
    print("Cliente:", orden["cliente"])
    print("Equipo:", orden["equipo"])
    print("Falla:", orden["falla"])
    print("Estado:", orden["estado"])
    print("Costo estimado: $", orden["costo"])


def mostrar_todas():
    if len(ordenes) == 0:
        print("No existen órdenes cargadas.")
        return

    print("\n--- TODAS LAS ÓRDENES ---")

    for orden in ordenes:
        mostrar_orden(orden)


def buscar_orden(numero):
    for orden in ordenes:
        if orden["numero"] == numero:
            return orden

    return None


def filtrar_por_estado(estado):
    encontrados = 0

    print("\n--- ÓRDENES POR ESTADO ---")

    for orden in ordenes:
        if orden["estado"].lower() == estado.lower():
            mostrar_orden(orden)
            encontrados += 1

    if encontrados == 0:
        print("No existen órdenes con ese estado.")


def filtrar_por_costo(limite):
    encontrados = 0

    print("\n--- ÓRDENES SEGÚN COSTO ---")

    for orden in ordenes:
        if orden["costo"] <= limite:
            mostrar_orden(orden)
            encontrados += 1

    if encontrados == 0:
        print("No existen órdenes cuyo costo sea menor o igual al límite.")


# Menú principal

while True:

    print("\n========== MENÚ ==========")
    print("1. Buscar orden por número")
    print("2. Filtrar órdenes por estado")
    print("3. Filtrar órdenes por costo")
    print("4. Mostrar todas las órdenes")
    print("5. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        numero = int(input("Ingrese el número de orden: "))

        orden = buscar_orden(numero)

        if orden is not None:
            mostrar_orden(orden)
        else:
            print("No se encontró una orden con ese número.")

    elif opcion == "2":

        estado = input("Ingrese el estado: ")
        filtrar_por_estado(estado)

    elif opcion == "3":

        limite = float(input("Ingrese el costo máximo: "))
        filtrar_por_costo(limite)

    elif opcion == "4":

        mostrar_todas()

    elif opcion == "5":

        print("Programa finalizado.")
        break

    else:
        print("Opción inválida.")