# Ejercicio 1 - Control del laboratorio antes de una clase

equipos = [
    {"inventario": 101, "tipo": "PC", "marca": "Lenovo", "estado": "Disponible", "anio": 2023},
    {"inventario": 102, "tipo": "Notebook", "marca": "HP", "estado": "En reparación", "anio": 2022},
    {"inventario": 103, "tipo": "PC", "marca": "Dell", "estado": "Disponible", "anio": 2024},
    {"inventario": 104, "tipo": "Monitor", "marca": "Samsung", "estado": "Baja", "anio": 2020},
    {"inventario": 105, "tipo": "Notebook", "marca": "Lenovo", "estado": "Disponible", "anio": 2025},
    {"inventario": 106, "tipo": "PC", "marca": "HP", "estado": "Disponible", "anio": 2021},
    {"inventario": 107, "tipo": "Monitor", "marca": "LG", "estado": "En reparación", "anio": 2023},
    {"inventario": 108, "tipo": "Notebook", "marca": "Dell", "estado": "Disponible", "anio": 2024}
]

anio_minimo = int(input("Ingrese el año mínimo: "))

cantidad = 0

print("\nEquipos disponibles que cumplen la condición:")

# Único recorrido de la lista
for equipo in equipos:
    if equipo["estado"] == "Disponible" and equipo["anio"] >= anio_minimo:
        print(f"Inventario: {equipo['inventario']}")
        print(f"Tipo: {equipo['tipo']}")
        print(f"Marca: {equipo['marca']}")
        print(f"Año: {equipo['anio']}")
        print("-" * 30)

        cantidad += 1

if cantidad == 0:
    print("No existe ningún equipo disponible que cumpla con el año indicado.")
else:
    print(f"Cantidad de equipos que cumplen ambas condiciones: {cantidad}")