# Ejercicio 2 - Buscador flexible de repuestos

repuestos = [
    {"codigo": "R001", "descripcion": "SSD Kingston 480 GB", "categoria": "Almacenamiento", "marca": "Kingston", "precio": 45000, "stock": 5},
    {"codigo": "R002", "descripcion": "SSD Crucial 1 TB", "categoria": "Almacenamiento", "marca": "Crucial", "precio": 70000, "stock": 3},
    {"codigo": "R003", "descripcion": "Memoria RAM 8 GB DDR4", "categoria": "Memoria", "marca": "Kingston", "precio": 30000, "stock": 0},
    {"codigo": "R004", "descripcion": "Memoria RAM 16 GB DDR4", "categoria": "Memoria", "marca": "Corsair", "precio": 55000, "stock": 4},
    {"codigo": "R005", "descripcion": "Fuente de alimentación 600W", "categoria": "Fuente", "marca": "Thermaltake", "precio": 80000, "stock": 2},
    {"codigo": "R006", "descripcion": "Disco rígido 1 TB", "categoria": "Almacenamiento", "marca": "Western Digital", "precio": 60000, "stock": 0},
    {"codigo": "R007", "descripcion": "Placa de video RTX 4060", "categoria": "Video", "marca": "MSI", "precio": 400000, "stock": 1},
    {"codigo": "R008", "descripcion": "Teclado mecánico", "categoria": "Periféricos", "marca": "Redragon", "precio": 45000, "stock": 6}
]

busqueda = input("Ingrese una parte de la descripción: ").lower()

coincidencias = 0
disponibles = 0

print("\nResultados de la búsqueda:")

for repuesto in repuestos:
    if busqueda in repuesto["descripcion"].lower():
        coincidencias += 1

        print(f"\nCódigo: {repuesto['codigo']}")
        print(f"Descripción: {repuesto['descripcion']}")
        print(f"Categoría: {repuesto['categoria']}")
        print(f"Marca: {repuesto['marca']}")
        print(f"Precio: ${repuesto['precio']}")
        print(f"Stock: {repuesto['stock']}")

        if repuesto["stock"] > 0:
            print("Disponible: Sí")
            disponibles += 1
        else:
            print("Disponible: No")

if coincidencias == 0:
    print("\nLa búsqueda no produjo resultados.")
else:
    print(f"\nCantidad total de coincidencias: {coincidencias}")
    print(f"Cantidad de repuestos disponibles: {disponibles}")